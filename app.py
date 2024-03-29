from enum import Enum
from pathlib import Path
from urllib.parse import quote

import requests
from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import ORJSONResponse
from fastapi.responses import Response, HTMLResponse
from fastapi.staticfiles import StaticFiles


class BadgeType(Enum):
    user = "user"
    animal = "animal"


root_folder: Path = Path(__file__).parent
icons_folder: Path = root_folder / "static" / "icons"
assets_folder: Path = root_folder / "static" / "assets"

badge_template: dict[str, str | int] = {
    "schemaVersion": 1,
    "label": "Furry",
    "message": "Badge",
}

data: dict = {
    BadgeType.user.name: {
        "furry": {
            "alias": "Furry",
        },
        "buzzly": {
            "alias": "Buzzly",
            "colors": ("#EE9B00", "#79340E")
        },
        "deviantart": {
            "alias": "DeviantArt",
            "colors": ("#475C4D", "#00E59B")
        },
        "e621": {
            "colors": ("#FDBE2F", "#00549E")
        },
        "furaffinity": {
            "alias": "Fur Affinity",
            "colors": ("#151718", "#FAAF3A")
        },
        "furrynetwork": {
            "alias": "Furry Network",
            "colors": ("#FFFFFF", "#2E76B4")
        },
        "itaku": {
            "alias": "Itaku",
            "colors": ("#FFEB3B", "#303030")
        },
        "sofurry": {
            "alias": "SoFurry",
            "colors": ("#543D3B", "#C05D00")
        },
        "vcl": {
            "alias": "VCL",
            "colors": ("#005E74", "#DA5A36"),
        },
        "weasyl": {
            "alias": "Weasyl",
            "colors": ("#1D2224", "#990000")
        },
        "wikifur": {
            "alias": "WikiFur",
            "colors": ("#FFFFFF", "#43459C")
        },
        "yiffstar": {
            "alias": "Yiffstar",
            "colors": ("#2771CF", "#FFFFFF")
        }
    },
    BadgeType.animal.name: {
        "furry": {
            "alias": "Furry",
        },
        "fox": {
            "alias": "Fox",
            "colors": ("#FFFFFF", "#DF701F")
        },
        "tiger": {
            "alias": "Tiger",
            "colors": ("#000000", "#F0C419")
        },
        "wolf": {
            "alias": "Wolf",
            "colors": ("#C3B9B1", "#878791")
        },
        "dragon": {
            "alias": "Dragon",
            "colors": ("#EA5A47", "#B1CC33")
        },
        "bear": {
            "alias": "Bear",
            "colors": ("#D7B487", "#7C665D")
        },
        "horse": {
            "alias": "Horse",
            "colors": ("#E1A178", "#96695F")}
    }
}

icons: dict[str, str] = {p.name.removesuffix(".svg"): p.read_text() for p in icons_folder.iterdir()}

app: FastAPI = FastAPI(servers=[{"url": "https://furry-badges.herokuapp.com"}],
                       license_info={"name": "European Union Public Licence v. 1.2", "url": "https://eupl.eu/1.2/en"},
                       docs_url=None, redoc_url=None)

app.mount("/assets", StaticFiles(directory=assets_folder), "assets")
app.mount("/icons", StaticFiles(directory=icons_folder), "icons")


def get_badge(endpoint: str, **params) -> Response:
    res: requests.Response = requests.request("GET", f"https://img.shields.io/endpoint",
                                              params={"url": endpoint} | params)
    return Response(
        res.content,
        res.status_code,
        media_type=res.headers.get("Content-Type", None)
    )


@app.get("/", response_class=HTMLResponse)
def index():
    return HTMLResponse(root_folder.joinpath("index.html").read_text())


@app.get("/badge/endpoint/{badge_type}/{site}/{username}/", response_class=ORJSONResponse)
@app.get("/badge/endpoint/{badge_type}/{site}/{username}/{label}/", response_class=ORJSONResponse)
def badge_endpoint(badge_type: BadgeType, site: str, username: str, label: str = None):
    site_: str = site.lower().replace(" ", "")
    data_: dict = data[badge_type.name].get(site_, {})
    site = site if not site.islower() or " " in site else data_.get("alias", site)

    badge_label: dict = {"label": label or site, "message": username}
    badge_colors: dict = {"labelColor": data_["colors"][0], "color": data_["colors"][1]} if "colors" in data_ else {}
    badge_logo: dict = {"logoSvg": icons[site_]} if site_ in icons else {}

    return badge_template | badge_label | badge_colors | badge_logo


@app.get("/badge/user/{site}/{username}/", response_class=Response)
@app.get("/badge/user/{site}/{username}/{label}/", response_class=Response)
def badge_user(request: Request, site: str, username: str, label: str = None):
    return get_badge(app.servers[0]["url"] +
                     app.url_path_for(badge_endpoint.__name__, badge_type=BadgeType.user.name, site=site,
                                      username=quote(username), **({"label": quote(label)} if label else {})),
                     **request.query_params)


@app.get("/badge/animal/{icon}/{username}/", response_class=Response)
@app.get("/badge/animal/{icon}/{username}/{label}/", response_class=Response)
def badge_user(request: Request, icon: str, username: str, label: str = None):
    return get_badge(app.servers[0]["url"] +
                     app.url_path_for(badge_endpoint.__name__, badge_type=BadgeType.animal.name, site=icon,
                                      username=quote(username), **({"label": quote(label)} if label else {})),
                     **request.query_params)
