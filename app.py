from functools import cache
from pathlib import Path

import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import ORJSONResponse
from fastapi.responses import Response

root_folder: Path = Path(__file__).parent
static_folder: Path = root_folder / "static"

app: FastAPI = FastAPI(servers=[{"url": "https://furaffinity-badge.herokuapp.com"}],
                       license_info={"name": "European Union Public Licence v. 1.2", "url": "https://eupl.eu/1.2/en"},
                       docs_url=None, redoc_url=None)

badge: dict[str, str | int] = {
    "schemaVersion": 1,
    "label": "FurAffinity",
    "message": "Badge",
    "color": "#FAAF3A",
    "labelColor": "#151718",
    "logoSvg": (static_folder / "logo.svg").read_text()
}


@cache
def get_badge(endpoint: str, **params) -> Response:
    res: requests.Response = requests.request("GET", f"https://img.shields.io/endpoint",
                                              params={"url": endpoint} | params)
    return Response(
        res.content,
        res.status_code,
        media_type=res.headers.get("Content-Type", None)
    )


@app.get("/badge/endpoint/", response_class=ORJSONResponse)
def badge_endpoint():
    return badge


@app.get("/badge/user/{username}", response_class=Response)
def badge_user(request: Request, username: str = ""):
    params: dict = {"message": username} | {k: v for k, v in request.query_params.items()}
    return get_badge(app.servers[0]["url"] + app.url_path_for(badge_endpoint.__name__), **params)
