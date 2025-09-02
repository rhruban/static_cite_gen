import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_eq(self):
        node = HTMLNode("a", "My website", None, {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("a", "My website", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = HTMLNode("a", "My website", None, {"href": "https://www.google.com","target": "_blank",})
        node2 = HTMLNode("p", "My website", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = HTMLNode("a", "My website", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(
            "HTMLNode(a, My website, children: None, {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node)
        )

            
if __name__ == "__main__":
    unittest.main()
