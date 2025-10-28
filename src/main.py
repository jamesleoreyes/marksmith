from textnode import TextNode, TextType

def main():
    node = TextNode('this is text', TextType.PLAIN, 'https://boot.dev')
    print(node)
    
main()