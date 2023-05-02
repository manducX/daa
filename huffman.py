import heapq
from collections import defaultdict

def huffman_code(text):
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    heap = [[f, [c, ""]] for c, f in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    codes = dict(heapq.heappop(heap)[1:])
    return codes

text = str(input("Enter Text :"))
codes = huffman_code(text)
print(codes)
