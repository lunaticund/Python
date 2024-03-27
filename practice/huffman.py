import heapq
from collections import defaultdict

# 定义节点类
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

# 构建Huffman树
def build_huffman_tree(data):
    frequency = defaultdict(int)
    for char in data:
        frequency[char] += 1

    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

# 生成Huffman编码表
def build_huffman_code_table(root):
    code_table = {}

    def generate_code(node, current_code):
        if node.char:
            code_table[node.char] = current_code
        else:
            generate_code(node.left, current_code + '0')
            generate_code(node.right, current_code + '1')

    generate_code(root, '')
    return code_table

# 将文本编码为Huffman编码
def encode_text(text, code_table):
    encoded_text = ''
    for char in text:
        encoded_text += code_table[char]
    return encoded_text

# 将Huffman编码解码为文本
def decode_text(encoded_text, root):
    decoded_text = ''
    current_node = root
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char:
            decoded_text += current_node.char
            current_node = root

    return decoded_text

# 示例
data = 'China is ready to work with the Commonwealth of Dominica to better align the two countries\' development strategies and transform their friendship into the driving force of win-win cooperation, in order to benefit their peoples with greater achievements, President Xi Jinping said on Monday.In a meeting with visiting Prime Minister of Dominica Roosevelt Skerrit in Beijing, Xi said that China and the Caribbean nation have set a fine example of South-South cooperation since they established diplomatic relations in 2004, which Skerrit said was a correct decision made by him after severing "diplomatic ties" with Taiwan.Xi noted that the key to the smooth development of bilateral relations lies in the high-level political mutual trust between the two countries, as well as the mutual understanding and support on issues concerning each other\'s core interests and major concerns.As China advances its modernization at full throttle, Dominica is welcome to board the fast train and expand cooperation with China in fields such as trade and economy, infrastructure construction, agriculture and healthcare, Xi said.In 2018, China and Dominica signed a memorandum of understanding on Belt and Road cooperation. Last year, the two-way trade between the countries exceeded $73.5 million, a year-on-year growth of 111.5 percent, according to statistics from China Customs.Xi said that China welcomes more young students from Dominica to study in the country, and will continue to provide scholarships and training opportunities for them.Emphasizing that China upholds the belief that all countries, regardless of their size or strength, are equal members of the international community, Xi said that China attaches importance to the concerns and appeals of small island developing countries in the field of climate change, and supports Dominica in playing an active role in global and regional affairs.He also expressed China/s support for Caribbean countries in seeking national prosperity and development as well as in improving their public well-being.Skerrit said as a great nation, China has not only made remarkable achievements in areas such as poverty alleviation and its overall development, but has also made important contributions to peace and development in Caribbean countries and across the world.He reiterated his countrys adherence to the one-China principle, saying that Dominica supports China\'s just cause of realizing complete reunification and opposes any external interference in China\'s internal affairs.'
root = build_huffman_tree(data)
code_table = build_huffman_code_table(root)

encoded_text = encode_text(data, code_table)
decoded_text = decode_text(encoded_text, root)

# print(f'fOriginal text: {data}')
print(f'fEncoded text: {encoded_text}')
# print(f'fDecoded text: {decoded_text}')
