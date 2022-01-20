<div align="center">

<img alt="logo" width="400" src="https://raw.githubusercontent.com/FurryCoders/Logos/main/logos/furry-badges-transparent.png">

# Furry Badges

Create badges for furry websites with the [Shields.io](https://shields.io) API.

Build your own badge online at [furry-badges.herokuapp.com](https://furry-badges.herokuapp.com)!

</div>

## User Badge

To create a user badge, use the `/badge/{site}/{username}` and `/badge/{site}/{username}/{label}` routes.

For example: `https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA`
-> [![](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)](https://furry-badges.herokuapp.com/badge/user/furaffinity/User/FA)

The label can be specified either in the path, or using the `?label` query parameter. The latter will override the path
value. To disable the label entirely whilst keeping the logo, use `?label=+` as query parameter.

Colors and logos change depending on the site used. Logos and colors are provided for the following websites:

| Site          | Site Code      | Logo                                                                                                                                    |
|:--------------|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------|
| Generic paw   | `furry`        | [![](https://furry-badges.herokuapp.com/badge/user/Furry/Logo)](https://furry-badges.herokuapp.com/badge/user/Furry/Logo)               |
| e621          | `e621`         | [![](https://furry-badges.herokuapp.com/badge/user/e621/Logo)](https://furry-badges.herokuapp.com/badge/user/e621/Logo)                 |
| Fur Affinity  | `furaffinity`  | [![](https://furry-badges.herokuapp.com/badge/user/FurAffinity/Logo)](https://furry-badges.herokuapp.com/badge/user/FurAffinity/Logo)   |
| Furry Network | `furrynetwork` | [![](https://furry-badges.herokuapp.com/badge/user/FurryNetwork/Logo)](https://furry-badges.herokuapp.com/badge/user/FurryNetwork/Logo) |
| So Furry      | `sofurry`      | [![](https://furry-badges.herokuapp.com/badge/user/SoFurry/Logo)](https://furry-badges.herokuapp.com/badge/user/SoFurry/Logo)           |
| Weasyl        | `weasyl`       | [![](https://furry-badges.herokuapp.com/badge/user/Weasyl/Logo)](https://furry-badges.herokuapp.com/badge/user/Weasyl/Logo)             |

_Note_: logos are matched case-insensitively, but the label on the badge will respect the site used in the link.<br/>

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## JSON Endpoint

The `/badge/endpoint/{site}/{username}` route is used as endpoint for the Shields.io API.
