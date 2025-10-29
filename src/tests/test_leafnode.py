import unittest

from nodes.htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!", {"class": "paragraph", "name": "first"})
        self.assertEqual(node.to_html(), '<p class="paragraph" name="first">Hello, world!</p>')

    def test_leaf_to_html_no_props(self):
        node = LeafNode("strong", "Bold text")
        self.assertEqual(node.to_html(), '<strong>Bold text</strong>')

    def test_leaf_to_html_none_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), 'Just text')

    def test_leaf_to_html_empty_value_raises(self):
        node = LeafNode("span", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_with_one_prop(self):
        node = LeafNode("a", "link here", {"href": "https://example.com"})
        self.assertEqual(node.to_html(), '<a href="https://example.com">link here</a>')

    def test_leaf_to_html_empty_props_dict(self):
        node = LeafNode("em", "Em text", {})
        self.assertEqual(node.to_html(), '<em>Em text</em>')

    def test_leaf_to_html_multiple_props(self):
        node = LeafNode("div", "Block", {"id": "main", "style": "color:red;"})
        html = node.to_html()
        self.assertIn('id="main"', html)
        self.assertIn('style="color:red;"', html)
        self.assertTrue(html.startswith("<div") and html.endswith(">Block</div>"))
        
if __name__ == '__main__':
    unittest.main()