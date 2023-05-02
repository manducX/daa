# Define the functions for small, divide, solution, and combine based on the specific problem you are trying to solve
def small(n):
    if len(n) <= 1:
        return True
    else:
        return False
def divide(n):
    mid = len(n) // 2
    n1 = n[:mid]
    n2 = n[mid:]
    return n1, n2

def solution(n):
    return n[0]

def combine(solution1, solution2):
    return max(solution1, solution2)
def divide_and_conquer(n):
    if small(n):
        return solution(n)
    else:
        n1, n2 = divide(n)
        solution1 = divide_and_conquer(n1)
        solution2 = divide_and_conquer(n2)
        return combine(solution1, solution2)

n = input("Enter Numbers: ").split()
result = divide_and_conquer(n)
print("The maximum element is:", result)
