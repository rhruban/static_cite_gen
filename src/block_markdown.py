from enum import Enum

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
