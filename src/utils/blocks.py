from enum import Enum
import re

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
    heading_pattern = re.compile(r"^#{1,6} .+$")
    code_pattern = re.compile(f"^```[\s\S]*```$", re.DOTALL)
    quote_pattern = re.compile(f"^(>.*)(\n>.*)*$")
    ulist_pattern = re.compile(r"^- .+(?:\n- .+)*$")
    olist_pattern = re.compile(r"^\d+\. .+(?:\n\d+\. .+)*$")
    
    if heading_pattern.fullmatch(block):
        return BlockType.HEADING
    elif code_pattern.fullmatch(block):
        return BlockType.CODE
    elif quote_pattern.fullmatch(block):
        return BlockType.QUOTE
    elif ulist_pattern.fullmatch(block):
        return BlockType.UNORDERED_LIST
    elif olist_pattern.fullmatch(block):
        lines = block.split('\n')
        for i, line in enumerate(lines):
            number = int(line.split('.')[0])
            if number != i + 1:
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH