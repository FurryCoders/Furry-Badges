<?php /** @noinspection SpellCheckingInspection */

const DATA = [
    "user" => [
        "furry" => [
            "alias" => "Furry",
            "icon" => "furry.svg"
        ],
        "buzzly" => [
            "alias" => "Buzzly",
            "colors" => ["#EE9B00", "#79340E"],
            "icon" => "buzzly.svg"
        ],
        "deviantart" => [
            "alias" => "DeviantArt",
            "colors" => ["#475C4D", "#00E59B"],
            "icon" => "deviantart.svg"
        ],
        "e621" => [
            "alias" => "e621",
            "colors" => ["#FDBE2F", "#00549E"],
            "icon" => "e621.svg"
        ],
        "furaffinity" => [
            "alias" => "Fur Affinity",
            "colors" => ["#151718", "#FAAF3A"],
            "icon" => "furaffinity.svg"
        ],
        "furrynetwork" => [
            "alias" => "Furry Network",
            "colors" => ["#FFFFFF", "#2E76B4"],
            "icon" => "furrynetwork.svg"
        ],
        "sofurry" => [
            "alias" => "SoFurry",
            "colors" => ["#543D3B", "#C05D00"],
            "icon" => "sofurry.svg"
        ],
        "vcl" => [
            "alias" => "VCL",
            "colors" => ["#005E74", "#DA5A36"],
            "icon" => "vcl.svg"
        ],
        "weasyl" => [
            "alias" => "Weasyl",
            "colors" => ["#1D2224", "#990000"],
            "icon" => "weasyl.svg"
        ],
        "wikifur" => [
            "alias" => "WikiFur",
            "colors" => ["#FFFFFF", "#43459C"],
            "icon" => "wikifur.svg"
        ],
        "yiffstar" => [
            "alias" => "Yiffstar",
            "colors" => ["#2771CF", "#FFFFFF"],
            "icon" => "yiffstar.svg"
        ]
    ],
    "animal" => [
        "furry" => [
            "alias" => "Furry",
            "icon" => "furry.svg"
        ],
        "fox" => [
            "alias" => "Fox",
            "colors" => ["#FFFFFF", "#DF701F"],
            "icon" => "fox.svg"
        ],
        "tiger" => [
            "alias" => "Tiger",
            "colors" => ["#000000", "#F0C419"],
            "icon" => "tiger.svg"
        ],
        "wolf" => [
            "alias" => "Wolf",
            "colors" => ["#C3B9B1", "#878791"],
            "icon" => "wolf.svg"
        ],
        "dragon" => [
            "alias" => "Dragon",
            "colors" => ["#EA5A47", "#B1CC33"],
            "icon" => "dragon.svg"
        ],
        "bear" => [
            "alias" => "Bear",
            "colors" => ["#D7B487", "#7C665D"],
            "icon" => "bear.svg"
        ],
        "horse" => [
            "alias" => "Horse",
            "colors" => ["#E1A178", "#96695F"],
            "icon" => "horse.svg"
        ]
    ],
];


function badge_parameters($type, $site, $name, $label): ?array
{
    $type = strtolower(urldecode($type));
    $site = strtolower(urldecode($site));
    $name = urldecode($name);
    $label = urldecode($label);

    if (!isset(DATA[$type])) return null;
    elseif (!isset(DATA[$type][$site])) return null;

    $parameters = [
        "schemaVersion" => 1,
        "label" => $label ?: DATA[$type][$site]["alias"],
        "message" => $name,
    ];

    if (isset(DATA[$type][$site]["colors"])) {
        $parameters["labelColor"] = DATA[$type][$site]["colors"][0];
        $parameters["color"] = DATA[$type][$site]["colors"][1];
    }

    if (file_exists(__DIR__ . "/static/icons/" . DATA[$type][$site]["icon"])) {
        $parameters["logoSvg"] = file_get_contents(__DIR__ . "/static/icons/" . DATA[$type][$site]["icon"]);
    }

    return $parameters;
}


function badge_json()
{
    header("Content-Type: application/json");

    preg_match("/^\/badge\/json\/([^\/]+)\/([^\/]+)\/([^\/]+)(?:\/([^\/]+))?\/?$/", $_SERVER["REQUEST_URI"], $matches);

    $parameters = null;

    if (isset($matches[0])) {
        $parameters = badge_parameters($matches[1], $matches[2], $matches[3], $matches[4] ?? null);
    }

    if ($parameters) {
        header("Status: 200 OK", true, 200);
        echo(json_encode($parameters));
    } else {
        header("Status: 404 Not Found", true, 404);
        echo(json_encode(["error" => "Invalid path"]));
    }
}

function badge_svg()
{
    $url = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH);
    $query_string = parse_url($_SERVER["REQUEST_URI"], PHP_URL_QUERY);
    preg_match("/^\/badge\/svg\/([^\/]+)\/([^\/]+)\/([^\/]+)(?:\/([^\/]+))?\/?$/", $url, $matches);

    if (
        !isset($matches[0]) ||
        !isset(DATA[urldecode($matches[1])]) ||
        !isset(DATA[urldecode($matches[1])][str_ireplace(" ", "", strtolower(urldecode($matches[2])))])
    ) {
        die(404);
    } else {
        $endpoint = (isset($_SERVER['HTTPS']) ? "https" : "http") .
            "://$_SERVER[HTTP_HOST]" .
            "/badge/json/$matches[1]/$matches[2]/$matches[3]/" . ($matches[4] ?? "");
        $endpoint = urlencode($endpoint);
        $response = file_get_contents("https://img.shields.io/endpoint?url=$endpoint&$query_string");
        if ($response) {
            header("Status: 200 OK", true, 200);
            header("Content-Type: image/svg+xml");
            echo($response);
        } else {
            die(404);
        }
    }
}


if ($_SERVER["REQUEST_URI"] == "/") {
    include_once "index.html";
} elseif ($_SERVER["REQUEST_URI"] == "/" . basename(__FILE__)) {
    header("Location: " . (isset($_SERVER['HTTPS']) ? "https" : "http") . "://$_SERVER[HTTP_HOST]", true, 301);
} elseif (strpos($_SERVER["REQUEST_URI"], "/static") === 0) {
    die(404);
} elseif (strpos($_SERVER["REQUEST_URI"], "/badge/json/") === 0) {
    badge_json();
} elseif (strpos($_SERVER["REQUEST_URI"], "/badge/svg/") === 0) {
    badge_svg();
} else {
    header("Location: " . (isset($_SERVER['HTTPS']) ? "https" : "http") . "://$_SERVER[HTTP_HOST]", true, 301);
}