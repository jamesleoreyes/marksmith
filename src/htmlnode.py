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
        result = ' '
        
        if self.props:        
            for key, value in self.props.items():
                result += f'{key}={value} '
                
        return result
    
class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str | None,
        props: dict[str, str] = None
    ):
        self.tag = tag
        self.value = value
        self.props = props
        super().__init__(tag, value, None, props)
        
    def props_to_html(self):
        result = ''
        
        if self.props:
            for key, value in self.props.items():
                result += f' {key}="{value}"'
                
        return result
    
    def to_html(self):
        if not self.value:
            raise ValueError('Value is required')
        
        if self.tag == None:
            return self.value
        
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'