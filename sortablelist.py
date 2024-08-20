class SortableList:
    def __init__(self, original_list):
        self.array = list(original_list)

    def swap(self, i, j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def __min__(self):
        minval = self.array[0]
        for i in range(len(self.array)):
            x = self.array[i]
            if minval > x:
                minval = x
        return minval

    def __max__(self):
        maxval = self.array[0]
        for i in range(len(self.array)):
            x = self.array[i]
            if maxval < x:
                maxval = x
        return maxval

    def __sum__(self):
            val = 0
            for i in range(len(self.array)): 
                val = self.array[i] + val
            return val


    def linear_search(self, value):
        i = 0
        while i < len(self.array):
            if self.array[i] == value:
                return i
            else:
                i = i + 1
        return None

    def binary_search(self, value):
        assert self.array == sorted(self.array)
        smallest = 0
        largest = len(self.array) - 1
        middle = (largest+smallest) // 2#round down to whole number

        while largest>=smallest:
            if self.array[middle]==value:
                return middle
            if self.array[middle]>value:
                largest = middle - 1
            else :
                smallest = middle + 1
            middle = (largest+smallest) // 2 
        return None

    def bogo_sort(self):
        import random
        while self.array!=sorted(self.array):
            random.shuffle(self.array)
        return 

    def bubble_sort(self):
        # TODO: bubble sort self.array
        num_swaps = 1
        while num_swaps > 0:
            num_swaps = 0
            for i in range(0, len(self.array) - 1):
                if self.array[i]>self.array[i + 1]:
                    self.swap(i, i + 1)
                    num_swaps = num_swaps + 1
        return self.array 

    def selection_sort(self):
        num_sorted = 0
        while num_sorted < len(self.array):
            index_smallest = num_sorted
            for i in range(num_sorted, len(self.array)):
                if self.array[i]<self.array[index_smallest]:
                    index_smallest = i
            
            self.swap(index_smallest, num_sorted)
            num_sorted += 1
        return

    def insertion_sort(self):
        # TODO: insertion sort self.array
        return

    def quick_sort(self):
        def quick_sort_rec(i_first, i_last):
            if i_first < i_last - 1:
                front = i_first + 1
                back = i_last
                i = front
                while i < back:
                    if self.array[i] <= self.array[i_first]:
                        i += 1
                    else:
                        back -= 1
                        self.swap(i, back)
                self.swap(i_first, i-1)
                quick_sort_rec(i_first, i-1)
                quick_sort_rec(i, i_last)
            return
        quick_sort_rec(0, len(self.array))
        return

    def merge_sort(self):
        temp_array = self.array.copy() # in-place merge sort too hard 😔
        def merge_rec(i_first, i_last):
            if i_first < i_last - 1:
                i_mid = (i_first + i_last) // 2
                merge_rec(i_first, i_mid)
                merge_rec(i_mid, i_last)
                i = i_first
                j = i_mid
                front = i_first
                while i < i_mid and j < i_last:
                    if self.array[i] <= self.array[j]:
                        temp_array[front] = self.array[i]
                        i += 1
                    else:
                        temp_array[front] = self.array[j]
                        j += 1
                    front += 1
                while i < i_mid:
                    temp_array[front] = self.array[i]
                    i += 1
                    front += 1
                while j < i_last:
                    temp_array[front] = self.array[j]
                    j += 1
                    front += 1
                for i in range(i_first, i_last):
                    self.array[i] = temp_array[i]
        merge_rec(0, len(self.array))
        del temp_array
        return

    def python_default_sort(self):
        self.array.sort()

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return f'SortableList<{self.array}>'


# Testing the class
if __name__ == "__main__":
    mode = "TIMING"
    
    if mode == "TESTING":
        example_list = [35, 65, 92, 15, 14, 3, 35, 65, 92, 15, 14, 3]
        print(f'Original list:\n\t{example_list}')

        a = SortableList(example_list)
        a.bubble_sort()
        print(f'Bubble sort:\n\t{a}')

        b = SortableList(example_list)
        b.selection_sort()
        print(f'Selection sort:\n\t{b}')

        c = SortableList(example_list)
        c.insertion_sort()
        print(f'Insertion sort:\n\t{c}')

        d = SortableList(example_list)
        d.quick_sort()
        print(f'Quick sort:\n\t{d}')

        e = SortableList(example_list)
        e.merge_sort()
        print(f'Merge sort:\n\t{e}')

        f = SortableList(example_list)
        f.python_default_sort()
        print(f'Python default sort:\n\t{f}')
        
    elif mode == "TIMING":
        import random
        import time
        BIG_NUM = 5000 # five thousand
        example_list = [random.randint(1, BIG_NUM) for _ in range(BIG_NUM)]

        def measure_time(func):
            start_time = time.time()
            func()
            end_time = time.time()
            return round(end_time - start_time, 4)

        a = SortableList(example_list)
        print(f'Bubble sort: {measure_time(a.bubble_sort)}')

        b = SortableList(example_list)
        print(f'Selection sort: {measure_time(b.selection_sort)}')

        c = SortableList(example_list)
        print(f'Insertion sort: {measure_time(c.insertion_sort)}')

        d = SortableList(example_list)
        print(f'Quick sort: {measure_time(d.quick_sort)}')

        e = SortableList(example_list)
        print(f'Merge sort: {measure_time(e.merge_sort)}')

        f = SortableList(example_list)
        print(f'Python default sort: {measure_time(f.python_default_sort)}')
        
    elif mode == "EXTRA_TIMING":
        import random
        import time
        BIG_NUM = 1000000 # a million
        example_list = [random.randint(1, BIG_NUM) for _ in range(BIG_NUM)]

        def measure_time(func):
            start_time = time.time()
            func()
            end_time = time.time()
            return round(end_time - start_time, 4)

        d = SortableList(example_list)
        print(f'Quick sort: {measure_time(d.quick_sort)}')

        e = SortableList(example_list)
        print(f'Merge sort: {measure_time(e.merge_sort)}')

        f = SortableList(example_list)
        print(f'Python default sort: {measure_time(f.python_default_sort)}')
