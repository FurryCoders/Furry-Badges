# Fur Affinity Badge

[![furaffinity](https://furaffinity-badge.herokuapp.com/badge/user/FlameOfFurious)](https://furaffinity.net/user/FlameOfFurious)

Create badges for FurAffinity users using the Shields.io API.

## User Badge

To create a user badge, use the `/badge/user/{username}` route.

For example: `https://furaffinity-badge.herokuapp.com/badge/user/FlameOfFurious`
-> ![](https://furaffinity-badge.herokuapp.com/badge/user/FlameOfFurious)

The route supports all [Shields.io style parameters](https://shields.io/#styles) except for `message` (it's used by the
backend for the username).

The badge can be embedded in Markdown, reStructuredText, AsciiDoc, HTML, etc. like all Shields.io badges.

## JSON Endpoint

The `/badge/endpoint/` and `/badge/endpoint/{username}` routes are used as endpoints for the Shields.io API.
