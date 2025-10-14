import unittest

from htmlnode import HTMLNode, LeafNode

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode(
            "p",
            "This is a paragraph of text.",
        )
        self.assertEqual(
            node.to_html(),
            "<p>This is a paragraph of text.</p>",
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")          

    def test_leaf_with_prop(self):
        node = LeafNode(
            "a", 
            "Click me!", 
            {"href": "https://www.google.com"}
        )
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_repr(self):
        node = LeafNode("a","Hi!",{"href": "www.google.com"})
        self.assertEqual(repr(node), "LeafNode(a, Hi!, {'href': 'www.google.com'})")

if __name__ == "__main__":
    unittest.main()
