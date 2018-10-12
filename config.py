import os

port = 8888

base_dir = os.path.dirname(__file__)
static_path = os.path.join(base_dir, "static")
template_path = os.path.join(base_dir, "template")

pages = [
    {
        "name": "Home",
        "route": "/",
        "template": "home.html",
        "navbar-display": True,
        "navbar-display-text": "Home",
        "navbar-children": None
    },
    {
        "name": "About",
        "route": "/about",
        "template": "about.html",
        "navbar-display": True,
        "navbar-display-text": "About Me",
        "navbar-children": None
    }
]