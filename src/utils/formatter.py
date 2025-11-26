from nodes.textnode import TextNode, TextType
from utils.regex import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            if delimiter not in node.text:
                new_nodes.append(node)
                continue
            
            parts = node.text.split(delimiter)
            if len(parts) < 3:
                print(f'parts: {parts}')
                raise Exception('Invalid text split result. Ensure valid markdown syntax is used for code, bold, or italic text')
            new_nodes.extend([
                TextNode(f"{parts[0]}", TextType.TEXT),
                TextNode(f"{parts[1]}", text_type),
                TextNode(f"{parts[2]}", TextType.TEXT)
            ])
        else:
            new_nodes.append(node)
    
    return new_nodes

def split_nodes_image(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        images = extract_markdown_images(text)
            
        if not images:
            new_nodes.extend([node])
            continue
        
        for alt, link in images:
            markdown = f"![{alt}]({link})"
            
            before, after = text.split(markdown, 1)
            
            if before:
                new_nodes.extend([
                    TextNode(before, TextType.TEXT)
                ])
                
            new_nodes.extend([
                TextNode(alt, TextType.IMAGE, link)
            ])
            
            text = after
            
        if text:
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )

    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]):
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
        text = node.text
        links = extract_markdown_links(text)
        
        if not links:
            new_nodes.append(node)
            continue
        
        for text_content, url in links:
            markdown = f"[{text_content}]({url})"
            
            before, after = text.split(markdown, 1)
            
            if before:
                new_nodes.extend([
                    TextNode(before, TextType.TEXT)
                ])
                
            new_nodes.extend([
                TextNode(text_content, TextType.LINK, url)
            ])
            
            text = after
            
        if text:
            new_nodes.append(
                TextNode(text, TextType.TEXT)
            )

    return new_nodes