from functools import cache
from pathlib import Path

import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import ORJSONResponse
from fastapi.responses import RedirectResponse
from fastapi.responses import Response

root_folder: Path = Path(__file__).parent
logos_folder: Path = root_folder / "static" / "logos"

app: FastAPI = FastAPI(servers=[{"url": "https://furry-badges.herokuapp.com"}],
                       license_info={"name": "European Union Public Licence v. 1.2", "url": "https://eupl.eu/1.2/en"},
                       docs_url=None, redoc_url=None)

app.add_route("/", lambda r: RedirectResponse("https://gitlab.com/projects/32921925"), ["GET"])

badge: dict[str, str | int] = {
    "schemaVersion": 1,
    "label": "Furry",
    "message": "Badge",
}

colors: dict[str, tuple[str, str]] = {
    "furaffinity": ("#151718", "#FAAF3A"),
    "fa": ("#151718", "#FAAF3A"),
    "weasyl": ("#1D2224", "#990000")
}
logos: dict[str, str] = {p.name.removesuffix(".svg"): p.read_text() for p in logos_folder.iterdir()}


@cache
def get_badge(endpoint: str, **params) -> Response:
    res: requests.Response = requests.request("GET", f"https://img.shields.io/endpoint",
                                              params={"url": endpoint} | params)
    return Response(
        res.content,
        res.status_code,
        media_type=res.headers.get("Content-Type", None)
    )


@app.get("/badge/endpoint/{site}/{username}", response_class=ORJSONResponse)
def badge_endpoint(username: str, site: str = None):
    site_: str = site.lower()
    badge_colors: dict = {"labelColor": colors[site_][0], "color": colors[site_][1]} if site_ in colors else {}
    badge_logo: dict = {"logoSvg": logos[site_]} if site_ in logos else {}
    return badge | {"label": site, "message": username} | badge_colors | badge_logo


@app.get("/badge/user/{site}/{username}", response_class=Response)
def badge_user(request: Request, site: str, username: str):
    return get_badge(app.servers[0]["url"] + app.url_path_for(badge_endpoint.__name__, site=site, username=username),
                     **request.query_params)
