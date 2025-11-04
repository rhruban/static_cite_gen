



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
