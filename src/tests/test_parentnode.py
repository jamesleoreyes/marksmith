import unittest

from nodes.htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_children_and_props(self):
        child_node = LeafNode("div", "Test", {"class": "main"})
        parent_node = ParentNode("div", [child_node], {"id": "heading"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="heading"><div class="main">Test</div></div>'
        )
        
    def test_to_html_with_children_and_empty_parent_props_dict(self):
        child_node = LeafNode("div", "Another test", None)
        parent_node = ParentNode("div", [child_node], {})
        self.assertEqual(
            parent_node.to_html(),
            '<div><div>Another test</div></div>'
        )
        
    def test_to_html_with_missing_parent_tag(self):
        child_node = LeafNode("p", "This is a paragraph", None)
        parent_node = ParentNode("", [child_node], None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
            
    def test_to_html_with_none_child_value(self):
        child_node = LeafNode("p", None, None)
        parent_node = ParentNode("div", [child_node], None)
        with self.assertRaises(ValueError):
            parent_node.to_html()
        
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
        
    def test_to_html_with_2_grandchildren(self):
        great_grandchild_node = LeafNode("p", "Hehehe")
        grandchild_node = ParentNode("div", [great_grandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("main", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<main><div><div><p>Hehehe</p></div></div></main>'
        )
        
    def test_to_html_with_3_grandchildren(self):
        great_great_grandchild_node = LeafNode("p", 'This is not an image', {"id": "not-an-image"})
        great_grandchild_node = ParentNode("div", [great_great_grandchild_node], {"class": "paragraph"})
        grandchild_node = ParentNode("div", [great_grandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("main", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<main><div><div><div class="paragraph"><p id="not-an-image">This is not an image</p></div></div></div></main>'
        )
        
if __name__ == '__main__':
    unittest.main()