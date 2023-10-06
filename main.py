from typing import Dict, Optional


class DataCapture:
    def __init__(self):
        self.freq_map: Dict[int, int] = {}

    def add(self, value: int) -> None:
        self.freq_map[value] = self.freq_map.get(value, 0) + 1

    def build_stats(self) -> 'Stats':
        return Stats(self.freq_map)


class Stats:
    def __init__(self, freq_map: Dict[int, int]):
        self.freq_sum: Dict[int, Dict[str, int]] = {}
        self.previous: Optional[int] = None
        total = 0

        # Counting Sort to get the sorted keys in O(n)
        max_val = max(freq_map.keys())
        count = [0] * (max_val + 1)
        for key in freq_map.keys():
            count[key] += 1

        sorted_keys = []
        for i, c in enumerate(count):
            sorted_keys.extend([i] * c)

        for num in sorted_keys:
            total += freq_map[num]
            self.freq_sum[num] = {"previous": self.previous, "sum": total}
            self.previous = num

    def less(self, value: int) -> int:
        if value not in self.freq_sum:
            raise ValueError
        if self.freq_sum[value]["previous"] is None:
            return 0
        return self.freq_sum[self.freq_sum[value]["previous"]]["sum"]

    def greater(self, value: int) -> int:
        if value not in self.freq_sum:
            raise ValueError
        return self.freq_sum[self.previous]["sum"] - self.freq_sum[value]["sum"]

    def between(self, lo: int, hi: int) -> int:
        if hi not in self.freq_sum:
            raise ValueError
        return self.freq_sum[hi]["sum"] - self.less(lo)


# Example usage:
if __name__ == '__main__':
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.less(4))  # Outputs: 2
    print(stats.between(3, 6))  # Outputs: 4
    print(stats.greater(4))  # Outputs: 2
