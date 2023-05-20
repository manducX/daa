import heapq

def optimal_merge_pattern():
    files = []
    n = int(input("Enter the number of files: "))
    for i in range(n):
        file_size = int(input(f"Enter the size of file {i+1}: "))
        files.append(file_size)

    heap = []
    for file in files:
        heapq.heappush(heap, file)

    total_cost = 0
    while len(heap) > 1:
        smallest_file = heapq.heappop(heap)
        next_smallest_file = heapq.heappop(heap)
        merge_cost = smallest_file + next_smallest_file
        total_cost += merge_cost
        heapq.heappush(heap, merge_cost)

    return total_cost
total_merge_cost = optimal_merge_pattern()
print(total_merge_cost)  # Output: the total merge cost for the given files
