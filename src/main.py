from textnode import TextNode, TextType

def main():
    nody = TextNode("There is some anchor text", TextType.LINK, 'https://www.boot.dev')

    print(nody)


if __name__ == "__main__":
    main()
