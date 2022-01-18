from functools import cache
from pathlib import Path

import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import ORJSONResponse
from fastapi.responses import Response
from fastapi.templating import Jinja2Templates

root_folder: Path = Path(__file__).parent
logos_folder: Path = root_folder / "static" / "logos"
templates: Jinja2Templates = Jinja2Templates(str(root_folder))

badge_template: dict[str, str | int] = {
    "schemaVersion": 1,
    "label": "Furry",
    "message": "Badge",
}

colors: dict[str, tuple[str, str]] = {
    "furaffinity": ("#151718", "#FAAF3A"),
    "weasyl": ("#1D2224", "#990000")
}

logos: dict[str, str] = {p.name.removesuffix(".svg"): p.read_text() for p in logos_folder.iterdir()}

app: FastAPI = FastAPI(servers=[{"url": "https://furry-badges.herokuapp.com"}],
                       license_info={"name": "European Union Public Licence v. 1.2", "url": "https://eupl.eu/1.2/en"},
                       docs_url=None, redoc_url=None)

app.add_route("/",
              lambda r: templates.TemplateResponse("index.html", {"request": r, "sites": [*logos.keys()]}),
              ["GET"])


def get_badge(endpoint: str, **params) -> Response:
    res: requests.Response = requests.request("GET", f"https://img.shields.io/endpoint",
                                              params={"url": endpoint} | params)
    return Response(
        res.content,
        res.status_code,
        media_type=res.headers.get("Content-Type", None)
    )


@app.get("/badge/endpoint/{site}/{username}/", response_class=ORJSONResponse)
@app.get("/badge/endpoint/{site}/{username}/{label}/", response_class=ORJSONResponse)
def badge_endpoint(site: str, username: str, label: str = None):
    site_: str = site.lower()
    badge_label: dict = {"label": label or site_, "message": username}
    badge_colors: dict = {"labelColor": colors[site_][0], "color": colors[site_][1]} if site_ in colors else {}
    return badge_template | badge_label | badge_colors | badge_logo


@app.get("/badge/user/{site}/{username}/", response_class=Response)
@app.get("/badge/user/{site}/{username}/{label}/", response_class=Response)
def badge_user(request: Request, site: str, username: str, label: str = None):
    return get_badge(app.servers[0]["url"] +
                     app.url_path_for(badge_endpoint.__name__, site=site, username=username,
                                      **({"label": label} if label else {})),
                     **request.query_params)
