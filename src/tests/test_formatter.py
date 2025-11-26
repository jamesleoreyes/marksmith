import unittest

from nodes.textnode import TextNode, TextType
from utils.formatter import split_nodes_delimiter, split_nodes_image


class TestDelimiter(unittest.TestCase):
    # should split the text into TEXT nodes and CODE nodes for each code block
    def test_text_with_single_code_block(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ]
        )
        
    # should raise an exception if the code block is incomplete
    def test_incomplete_code_delimiter(self):
        node = TextNode("This is text with an `incomplete delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)
            
    # should split the text into TEXT nodes and BOLD nodes for each bold text
    def test_text_with_single_bold_text(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ]
        )
        
    # should raise an exception if the bold text is incomplete
    def test_incomplete_bold_delimiter(self):
        node = TextNode("This is text with an **incomplete delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)
        
    # should split the text into TEXT nodes and ITALIC nodes for each italic text
    def test_text_with_single_italic_text(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT)
            ]
        )
        
    # should raise an exception if the italic text is incomplete
    def test_incomplete_italic_delimiter(self):
        node = TextNode("This is text with an _incomplete delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)
            
    # should simply return the node as BOLD since it's not a valid TEXT syntax
    def test_non_text_type_nodes(self):
        node = TextNode("This is a text with a **bold** word", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [TextNode("This is a text with a **bold** word", TextType.BOLD)]
        )

class TestImageSplitter(unittest.TestCase):
    # should split the text into TEXT nodes and IMAGE nodes for each image
    def test_text_with_multiple_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )
        
    # should split the text into 1 TEXT node and 1 IMAGE node
    def test_text_with_single_image_and_no_text_after(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png")
            ],
            new_nodes,
        )
        
    # should split the text into 2 TEXT nodes and 1 IMAGE node with text before and after the image
    def test_text_with_single_image_and_text_after(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and some text after",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and some text after", TextType.TEXT),
            ],
            new_nodes,
        )
    
    # should simply return the node as TEXT since it does not contain any images
    def test_text_with_no_images(self):
        node = TextNode(
            "This is a text without an image",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is a text without an image", TextType.TEXT)
            ],
            new_nodes
        )
    
    # should simply return the node as LINK since it's a valid link syntax
    def test_non_text_type_nodes(self):
        node = TextNode(
            "Wikipedia",
            TextType.LINK,
            "https://wikipedia.com"
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("Wikipedia", TextType.LINK, 'https://wikipedia.com')
            ],
            new_nodes
        )
        
    # should simply return the node as TEXT since it's not a valid image syntax
    def test_text_with_missing_end_parenthesis(self):
        node = TextNode(
            "This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [TextNode("This is a text with an ![image](https://i.imgur.com/zjjcJKZ.png", TextType.TEXT)],
            new_nodes
        )
  
if __name__ == "__main__":
    unittest.main()