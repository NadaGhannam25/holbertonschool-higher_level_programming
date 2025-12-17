#!/usr/bin/env python3


class CountedIterator:
    """Iterator that counts how many items were iterated"""

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        item = next(self.iterator)   # قد يرفع StopIteration (نتركه)
        self.count += 1
        return item

    def get_count(self):
        return self.count

