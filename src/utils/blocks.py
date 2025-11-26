from enum import Enum
import re
from nodes.htmlnode import HTMLNode, LeafNode, ParentNode
from utils.convert import text_node_to_html_node, text_to_text_nodes
from utils.regex import HEADING_PATTERN, CODE_PATTERN, QUOTE_PATTERN, ULIST_PATTERN, OLIST_PATTERN
from nodes.textnode import TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def get_block_type(block: str) -> BlockType:    
    if HEADING_PATTERN.fullmatch(block):
        return BlockType.HEADING
    elif CODE_PATTERN.fullmatch(block):
        return BlockType.CODE
    elif QUOTE_PATTERN.fullmatch(block):
        return BlockType.QUOTE
    elif ULIST_PATTERN.fullmatch(block):
        return BlockType.UNORDERED_LIST
    elif OLIST_PATTERN.fullmatch(block):
        lines = block.split('\n')
        for i, line in enumerate(lines):
            number = int(line.split('.')[0])
            if number != i + 1:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
    
def markdown_to_blocks(markdown: str) -> list[str]:
    if type(markdown) != str:
        raise TypeError('Markdown must be a string')
    
    result: list[str] = []
    blocks = markdown.split('\n\n')
    
    for block in blocks:
        stripped = block.strip()
        if stripped != '':
            result.append(stripped)
        
    return result

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_nodes = []
    
    for block in blocks:
        block_type = get_block_type(block)
        match block_type:
            case BlockType.HEADING:
                html_nodes.append(LeafNode('h1', block))
            case BlockType.CODE:
                lines = block.split('\n')
                inner_text = '\n'.join(lines[1:-1]) + '\n'
                html_nodes.append(ParentNode('pre', [LeafNode('code', inner_text)]))
            case BlockType.QUOTE:
                html_nodes.append(LeafNode('blockquote', block))
            case BlockType.UNORDERED_LIST:
                html_nodes.append(ParentNode('ul', [LeafNode('li', block)]))
            case BlockType.ORDERED_LIST:
                html_nodes.append(ParentNode('ol', [LeafNode('li', block)]))
            case BlockType.PARAGRAPH:
                noramlized = ' '.join(block.split('\n'))
                text_nodes = text_to_text_nodes(noramlized)
                child_nodes = []
                for text_node in text_nodes:
                    child_node = text_node_to_html_node(text_node)
                    child_nodes.append(child_node)
                html_nodes.append(ParentNode('p', child_nodes))
                
    return ParentNode('div', html_nodes)