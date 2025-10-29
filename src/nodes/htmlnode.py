from __future__ import annotations
from typing import Optional

class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        value: Optional[str] = None,
        children: Optional[list[HTMLNode]] = None,
        props: Optional[dict[str, str]] = None
    ):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def __repr__(self):
        print(f'TAG: {self.tag}')
        print(f'VALUE: {self.value}')
        print(f'CHILDREN: {self.children}')
        print(f'PROPS: {self.props}')
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        result = ''
        
        if self.props:        
            for key, value in self.props.items():
                result += f' {key}="{value}"'
                
        return result
    
class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str | None,
        props: Optional[dict[str, str]] = None
    ):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError('Value is required')
        
        if not self.tag:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list[HTMLNode],
        props: Optional[dict[str, str]] | None = None
    ):
        self.tag = tag
        self.children = children
        self.props = props
        
    def to_html(self):
        if not self.tag:
            raise ValueError('A tag is required')
        
        if not self.children:
            raise ValueError('Children are required')
        
        children = ''
        for child in self.children:
            children += child.to_html()
        
        return f'<{self.tag}{self.props_to_html()}>{children}</{self.tag}>'