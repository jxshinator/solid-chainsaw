class DataProcessor:
    def __init__(self, items):
        self.items = items

    def filter_even(self):
        return [x for x in self.items if x % 2 == 0]

    def get_summary(self):
        return {
            'total': len(self.items),
            'evens': len(self.filter_even())
        }
