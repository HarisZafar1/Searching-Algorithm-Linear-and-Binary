class Search:
    def __init__(self, lst, target):
        self.lst = lst
        self.target = target

    def linear_search(self):
        for value in self.lst:
            if value == self.target:
                return value  # Target found, return its value
        return None  # Target not found

    def binary_search(self):
        left, right = 0, len(self.lst) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.lst[mid] == self.target:
                return self.lst[mid]  # Target found, return its value
            elif self.lst[mid] < self.target:
                left = mid + 1
            else:
                right = mid - 1
        return None  # Target not found

# Example usage
lst = [15, 3, 7, 1, 13, 9, 11, 5]  # Unsorted list for linear search
slst = [1, 3, 5, 7, 9, 11, 13, 15]  # Sorted list for binary search

# General Linear Search
obj = Search(lst, 7)
print("\nLinear Search:")
print(f"General Case (target=7): Value {obj.linear_search()}")  # General case

# Best and Worst Cases for Linear Search
obj = Search(lst, 15)
print(f"Best Case (target=15):  {obj.linear_search()}")

obj = Search(lst, 1)
print(f"Worst Case (target=1): {obj.linear_search()}")

# General Binary Search
obj = Search(slst, 7)
print("\nBinary Search:")
print(f"General Case (target=7): {obj.binary_search()}")  # General case

# Best and Worst Cases for Binary Search
obj = Search(slst, 9)
print(f"Best Case (target=9): {obj.binary_search()}")  # Best case: middle element

obj = Search(slst, 15)
print(f"Worst Case (target=15):  {obj.binary_search()}")  # Worst case: last element after full search
