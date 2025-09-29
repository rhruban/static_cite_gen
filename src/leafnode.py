from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        html_out = ""
        if self.tag is None:
            html_out += self.value
        else:
            html_out += f'<{self.tag}'
            if self.props is not None:
                html_out += self.props_to_html()
            html_out += f'>{self.value}'
            html_out += f'</{self.tag}>'
        return html_out

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

