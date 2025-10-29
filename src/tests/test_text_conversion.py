import unittest
from nodes.textnode import TextNode, TextType
from utils.convert import text_node_to_html_node

class TestTextConversion(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        
    def test_bold_text(self):
        node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
        
    def test_italic_text(self):
        node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
        
    def test_code_text(self):
        node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
        
    def test_link_text(self):
        node = TextNode("This is a link text node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
        
    def test_image_text(self):
        node = TextNode("This is an image text node", TextType.IMAGE, "https://boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, '')
        self.assertEqual(html_node.props, {"src": "https://boot.dev/image.png", "alt": "This is an image text node"})

    def test_invalid_text_type(self):
        node = TextNode("This is an invalid text node", "invalid")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
        
if __name__ == "__main__":
    unittest.main()