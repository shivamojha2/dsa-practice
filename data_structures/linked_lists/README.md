# Linked Lists

## What they are

A chain of nodes, each pointing to the next (and sometimes the previous).

* **Singly:** `value | next →`
* **Doubly:** `← prev | value | next →`

Why they exist: constant-time inserts/removals when you already have the node (no shifting like arrays).

---

## Visuals: how the pointers move

### Insert right after `HEAD` (DLL)

Before -
`HEAD <-> A <-> ... <-> TAIL`

Insert `X` **after** `HEAD` -
`HEAD <-> X <-> A <-> ... <-> TAIL`

Pointers (4 updates):

1. `X.prev = HEAD`
2. `X.next = HEAD.next`
3. `HEAD.next.prev = X`
4. `HEAD.next = X`

### Remove a node `X` in the middle (DLL)

Before
`... <-> P <-> X <-> N <-> ...`

After
`... <-> P <-> N <-> ...`

Pointers (4 updates):

1. `P.next = N`
2. `N.prev = P`
   (Optionally clear `X.prev = X.next = None`)

### Why “dummy” (sentinel) nodes?

Keep permanent `HEAD` and `TAIL` sentinels so you don’t write special cases for empty/1-node lists:
`HEAD <-> (real nodes...) <-> TAIL`

---

## Complexity (typical)

* Access by index: **O(n)**
* Insert/remove when you already have the node (or its predecessor in SLL): **O(1)**
* Search by value: **O(n)**
* Space: **O(n)**

---

## Pattern toolbox (with quick visuals)

### 1) Reverse a singly list

Idea: iterative pointer flip `prev, curr = None, head`.

```
None <- A <- B <- C    D -> ...
          ↑curr  ↑prev
```

Loop: save `next`, set `curr.next = prev`, advance both.

### 2) Find middle (slow/fast pointers)

* `slow` moves 1 step; `fast` moves 2.
* When `fast` hits end, `slow` is at middle.

### 3) Detect cycle (Floyd’s tortoise–hare)

* Move `slow` by 1, `fast` by 2; if they ever meet → cycle.
* To find entry: reset one pointer to head; move both 1 step until they meet.

### 4) Remove N-th from end (one pass)

* Two pointers: advance `fast` **N** steps, then move both until `fast` hits end; remove `slow.next`.
* Use a **dummy head** to handle removing the first node.

### 5) Merge two sorted lists (like merge step in mergesort)

* Build a new chain by always taking the smaller head from the two lists.

### 6) LRU cache (what you just built)

* **Hash map:** `key → node`
* **DLL:** Most recent at head, least recent before tail
* `get/put` move the node to head; evict from tail.

---

## When to pick a linked list (vs array/list)

Choose a linked list when you:

* Do tons of inserts/removals in the middle given a pointer to the spot.
* Need a stable O(1) queue/deque with predictable pointer ops.

Prefer array/list when you:

* Need random access by index or tight cache locality / vectorized ops.

---

## Pitfalls to watch

* Forgetting one of the 4 pointer updates (causes cycles or breaks the chain).
* Not using a sentinel, leading to edge-case bugs on empty/length-1 lists.
* In SLL deletions, you **must** know the predecessor (or use “copy next into current” trick if allowed).

---

## Minimal Python templates

Singly node:

```python
class SNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
```

Reverse SLL:

```python
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev, curr = curr, nxt
    return prev
```

Doubly with sentinels (core helpers):

```python
class DNode:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DList:
    def __init__(self):
        self.head, self.tail = DNode(), DNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_after_head(self, x):
        x.prev = self.head
        x.next = self.head.next
        self.head.next.prev = x
        self.head.next = x

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev
```

---

## Quick practice (try mentally, then code)

1. Reverse a list: `1→2→3→4→None` → ?
2. Given `1→2→3→4→5`, remove 2nd from end → ?
3. Two sorted lists `1→4→7` and `2→3→6→8` → merged result?
