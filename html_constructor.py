from abc import ABC, abstractmethod

# pylint: disable = useless-suppression
# pylint: disable = import-error
from constructor_tag import ConstructorTag

# pylint: enable = import-error
# pylint: enable = useless-suppression


class Tag(ABC):
    @abstractmethod
    def __init__(self) -> None:
        self.constructor = ConstructorTag()
        self.tag = self.__class__.__name__.lower()

    @property
    def tag_open(self) -> str:
        """Return <tag>"""

        return "<" + self.tag + ">"

    @abstractmethod
    def tag_create(self) -> tuple:
        """Return (tag_open, tag_close, content)"""

    @property
    def tag_close(self) -> str:
        """Return </tag>"""

        return "</" + self.tag + ">"

    @property
    def tag_complete(self) -> str:
        """Return <tag> content </tag>"""

        return (
            self.constructor.create_tag(*self.tag_create())[
                : -len(self.tag_close)
            ]
            + "\n"
            + self.tag_close
        )


class Html(Tag):
    """
    [(rel, href),(rel_2, href_2)] -> example:

    Html(
        [('license', 'url'), ('icon', 'path'), ('stylesheet', 'path')],
        title="Document", language="en")
    """

    def __init__(
        self,
        title: str,
        language: str = "en",
        body: Tag = None,
        links: dict = None,
    ) -> None:
        super().__init__()
        self.lang = language
        self.title = title
        self.body = body
        self.prev_links = links
        self.spaces = self.constructor.spaces

    def __assembling_links(self) -> str:
        if self.prev_links:
            links = ""
            for url in self.prev_links:
                rel, href = url
                links += f'{self.spaces*2}<link rel="{rel}" href="{href}" />\n'

            return links

        return ""

    @property
    def tag_open(self) -> str:
        return (
            f"<!DOCTYPE html>\n<html lang='{self.lang}'>\n"
            + f"{self.spaces}<head>\n"
            + f'{self.spaces*2}<meta charset="UTF-8" />\n'
            f'{self.spaces*2}<meta http-equiv="X-UA-Compatible" '
            'content="IE=edge" />\n'
            f'{self.spaces*2}<meta name="viewport" '
            'content="width=device-width, initial-scale=1.0" />\n'
            + self.__assembling_links()
            + f"{self.spaces*2}<title>{self.title}</title>\n"
            f"{self.spaces}</head>"
        )

    def tag_create(self) -> str:
        if isinstance(self.body, Body):
            return self.tag_open, self.tag_close, [self.body]

        raise AttributeError("The content in <html> should only be <body>")


class Body(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class Header(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class Main(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class Footer(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class Div(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class A(Tag):  # pylint: disable = invalid-name
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
        content: list[Tag] = None,
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.content = content
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, self.content


class Img(Tag):
    def __init__(
        self,
        attributes: dict = None,
        style: dict = None,
        text: str = "",
    ) -> None:
        super().__init__()
        self.attributes = attributes
        self.style = style
        self.text = text
        self.tag = self.__class__.__name__.lower()

    def tag_create(self) -> str:
        tag_op = self.constructor.open_tag_default(
            tag=self.tag,
            attributes=self.attributes,
            style=self.style,
            text=self.text,
        )
        tag_cl = self.constructor.close_tag(self.tag)
        return tag_op, tag_cl, None
