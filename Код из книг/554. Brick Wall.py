from collections import defaultdict
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edges, maxEdges = defaultdict(int), 0
        for row in wall:
            for idx in accumulate(row[:-1]):
                edges[idx] += 1
                maxEdges = max(maxEdges, edges[idx])
        return len(wall) - maxEdges