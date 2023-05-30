class MaxHeap:
  def __init__(self, ls=None):
    self.heap = None
    if ls != None:
        for i in ls:
            self.insert(i)
  
  def heapify(self, index):
    if self.heap == None:
      return None
    
    left = (index*2)+1
    right = (index*2)+2
    lengthOfHeap = len(self.heap)

    if left >= lengthOfHeap and right >= lengthOfHeap:
      return
    if right >= lengthOfHeap:
      if self.heap[left] >= self.heap[index]:
        hold = self.heap[index]
        self.heap[index] = self.heap[left]
        self.heap[left]=hold
        self.heapify((index-1)//2)
        return
      else:
        return

    if self.heap[index] >= max(self.heap[left], self.heap[right]):
      return
    else:
      if self.heap[left] >= self.heap[right]:
        hold = self.heap[index]
        self.heap[index] = self.heap[left]
        self.heap[left]=hold
        if index != 0:
            self.heapify((index-1)//2)
      else:
        hold = self.heap[index]
        self.heap[index] = self.heap[right]
        self.heap[right]=hold
        if index != 0:
            self.heapify((index-1)//2)
    return
  
    
  def insert(self, element):
    if self.heap == None:
      self.heap = [element]
    else:
      nextIndex = len(self.heap)
      self.heap.append(element)
      self.heapify((nextIndex-1)//2)
    return None
  


  def getMax(self):
    if self.heap == None:
      return None
    hold = self.heap[0]
    self.heap[0] = self.heap[len(self.heap)-1]
    self.heap.pop()
    if self.heap == []:
      self.heap = None
    self.heapify(0)
    return hold
    

  def print(self):
    return self.heap

def test_max_heap(input):
  mx = None
  result = []
  i = 0
  while i < len(input):
    if input[i] == 'MaxHeap':
      mx = MaxHeap(input[i+1])
      result.append(None)
      i += 2
    elif input[i] == 'insert':
      result.append(mx.insert(input[i+1]))
      i += 2
    elif input[i] == 'getMax':
      result.append(mx.getMax())
      i += 1
    elif input[i] == 'print':
      res = mx.print()
      if res == None:
         result.append([])
      else:
        result.append(res[:])
      i += 1
    else:
      i += 1
  return result 



class minHeap:
    def __init__(self, ls=None):
        self.heap = None
        if ls != None:
            for key, value in ls.items():
                self.insert(key, value)
    
    def insert(self, key, value):
       n = node(count=value, symbol=key)
       if self.heap == None:
          self.heap = [n]
       else:
            nextIndex = len(self.heap)
            self.heap.append(n)
            self.heapify(nextIndex)

    def heapify(self, index):
        if self.heap == None:
            return None
        
        parent = (index-1)//2
        if parent < 0:
           return

        if self.heap[index].count <= self.heap[parent].count:
           hold = self.heap[parent]
           self.heap[parent] = self.heap[index]
           self.heap[index] = hold
           #self.print()
           self.heapify(parent)
        
        
    def print(self):
        s = []
        for n in self.heap:
           s.append(n.count)
        print(s)
           
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
            if right_node.lchild != None and right_node.rchild != None:
                print("TrueA")
                self.updateCodes(right_node, "0")
            else:
                print("falseA")
                right_node.code = '0'
            if left_node.lchild != None and left_node.rchild != None:
                print("TrueB")
                self.updateCodes(left_node, "1")
            else:
                print("falseB")
                left_node.code = '1'


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

    def encode(self, s):
        encoded_text = ""
        self.make_frequency_dict(s)
        self.build_huffman_tree()
        self.make_codes_dict()
        for character in s:
            encoded_text += self.codes[character]
        return encoded_text, self.codes

    def decode(self, s, d):
        current_code = ""
        decoded_text = ""
        dc = {value:key for key, value in d.items()}
        for bit in s:
            current_code += bit
            if current_code in dc:
                decoded_text += dc[current_code]
                current_code = ""

        return decoded_text





if __name__ == "__main__":
    #print("Heap Test")
    input = ["MaxHeap",[],"insert",10,"insert",20,"insert",30,"print"]
    print(test_max_heap(input)) # [None, [4, 3, 2], None, None, None, None, 7, None, [8, 4, 6, 1, 3, 2, 5]]
    #input = 'aabc'
    #print(hc.encode(input)) # ('001011', {'a': '0', 'b': '10', 'c': '11'})
    hc = HuffmanCoding()
    input = 'aabc'
    print(hc.encode(input)) # ('001011', {'a': '0', 'b': '10', 'c': '11'})

    input = 'football'
    print(hc.encode(input)) # ('01010100111101110000', {'l': '00', 'f': '010', 't': '011', 'o': '10', 'b': '110', 'a': '111'})
        
    #input = "AAAABBBCC"
    #print(hc.encode(input))
    #d = {'a':2, 'b':3, 'c':4}
    #m = minHeap(d)
   #print(m.print())
