class ConstructorTag:
    spaces = "  "

    def __init__(self) -> None:
        self.space = 0
        self.before = 0

    @staticmethod
    def __assembling_style(styles: tuple) -> str:
        if styles:
            style_complete = ' style="'
            for key, value in styles.items():
                style_complete += f"{key}: {value}; "

            return style_complete + '"'

        return ""

    @staticmethod
    def __assembling_attributes(attributes: dict) -> str:
        if attributes:
            id_class_complete = " "
            for key, value in attributes.items():
                id_class_complete += f'{key}="{value}" '

            return id_class_complete

        return ""

    def open_tag_default(
        self, tag: str, attributes: dict, style: dict, text: str
    ) -> str:
        return (
            f"<{tag}{self.__assembling_attributes(attributes)}"
            f"{self.__assembling_style(style)}>{text}"
        )

    @staticmethod
    def close_tag(tag: str) -> str:
        return f"</{tag}>"

    @classmethod
    def add_space(cls, string: str, amount: int) -> str:
        return (cls.spaces * amount) + string

    def create_tag(
        self, tag_open: str, tag_close: str, tag_content: list = None
    ) -> str:
        self.space += 1
        self.before = self.space
        content = ""
        if tag_content:
            for tag in tag_content:
                if not isinstance(tag, tuple):
                    tgop, tgcl, cont = tag.tag_create()
                else:
                    tgop, tgcl, cont = tag
                content += self.create_tag(
                    "\n" + self.add_space(tgop, self.before),
                    "\n" + self.add_space(tgcl, self.before),
                    cont,
                )
        self.space -= 1
        self.before = self.space
        return tag_open + content + tag_close

    def assembling_tags(self, tags: list) -> list:
        return [self.create_tag(*tag) for tag in tags]
