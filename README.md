<div align="center">

<img alt="logo" width="400" src="https://raw.githubusercontent.com/FurryCoders/Logos/main/logos/furry-badges-transparent.png">

# Furry Badges

Create badges for furry websites with the [Shields.io](https://shields.io) API.

Build your own badge online at [furry-badges.herokuapp.com](https://furry-badges.herokuapp.com)!

Do you have suggestions on new logos and
sites? [Open a logo request!](https://github.com/FurryCoders/Furry-Badges/issues/new?assignees=MatteoCampinoti94&labels=enhancement&template=logo-request.yml&title=%5BLogo+Request%5D%3A+)

</div>

## User Badge

To create a user badge, use the `/badge/user/{site}/{username}` and `/badge/user/{site}/{username}/{label}` routes.

For example: `https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA`
-> [![](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the site used. Logos and colors are provided for the following websites:

| Site           | Logo                                                                                                                                     |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| `furry`        | [![](https://furry-badges.herokuapp.com/badge/user/Furry/Logo)](https://furry-badges.herokuapp.com/badge/user/furry/Logo)                |
| `buzzly`       | [![](https://furry-badges.herokuapp.com/badge/user/buzzly/Logo)](https://furry-badges.herokuapp.com/badge/user/buzzly/Logo)              |
| `deviantart`   | [![](https://furry-badges.herokuapp.com/badge/user/deviantart/Logo)](https://furry-badges.herokuapp.com/badge/user/deviantart/Logo)      |
| `e621`         | [![](https://furry-badges.herokuapp.com/badge/user/e621/Logo)](https://furry-badges.herokuapp.com/badge/user/e621/Logo)                  |
| `furaffinity`  | [![](https://furry-badges.herokuapp.com/badge/user/furaffinity/Logo)](https://furry-badges.herokuapp.com/badge/user/furaffinity/Logo)    |
| `furrynetwork` | [![](https://furry-badges.herokuapp.com/badge/user/furrynetwork/Logo/)](https://furry-badges.herokuapp.com/badge/user/furrynetwork/Logo) |
| `sofurry`      | [![](https://furry-badges.herokuapp.com/badge/user/sofurry/Logo)](https://furry-badges.herokuapp.com/badge/user/sofurry/Logo)            |
| `vcl`          | [![](https://furry-badges.herokuapp.com/badge/user/vcl/Logo)](https://furry-badges.herokuapp.com/badge/user/vcl/Logo)                    |
| `weasyl`       | [![](https://furry-badges.herokuapp.com/badge/user/weasyl/Logo)](https://furry-badges.herokuapp.com/badge/user/weasyl/Logo)              |
| `wikifur`      | [![](https://furry-badges.herokuapp.com/badge/user/wikifur/Logo)](https://furry-badges.herokuapp.com/badge/user/wikifur/Logo)            |
| `yiffstar`     | [![](https://furry-badges.herokuapp.com/badge/user/yiffstar/Logo/Yiffstar)](https://furry-badges.herokuapp.com/badge/user/yiffstar/Logo) |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## Animal Badge

To create an animal badge, use the `/badge/animal/{animal}/{username}` and `/badge/animal/{animal}/{username}/{label}`
routes.

For example: `https://furry-badges.herokuapp.com/badge/animal/fox/User/Foxy`
-> [![](https://furry-badges.herokuapp.com/badge/animal/fox/User/Foxy)](https://furry-badges.herokuapp.com/badge/animal/fox/User/Foxy)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the animal used. Logos and colors are provided for the following websites:

| Animal   | Logo                                                                                                                            |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------|
| `furry`  | [![](https://furry-badges.herokuapp.com/badge/animal/Furry/Logo)](https://furry-badges.herokuapp.com/badge/animal/Furry/Logo)   |
| `bear`   | [![](https://furry-badges.herokuapp.com/badge/animal/bear/Logo)](https://furry-badges.herokuapp.com/badge/animal/bear/Logo)     |
| `dragon` | [![](https://furry-badges.herokuapp.com/badge/animal/dragon/Logo)](https://furry-badges.herokuapp.com/badge/animal/dragon/Logo) |
| `fox`    | [![](https://furry-badges.herokuapp.com/badge/animal/fox/Logo)](https://furry-badges.herokuapp.com/badge/animal/fox/Logo)       |
| `tiger`  | [![](https://furry-badges.herokuapp.com/badge/animal/tiger/Logo)](https://furry-badges.herokuapp.com/badge/animal/tiger/Logo)   |
| `wolf`   | [![](https://furry-badges.herokuapp.com/badge/animal/wolf/Logo)](https://furry-badges.herokuapp.com/badge/animal/wolf/Logo)     |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## JSON Endpoint

The `/badge/endpoint/` route is used as endpoint for the Shields.io API.

## Credits

* [Buzzly logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/buzzly.svg) belongs
  to [Buzzly.art](https://buzzly.art).
* [DeviantArt logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/deviantart.svg) belongs
  to [DeviantArt](https://deviantart.com).
* [e621 logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/e621.svg) belongs
  to [e621](https://e621.net).
* [Fur Affinity logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/furaffinity.svg) belongs
  to [Fur Affinity](https://furaffinity.net).
* [Furry Network logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/furrynetwork.svg) belongs
  to [Furry Network](https://furrynetwork.com).
* [So Furry logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/sofurry.svg) belongs
  to [So Furry](https://sofurry.com) (converted to SVG format).
* [VCL logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/vcl.svg) belongs
  to [VCL](http://us.vclart.net/vcl/) (converted to SVG format).
* [Weasyl logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/weasyl.svg) belongs
  to [Weasyl](https://weasyl.com).
* [WikiFur logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/wikifur.svg) belongs
  to [WikiFur](https://wikifur.com/) (converted to SVG format).
* [Yiffstar logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/yiffstar.svg) belongs
  to the defunct Yiffstar, logo sourced from [WikiFur - Yiffstar](https://en.wikifur.com/wiki/Yiffstar).

[Animal icons](https://github.com/FurryCoders/Furry-Badges/tree/main/static/icons) sourced
from [SVG Repo](https://www.svgrepo.com/)
