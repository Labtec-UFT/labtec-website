import bleach

# Tags permitidas
ALLOWED_TAGS = [
    "p", "b", "i", "strong", "em",
    "ul", "ol", "li",
    "a", "br",
    "div", "span",
    "h1", "h2", "h3", "h4", "h5", "h6",
    "img"
]

# Atributos permitidos
ALLOWED_ATTRS = {
    "*": ["class", "style"],
    "a": ["href", "title", "target", "rel"],
    "img": ["src", "alt", "title", "width", "height"]
}

def clean_html(text: str, strip_opt: bool = True) -> str:
    """
    Limpa HTML e protege contra XSS.

    :param text: Texto a ser limpo
    :param strip_opt: True remove tags não permitidas
    :return: HTML seguro
    """
    if not text:
        return ""

    return bleach.clean(
        text,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        strip=strip_opt
    )