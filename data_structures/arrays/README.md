# Arrays — the essentials

## What they are

Contiguous memory of items; random access by **index** in O(1).

```
index:  0   1   2   3   4
nums = [5,  8,  2,  7,  9]
```

**Typical ops**

* Read/write by index → **O(1)**
* Insert/delete in middle → **O(n)** (shift)
* Append at end (dynamic array) → **amortized O(1)**
* Search by value → **O(n)** unless sorted (then binary search O(log n))

Python note: `list` is a dynamic array (not linked list).

---

## Must-know patterns (with tiny visuals)

### 1) Two Pointers (same array)

Use when the array is **sorted** or when you’re shrinking/expanding from ends.

* **Pair sum in sorted array**

```
L→             ←R
[1, 2, 4, 5, 9]
sum<L → L++ ; sum>R → R--
```

* **Remove duplicates in place** (write pointer)

```
read →
write →
[1,1,2,2,3]  keep first of each run
```

### 2) Sliding Window

For **subarrays** with constraints (length, sum, distinct chars).

* **Fixed size k**: move both ends; maintain running state.
* **Variable size**: expand R, shrink L while constraint violated.

```
L →          R →
[ a  b  c  a  b  c ]
expand R; if invalid → move L right until valid again
```

### 3) Prefix Sums (and diffs)

Precompute cumulative info to answer subarray queries fast.

* **Prefix sum**: `pre[i] = sum(nums[:i])`

  * Sum of `[l, r)` = `pre[r] - pre[l]` → O(1)
* **Hash map on prefix**: count subarrays hitting a target:

  * For sum: track seen `pre - target`.

### 4) Hash Map / Frequency Table

Count things in O(n), handle complements, check existence.

* Two Sum (value→index)
* Anagrams (char counts)
* Majority element (Boyer–Moore is O(1) space variant)

### 5) Binary Search (on index **or** on answer)

* On **sorted arrays**: find target/bounds (lower/upper).
* On **answer space**: if checking “can we achieve X?” is monotonic, binary search the smallest X (e.g., min capacity to ship packages in D days).

```
lo ... mid ... hi    choose half by predicate(mid)
```

### 6) Monotonic Stack (next greater/smaller)

For “next greater element”, “daily temps”, “largest rectangle”:

* Keep stack **monotone**; pop while new element breaks monotonicity.

```
stack holds indices with decreasing heights
```

### 7) Sorting + Greedy / Sweep

Sort then make one linear pass.

* Merge intervals, meeting rooms, activity selection.

### 8) Kadane’s (max subarray sum)

Track `best_end_here`, `best_so_far` in O(n).

---

## Complexity cheatsheet

* Index read/write: **O(1)**
* Insert/delete at i: **O(n)**
* Scan: **O(n)**
* Sort: **O(n log n)**
* Binary search: **O(log n)**
* Sliding window / two pointers (one pass): **O(n)**

---

## Python gotchas & tips

* Slicing makes copies: `b = a[:]` (O(n)).
* `list.insert(i,x)` / `pop(i)` are **O(n)**; `append`/`pop()` at end are amortized **O(1)**.
* Use `enumerate` to get (i, val).
* For “keep original indices” after sorting: sort **pairs** `(val, idx)`.
* `bisect_left/right` for binary search bounds.
* For top-K: `heapq.nlargest(k, data)` or manual min-heap.
* Counting: `collections.Counter` (but know how to do it manually).

---

## Mini templates (just the bones)

**Two pointers (pair sum, sorted)**

```python
L, R = 0, len(a)-1
while L < R:
    s = a[L] + a[R]
    if s == target: ...
    elif s < target: L += 1
    else: R -= 1
```

**Sliding window (variable)**

```python
need = {...}; have = {...}; formed = 0
L = 0
for R, x in enumerate(a):
    # include x
    while condition_violated:
        # exclude a[L]
        L += 1
    # update best using [L, R]
```

**Prefix sum with hashmap (subarray sum = k)**

```python
seen = {0: 1}
pre = 0
count = 0
for x in nums:
    pre += x
    count += seen.get(pre - k, 0)
    seen[pre] = seen.get(pre, 0) + 1
```

**Binary search (leftmost true)**

```python
lo, hi = 0, N
while lo < hi:
    mid = (lo + hi)//2
    if ok(mid): hi = mid
    else: lo = mid + 1
# lo is first index with ok==True
```

**Monotonic stack (next greater element)**

```python
res = [-1]*len(nums)
st = []  # indices, stack of decreasing values
for i, x in enumerate(nums):
    while st and nums[st[-1]] < x:
        j = st.pop()
        res[j] = x
    st.append(i)
```

**Kadane**

```python
best_end = best = nums[0]
for x in nums[1:]:
    best_end = max(x, best_end + x)
    best = max(best, best_end)
```

---

## How to pick a pattern (fast)

1. **Subarray / substring constraints?** → Sliding window / prefix sum.
2. **Sorted or can sort?** → Two pointers / binary search / greedy.
3. **Counts, existence, complements?** → Hash map.
4. **Next greater/smaller, ranges, histograms?** → Monotonic stack.
5. **Max/min value under monotone feasibility?** → Binary search on answer.

---

## Pitfalls

* Using nested loops when a map or window works in O(n).
* Forgetting to shrink window (infinite loops).
* Off-by-one in binary search bounds (test edges!).
* Not carrying original indices after sorting.
* Extra O(n) copies via slices unintentionally.

---

## Quick practice prompts (mental reps)

1. “Longest subarray with sum = k” → which pattern?
2. “Two numbers sum to target (array sorted)” → which pattern?
3. “Find first index ≥ x in sorted array” → which function / pattern?
4. “Daily Temperatures” → which pattern?

---