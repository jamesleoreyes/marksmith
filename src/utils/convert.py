from nodes.htmlnode import LeafNode
from nodes.textnode import TextNode, TextType
from utils.formatter import split_nodes_delimiter, split_nodes_image, split_nodes_link


def text_node_to_html_node(text_node: TextNode):
    if not isinstance(text_node.text_type, TextType):
        raise Exception('Invalid text type')
    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {"src": text_node.url, "alt": text_node.text})
        
def text_to_text_nodes(text: str):
    nodes: list[TextNode] = []
    
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)], "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_image(nodes)
    
    return nodes

def markdown_to_blocks(markdown: str) -> list[str]:
    if type(markdown) != str:
        raise TypeError('Markdown must be a string')
    
    result: list[str] = []
    blocks = markdown.split('\n\n')
    
    for block in blocks:
        stripped = block.strip()
        result.append(stripped)
        
    return result