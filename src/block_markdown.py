from enum import Enum

from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node, TextNode, TextType

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    QUOTE = 'quote'
    CODE = 'code'
    ULIST = 'unordered_list'
    OLIST = 'ordered_list'


def block_to_block_type(block):
    h_flag = 0
    for char in block[0:7]:
        if char == "#":
            h_flag = 1
        elif h_flag == 1 and char == " ":
            return BlockType.HEADING
        else:
            break

    if (block[0:3] == "```") and (block[-3:] == "```"):
        return BlockType.CODE

    lines = block.split("\n")
    q_flag = 1
    u_flag = 1
    o_flag = 1
    line_num = 0

    for line in lines:
        if line[0] != ">":
            q_flag = 0
        if line[0:2] != "- ":
            u_flag = 0
        line_num += 1
        if line[0:len(str(line_num))+2] != f"{line_num}. ":
            o_flag = 0

    if q_flag == 1:
        return BlockType.QUOTE
    if u_flag == 1:
        return BlockType.ULIST
    if o_flag == 1:
        return BlockType.OLIST
    else:
        return BlockType.PARAGRAPH


def markdown_to_blocks(markdown):
    final_blocks = []
    blocks = markdown.split('\n\n')
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        else:
            final_blocks.append(block)
    return final_blocks


def paragraph_to_html_node(block):
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode('p',children)


def heading_to_html_node(block):
    count = 0
    for letter in block:
        if letter == "#":
            count += 1
        else:
            break
    text = block[count+1:]
    children = text_to_children(text)
    return ParentNode(f"h{count}",children)


def quote_to_html_node(block):
    lines = block.split("\n")
    trimmed_lines = []
    for line in lines:
        trimmed_lines.append(line.lstrip(">").strip())
    text = " ".join(trimmed_lines)
    children = text_to_children(text)
    return ParentNode("blockquote", children)


def code_to_html_node(block):
    text = block[4:-3]
    code_text_node = TextNode(text, TextType.TEXT)
    child = text_node_to_html_node(code_text_node)
    code = ParentNode("code",[child])
    return ParentNode("pre",[code])


def ulist_to_html_node(block):
    lines = block.split("\n")
    html_lines = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        html_lines.append(ParentNode("li",children))
    return ParentNode("ul",html_lines)

def olist_to_html_node(block):
    lines = block.split("\n")
    html_lines = []
    for line in lines:
        text = line.split(" ",1)
        children = text_to_children(text[1])
        html_lines.append(ParentNode("li",children))
    return ParentNode("ol",html_lines)


def text_to_children(text):
    t_nodes = text_to_textnodes(text)
    h_nodes = []
    for t_node in t_nodes:
        h_nodes.append(text_node_to_html_node(t_node))
    return h_nodes


def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block_nodes.append(paragraph_to_html_node(block))
            case BlockType.HEADING:
                block_nodes.append(heading_to_html_node(block))
            case BlockType.QUOTE:
                block_nodes.append(quote_to_html_node(block))
            case BlockType.CODE:
                block_nodes.append(code_to_html_node(block))
            case BlockType.ULIST:
                block_nodes.append(ulist_to_html_node(block))
            case BlockType.OLIST:
                block_nodes.append(olist_to_html_node(block))
    return ParentNode('div',block_nodes,None)


