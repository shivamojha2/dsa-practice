# Patterns

## Big-O Refresher (runtime intuition)

- O(1): constant. Hash lookups (dict, set) are basically this.
- O(log n): binary search, balanced BSTs, heap push/pop.
- O(n): scanning once through an array/string.
- O(n log n): sorting, divide & conquer (merge sort, quicksort avg).
- O(n²): double loop (pairs, brute force subarrays).
- O(2ⁿ): recursion that tries all subsets, exponential.

👉 Rule of thumb for interviews:

- If n ≤ 10⁴–10⁵, you usually want O(n) or O(n log n).
- If n ≤ 10², O(n²) might be fine.

## Core Data Structures to Keep in Mind

- Array / List: index access = O(1), insert/delete in middle = O(n).
- Hash Map (dict): insert, lookup, delete ≈ O(1).
- Hash Set (set): membership check O(1).
- Stack / Queue: push/pop = O(1). Useful for recursion, BFS/DFS.
- Heap (priority queue): push/pop O(log n). Great for “k smallest/largest” or scheduling.
- Linked list / tree: less used in Python interviews, but understand traversal.

## Quick Python templates:

### Two pointers (sorted/partition problems):

```python
i, j = 0, len(a)-1
while i < j:
    # move i or j based on condition
    ...
```

### Sliding window (subarrays/strings):

```python
from collections import Counter
need, window = Counter(...), Counter()
left = formed = 0
for right, x in enumerate(s):
    window[x] += 1
    # while window valid, try shrink
    while ...:
        ...
        left += 1
```

### Binary search on answer/index:

```python
def ok(mid): ...
lo, hi = L, R
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid
    else: lo = mid + 1
```

### Graph BFS/DFS:

```python
from collections import deque, defaultdict
g = defaultdict(list)
# fill g
q, seen = deque([start]), {start}
while q:
    u = q.popleft()
    for v in g[u]:
        if v not in seen:
            seen.add(v); q.append(v)
```

### DP (memoization):

```python
from functools import lru_cache
@lru_cache(None)
def f(i, j, ...):
    if base: return ...
    res = ...
    return res
```

A couple tiny refreshers we’ll use constantly:

- Hash map get/update: cnt[x] = cnt.get(x, 0) + 1

- Big-O anchors: nested loops over n → O(n^2); scanning once with a dict/set → ~O(n) average; binary search → O(log n); heap ops → O(log n) each.
