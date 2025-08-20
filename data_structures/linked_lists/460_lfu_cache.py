"""
LRU:
dict: key → node
doubly linked list ordered MRU→LRU
get/put: move node to head; evict from tail.

LFU:
dict: key → (value, freq, pointer)
dict: freq → DLL of keys with that freq
Track min_freq
get: bump freq (remove from old freq list, add to new), update min_freq if needed
put: insert with freq=1; if full, evict from min_freq's list (LRU within that bucket)
Both achieve O(1) average per op; LFU has more bookkeeping and bigger constants.
"""