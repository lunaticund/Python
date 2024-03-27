import heapq
import string
import numpy as np

class Huff_Node:
    def __init__(self,name,freq):
        self.name=name
        self.freq=freq 
        self.left=None
        self.right=None 

    def __lt__(self, other):
        return self.freq < other.freq

#构造编码
Codes={}
def Encoding(Node,code=''):
    if Node.left==None:
        Codes[Node.name]=code
        return 
    Encoding(Node.left,code+'0')
    Encoding(Node.right,code+'1')

frequency={
    'A': 0.082, 'B': 0.015, 'C': 0.028, 'D': 0.043, 
    'E': 0.127, 'F': 0.022, 'G': 0.02, 'H': 0.061, 
    'I': 0.07, 'J': 0.0015, 'K': 0.0077, 'L': 0.04, 
    'M': 0.024, 'N': 0.067, 'O': 0.075, 'P': 0.019, 
    'Q': 0.00095, 'R': 0.06, 'S': 0.063, 'T': 0.091, 
    'U': 0.028, 'V': 0.0098, 'W': 0.024, 'X': 0.0015, 
    'Y': 0.02, 'Z': 0.00074
}
#计算修正后的频率
s_fre=sum(frequency.values())+1.5*0.127
for letter in string.ascii_uppercase:
    frequency[letter]=frequency[letter]/s_fre
frequency[' ']=frequency['E']*1.5

#构建Huffman树
Huff_heap=[Huff_Node(name,freq) for name,freq in frequency.items()]
heapq.heapify(Huff_heap)

while True:
    if len(Huff_heap)==1:
        root=New_node
        break
    left=heapq.heappop(Huff_heap)
    right=heapq.heappop(Huff_heap)
    # print(left.name,end=' ')
    # print(right.name)
    New_node=Huff_Node(left.name+right.name,left.freq+right.freq)
    New_node.left=left
    New_node.right=right
    heapq.heappush(Huff_heap,New_node)

Encoding(root)
print('Char  Frequency\tCodes')
for c,f in frequency.items():
    f=round(f*100,2)
    print(f'\'{c}\':\t{f}%\t{Codes[c]}')

#计算Shannon熵
Shannon_entropy=sum([-x*np.log2(x) for x in frequency.values()])
print(f'Shannon Entropy: {Shannon_entropy:.3f}')

#计算平均比特数
bits_aver=0
for x in string.ascii_uppercase:
    bits_aver=bits_aver+len(Codes[x])*frequency[x]
bits_aver=bits_aver+len(Codes[' '])*frequency[' ']
print(f'Average Bits: {bits_aver:.3f}')

#Huffman编码
f_date=open('Original_text.txt','r')
text=f_date.read()
f_encode=open('Encodes.txt','w+')
codes_digit={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}

for c in text:
    if (c in string.ascii_letters) or c==' ':
        c=c.upper()
        f_encode.write(Codes[c])
    elif c in string.digits:
        f_encode.write(codes_digit[c])
    else:
        f_encode.write(c)
        
f_date.close()

#Huffman解码
f_encode.seek(0,0)
code_text=f_encode.read()
f_encode.close()
f_decode=open('Decode.txt','w')

Recodes={k:c for c,k in Codes.items()}
Recodes_digit={k:c for c,k in codes_digit.items()}
# print(Recodes)
code_i=''
for x in code_text:
    if x in '01':
        code_i=code_i+x
        if code_i in Recodes.keys():
            f_decode.write(Recodes[code_i].lower())
            code_i=''
    elif x in string.ascii_lowercase:
        f_decode.write(Recodes_digit[x])
        code_i=''
    else:
        f_decode.write(x)
        code_i=''

f_decode.close()