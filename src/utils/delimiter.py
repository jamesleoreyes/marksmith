from nodes.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType):
    new_nodes: list[TextNode] = []
    
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) < 3:
                raise Exception('Invalid text split result. Ensure valid markdown syntax is used for code, bold, or italic text')
            new_nodes.extend([
                TextNode(f"{parts[0]}", TextType.TEXT),
                TextNode(f"{parts[1]}", text_type),
                TextNode(f"{parts[2]}", TextType.TEXT)
            ])
        else:
            new_nodes.append(node)
    
    return new_nodes