import unittest
from nodes.textnode import TextNode, TextType
from utils.convert import markdown_to_blocks, text_node_to_html_node, text_to_text_nodes

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
            
class TestTextToTextNodes(unittest.TestCase):
    # should split the text into TEXT, BOLD, ITALIC, CODE, IMAGE, and LINK text nodes
    def test_text_to_text_nodes_with_multiple_formats(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        self.assertListEqual(
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("text", TextType.BOLD),
                TextNode(" with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word and a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" and an ", TextType.TEXT),
                TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
                TextNode(" and a ", TextType.TEXT),
                TextNode("link", TextType.LINK, "https://boot.dev"),
            ],
            nodes
        )
        
class TestMarkdownBlocks(unittest.TestCase):
    def test_multiple_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
        
    def test_single_block(self):
        md = "This is a single paragraph"
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is a single paragraph"
            ],
        )
        
    def test_empty_markdown_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                ""
            ],
        )
        
    def test_invalid_markdown_type_int(self):
        md = 12345
        with self.assertRaises(TypeError):
            markdown_to_blocks(md)
            
    def test_invalid_markdown_type_list(self):
        md = ["This is a single paragraph"]
        with self.assertRaises(TypeError):
            markdown_to_blocks(md)
            
    def test_invalid_markdown_type_dict(self):
        md = {"This is a single paragraph": "This is a single paragraph"}
        with self.assertRaises(TypeError):
            markdown_to_blocks(md)
            
    def test_invalid_markdown_type_none(self):
        md = None
        with self.assertRaises(TypeError):
            markdown_to_blocks(md)
               
if __name__ == "__main__":
    unittest.main()