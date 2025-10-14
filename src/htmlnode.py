class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __eq__(self,other):
        return (
            self.tag == other.tag
            and self.value == other.value 
            and self.children == other.children
            and self.props == other.props
        )

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

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

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent Node needs a tag")
        if self.children is None:
            raise ValueError("Parent Node needs child")
        htmlout = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            htmlout += child.to_html()
        htmlout += f"</{self.tag}>"
        return htmlout

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
