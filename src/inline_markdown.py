import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            chunks = node.text.split(delimiter)
            if len(chunks) % 2 != 1:
                raise ValueError("Markdown syntax error, formatted section not closed")
            count = 0
            for chunk in chunks:
                count += 1
                if chunk == '':
                    continue
                if count % 2 == 1:
                    new_nodes.append(TextNode(chunk, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(chunk, text_type))
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_images(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        texts = old_node.text
        for image in images:
            parts = texts.split(f"![{image[0]}]({image[1]})", 1)
            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
            texts = parts[1]
        if texts != '':
            new_nodes.append(TextNode(texts, TextType.TEXT))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        images = extract_markdown_links(old_node.text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        texts = old_node.text
        for image in images:
            parts = texts.split(f"[{image[0]}]({image[1]})", 1)
            if parts[0] != '':
                new_nodes.append(TextNode(parts[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0],TextType.LINK,image[1]))
            texts = parts[1]
        if texts != '':
            new_nodes.append(TextNode(texts, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    new_nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = split_nodes_delimiter(new_nodes,'**',TextType.BOLD)
    new_nodes = split_nodes_delimiter(new_nodes,'_',TextType.ITALIC)
    new_nodes = split_nodes_delimiter(new_nodes,'`',TextType.CODE)
    new_nodes = split_nodes_image(new_nodes)
    new_nodes = split_nodes_link(new_nodes)
    return new_nodes

