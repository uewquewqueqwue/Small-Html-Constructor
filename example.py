from lorem import sentence

# pylint: disable = useless-suppression
# pylint: disable = import-error
from html_constructor import Html, Body, Div, Img

# pylint: enable = import-error
# pylint: enable = useless-suppression

divs = [
    Div(style={"color": "white", "font-size": "54px"}, text=sentence()),
    Div(style={"width": "300px",
                "height": "300px",
                "background-color": "#042326",
                "border-radius": "16px",}),
    Img(style={"width": "500px", "height": "500"},
        attributes={"src": "img.jpg"},),
]
body = Body(style={"background-color": "#0A3A40"}, content=divs)
html = Html(title="Document", body=body).tag_complete

with open(
    "index.html",
    "w",
    encoding="UTF-8",
) as file:
    file.write(html)
