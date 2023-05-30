class node:
    def __init__(self, count, symbol, lchild=None, rchild=None):
        self.symbol = symbol
        self.count = count
        self.lchild = lchild
        self.rchild = rchild
        self.code = ''

class HuffmanCoding:
    def __init__(self):
        self.freq = {}
        self.codes = {}
        self.reverse_mapping = {}
        self.root = None

    def make_frequency_dict(self, text):
        for character in text:
            if character in self.freq:
                self.freq[character] += 1
            else:
                self.freq[character] = 1

    def updateCodes(self, head, c):
        if head.lchild.symbol != None:
            hold = head.lchild.code
            head.lchild.code = c + hold
        else:
            self.updateCodes(head.lchild, c)
        if head.rchild.symbol != None:
            hold = head.rchild.code
            head.rchild.code = c + hold
        else:
            self.updateCodes(head.rchild, c)
        return

    def build_huffman_tree(self):
        nodes = []
        for key in self.freq:
            nodes.append(node(self.freq[key], key))

        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.count, reverse=True)

            

            right_node = nodes.pop()
            print(right_node.symbol)
            left_node = nodes.pop()
            print(left_node.symbol)
            if left_node.lchild != None and left_node.rchild != None:
                self.updateCodes(left_node, "0")
            else:
                left_node.code = '0'
            if right_node.lchild != None and right_node.rchild != None:
                self.updateCodes(right_node, "1")
            else:
                right_node.code = '1'


            new_node = node(left_node.count + right_node.count, None, left_node, right_node)

            nodes.append(new_node)

        self.root = nodes[0]

    def make_codes_dict(self):
        def traverse(node):
            if node.symbol is not None:
                self.codes[node.symbol] = node.code
                self.reverse_mapping[node.code] = node.symbol
                return

            traverse(node.lchild)
            traverse(node.rchild)

        traverse(self.root)

    def encode(self, text):
        encoded_text = ""
        self.make_frequency_dict(text)
        self.build_huffman_tree()
        self.make_codes_dict()
        for character in text:
            encoded_text += self.codes[character]
        print(self.codes)
        print(encoded_text)
        return encoded_text

    def decode(self, encoded_text):
        current_code = ""
        decoded_text = ""
        print(self.reverse_mapping)
        for bit in encoded_text:
            current_code += bit
            if current_code in self.reverse_mapping:
                decoded_text += self.reverse_mapping[current_code]
                current_code = ""

        return decoded_text

if __name__ == "__main__":
    h = HuffmanCoding()
    text = "football"
    h.encode(text)
    print(h.decode(h.encode(text)))
    