import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, 'https://boot.dev')
        node2 = TextNode('This is a text node', TextType.BOLD, 'https://boot.dev')
        self.assertEqual(node, node2)
        
    def test_not_eq(self):
        node = TextNode('This is a text node', TextType.BOLD, 'https://boot.dev')
        node2 = TextNode('This is another text node', TextType.CODE, 'http://boot.dev')
        self.assertNotEqual(node, node2)
        
    def test_eq_without_url(self):
        node = TextNode('This is a text node', TextType.CODE)
        node2 = TextNode('This is a text node', TextType.CODE)
        self.assertEqual(node, node2)
        
    def test_not_eq_type(self):
        node = TextNode('This is a text node', TextType.BOLD, 'https://boot.dev')
        node2 = TextNode('This is a text node', TextType.CODE, 'https://boot.dev')
        self.assertNotEqual(node, node2)
        
    def test_not_eq_url(self):
        node = TextNode('This is a text node', TextType.BOLD, 'http://boot.dev')
        node2 = TextNode('This is a text node', TextType.BOLD, 'https://boot.dev')
        self.assertNotEqual(node, node2)
        
    def test_not_eq_text(self):
        node = TextNode('This is a text node', TextType.BOLD, 'https://boot.dev')
        node2 = TextNode('This is another text node', TextType.BOLD, 'https://boot.dev')
        self.assertNotEqual(node, node2)
        
if __name__ == '__main__':
    unittest.main()