import unittest
from utils.blocks import markdown_to_blocks, get_block_type, BlockType, markdown_to_html_node

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
            [],
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
            
class TestGetBlockType(unittest.TestCase):
    def test_heading_1(self):
        block = "# This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_heading_2(self):
        block = "## This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_heading_3(self):
        block = "### This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_heading_4(self):
        block = "#### This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_heading_5(self):
        block = "##### This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_heading_6(self):
        block = "###### This is a heading"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)
        
    def test_paragraph(self):
        block = "This is a paragraph"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.PARAGRAPH)
        
    def test_unordered_list(self):
        block = "- This is a list item\n- This is another list item"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)
        
    def test_ordered_list(self):
        block = "1. This is a list item\n2. This is another list item"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)
        
    def test_code(self):
        block = "```python\nprint('Hello, world!')\n```"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)
        
    def test_quote(self):
        block = "> This is a quote\n> This is another quote"
        block_type = get_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)
               
class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
               
if __name__ == "__main__":
    unittest.main()