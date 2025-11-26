from enum import Enum
import re
from utils.regex import HEADING_PATTERN, CODE_PATTERN, QUOTE_PATTERN, ULIST_PATTERN, OLIST_PATTERN

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    
def markdown_to_blocks(markdown: str) -> list[str]:
    if type(markdown) != str:
        raise TypeError('Markdown must be a string')
    
    result: list[str] = []
    blocks = markdown.split('\n\n')
    
    for block in blocks:
        stripped = block.strip()
        result.append(stripped)
        
    return result

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