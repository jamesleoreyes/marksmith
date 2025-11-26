import re

HEADING_PATTERN = re.compile(r"^#{1,6} .+$")
CODE_PATTERN = re.compile(f"^```[\s\S]*```$", re.DOTALL)
QUOTE_PATTERN = re.compile(f"^(>.*)(\n>.*)*$")
ULIST_PATTERN = re.compile(r"^- .+(?:\n- .+)*$")
OLIST_PATTERN = re.compile(r"^\d+\. .+(?:\n\d+\. .+)*$")

def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return matches

def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    
    return matches

