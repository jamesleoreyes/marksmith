import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'This is a paragraph', None, None)
        node2 = HTMLNode('div', 'This is a div', None, None)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = HTMLNode('h1', 'Header', None, {'class': 'title'})
        try:
            node.__repr__()
        except Exception as e:
            self.fail(f"__repr__ raised an exception: {e}")

    def test_props_to_html_empty(self):
        node = HTMLNode('span', 'something', None, None)
        self.assertEqual(node.props_to_html(), ' ')

    def test_props_to_html_with_props(self):
        props = {'id': '"header"', 'class': '"main"'}
        node = HTMLNode('div', 'content', None, props)
        self.assertIn('id="header"', node.props_to_html())
        self.assertIn('class="main"', node.props_to_html())

    def test_to_html_not_implemented(self):
        node = HTMLNode('section', 'data', None, None)
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()