<div align="center">

<img alt="logo" width="400" src="https://raw.githubusercontent.com/FurryCoders/Logos/main/logos/furry-badges-transparent.png">

# Furry Badges

Create badges for furry websites with the [Shields.io](https://shields.io) API.

Build your own badge online at [furry-badges.codingfoxden.dk](https://furry-badges.codingfoxden.dk)!

Do you have suggestions on new logos and
sites? [Open a logo request!](https://github.com/FurryCoders/Furry-Badges/issues/new?assignees=MatteoCampinoti94&labels=enhancement&template=logo-request.yml&title=%5BLogo+Request%5D%3A+)

</div>

## User Badge

To create a user badge, use the `/badge/svg/user/{site}/{username}` and `/badge/svg/user/{site}/{username}/{label}`
routes.

For example: `https://furry-badges.codingfoxden.dk/badge/svg/user/furaffinity/user/FA`
-> [![](https://furry-badges.codingfoxden.dk/badge/svg/user/furaffinity/user/FA)](https://furry-badges.codingfoxden.dk/badge/svg/user/furaffinity/user/FA)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the site used. Logos and colors are provided for the following websites:

| Site           | Logo                                                                                                                                                 |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------|
| `furry`        | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/Furry/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/furry/Logo)                |
| `buzzly`       | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/buzzly/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/buzzly/Logo)              |
| `deviantart`   | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/deviantart/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/deviantart/Logo)      |
| `e621`         | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/e621/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/e621/Logo)                  |
| `furaffinity`  | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/furaffinity/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/furaffinity/Logo)    |
| `furrynetwork` | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/furrynetwork/Logo/)](https://furry-badges.codingfoxden.dk/badge/svg/user/furrynetwork/Logo) |
| `sofurry`      | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/sofurry/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/sofurry/Logo)            |
| `vcl`          | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/vcl/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/vcl/Logo)                    |
| `weasyl`       | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/weasyl/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/weasyl/Logo)              |
| `wikifur`      | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/wikifur/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/user/wikifur/Logo)            |
| `yiffstar`     | [![](https://furry-badges.codingfoxden.dk/badge/svg/user/yiffstar/Logo/Yiffstar)](https://furry-badges.codingfoxden.dk/badge/svg/user/yiffstar/Logo) |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link if no
other label is specified.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## Animal Badge

To create an animal badge, use the `/badge/svg/animal/{animal}/{username}`
and `/badge/svg/animal/{animal}/{username}/{label}`
routes.

For example: `https://furry-badges.codingfoxden.dk/badge/svg/animal/fox/user/Foxy`
-> [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/fox/user/Foxy)](https://furry-badges.codingfoxden.dk/badge/svg/animal/fox/user/Foxy)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the animal used. Logos and colors are provided for the following websites:

| Animal   | Logo                                                                                                                                        |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| `furry`  | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/Furry/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/Furry/Logo)   |
| `bear`   | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/bear/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/bear/Logo)     |
| `dragon` | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/dragon/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/dragon/Logo) |
| `fox`    | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/fox/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/fox/Logo)       |
| `horse`  | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/horse/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/horse/Logo)   |
| `tiger`  | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/tiger/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/tiger/Logo)   |
| `wolf`   | [![](https://furry-badges.codingfoxden.dk/badge/svg/animal/wolf/Logo)](https://furry-badges.codingfoxden.dk/badge/svg/animal/wolf/Logo)     |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the animal used in the link if no
other label is specified.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## JSON Endpoint

The `/badge/json/` route is used as endpoint for the Shields.io API and uses the following
format: `/badge/json/{user|animal}/{site}/{name}/{label}`

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
* [SoFurry logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/sofurry.svg) belongs
  to [SoFurry](https://sofurry.com) (converted to SVG format).
* [VCL logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/vcl.svg) belongs
  to [VCL](http://us.vclart.net/vcl/) (converted to SVG format).
* [Weasyl logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/weasyl.svg) belongs
  to [Weasyl](https://weasyl.com).
* [WikiFur logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/wikifur.svg) belongs
  to [WikiFur](https://wikifur.com/) (converted to SVG format).
* [Yiffstar logo](https://github.com/FurryCoders/furry-badges/blob/main/static/logos/yiffstar.svg) belongs to the
  defunct Yiffstar, logo sourced from [WikiFur - Yiffstar](https://en.wikifur.com/wiki/Yiffstar).

[Animal icons](https://github.com/FurryCoders/Furry-Badges/tree/main/static/icons) sourced
from [SVG Repo](https://www.svgrepo.com/)
