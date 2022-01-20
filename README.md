<div align="center">

<img alt="logo" width="400" src="https://raw.githubusercontent.com/FurryCoders/Logos/main/logos/furry-badges-transparent.png">

# Furry Badges

Create badges for furry websites with the [Shields.io](https://shields.io) API.

Build your own badge online at [furry-badges.herokuapp.com](https://furry-badges.herokuapp.com)!

</div>

## User Badge

To create a user badge, use the `/badge/user/{site}/{username}` and `/badge/user/{site}/{username}/{label}` routes.

For example: `https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA`
-> [![](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the site used. Logos and colors are provided for the following websites:

| Site           | Logo                                                                                                                                    |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| `furry`        | [![](https://furry-badges.herokuapp.com/badge/user/Furry/Logo)](https://furry-badges.herokuapp.com/badge/user/Furry/Logo)               |
| `e621`         | [![](https://furry-badges.herokuapp.com/badge/user/e621/Logo)](https://furry-badges.herokuapp.com/badge/user/e621/Logo)                 |
| `furaffinity`  | [![](https://furry-badges.herokuapp.com/badge/user/FurAffinity/Logo)](https://furry-badges.herokuapp.com/badge/user/FurAffinity/Logo)   |
| `furrynetwork` | [![](https://furry-badges.herokuapp.com/badge/user/FurryNetwork/Logo)](https://furry-badges.herokuapp.com/badge/user/FurryNetwork/Logo) |
| `sofurry`      | [![](https://furry-badges.herokuapp.com/badge/user/SoFurry/Logo)](https://furry-badges.herokuapp.com/badge/user/SoFurry/Logo)           |
| `weasyl`       | [![](https://furry-badges.herokuapp.com/badge/user/Weasyl/Logo)](https://furry-badges.herokuapp.com/badge/user/Weasyl/Logo)             |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## Animal Badge

To create an animal badge, use the `/badge/animal/{animal}/{username}` and `/badge/animal/{animal}/{username}/{label}`
routes.

| Site     | Logo                                                                                                                            |
|:---------|:--------------------------------------------------------------------------------------------------------------------------------|
| `furry`  | [![](https://furry-badges.herokuapp.com/badge/animal/Furry/Logo)](https://furry-badges.herokuapp.com/badge/animal/Furry/Logo)   |
| `dragon` | [![](https://furry-badges.herokuapp.com/badge/animal/dragon/Logo)](https://furry-badges.herokuapp.com/badge/animal/dragon/Logo) |
| `fox`    | [![](https://furry-badges.herokuapp.com/badge/animal/fox/Logo)](https://furry-badges.herokuapp.com/badge/animal/fox/Logo)       |
| `tiger`  | [![](https://furry-badges.herokuapp.com/badge/animal/tiger/Logo)](https://furry-badges.herokuapp.com/badge/animal/tiger/Logo)   |
| `wolf`   | [![](https://furry-badges.herokuapp.com/badge/animal/wolf/Logo)](https://furry-badges.herokuapp.com/badge/animal/wolf/Logo)     |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link.

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## JSON Endpoint

The `/badge/endpoint/{site}/{username}` route is used as endpoint for the Shields.io API.
