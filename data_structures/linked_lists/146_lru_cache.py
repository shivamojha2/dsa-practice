"""
LRU Cache is a data structure that stores key-value pairs and has a fixed size.
In an LRU cache, keys are unique

If the cache is full, the least recently used item is removed to make room for the new item.

**Intuition**
- We use a hashmap to store the key-value pairs, the key is the key and the value is the node.
- We use a doubly linked list to store the key-value pairs. Created class Node to represent the node.
- We use a dummy head before the real head and a dummy tail after the real tail to simplify the implementation.

The major operations needed are put and get.

Let's start with put method.
- If the key is already in the cache, we update the value and move the node to the head. (Since it becomes most recently used)
- If the key is not in the cache, we create a new node and add it to the head.
    - If the cache is full, we remove the least recently used item from the tail. (Since it is the least recently used)

Now, let's implement the get method.
- If the key is not in the cache, we return -1.
- If the key is in the cache, we move the node to the head and return the value.

To break these down into simpler steps, we can use the following helper functions. We need to add after head, remove before tail, move nodes to head when they are used, and also remove there previous position in cache.
- _add_after_head(node: Node)
- _remove_node(node: Node)
- _move_to_head(node: Node)
- _pop_tail()

**Is this optimal?**
Yes. Hash map + doubly linked list gives O(1) average for both ops. Any array/list scan would be O(n).

**Time/space complexity**
- get = O(1) avg (hash lookup + O(1) relink)
- put = O(1) avg (insert/update + optional O(1) eviction)
- Space = O(capacity) nodes + map entries (plus 2 dummies)

Q. Why doubly linked list (not singly)?
A. Need O(1) removal from the middle. Without prev, removal would require finding the predecessor (O(n)) or extra bookkeeping.

Q. Why store the key on each node?
A. In an LRU cache, keys are unique. So eviction can do del map[tail.key] in O(1) without searching.

Alternative in Python - collections.OrderedDict
"""

class Node:
    """
    Define a Node in the doubly linked list
    """
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    """
    New node → head (most recent)
    Evict node → tail (least recent)
    """

    def __init__(self, capacity: int):
        """
        Created two “dummy” nodes:
            # dummy_head (self.head) before the real head
            # dummy_tail (self.tail) after the real tail
        So the list always looks like:
        HEAD <-> nodeA <-> nodeB <-> nodeC <-> TAIL
        """
        self.capacity = capacity
        self.hm = {}
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_after_head(self, node: Node):
        # HEAD <-> A <-> ...
        # Add B in between
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node: Node):
        # ... <-> P <-> X <-> N <-> ...
        # Remove X
        # ... <-> P <-> N <-> ...
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = node.prev = None # Cleanup

    def _move_to_head(self, node: Node):
        # HEAD <-> A <-> P <-> X <-> N <-> ...
        # Move X to head (Detach first, then insert at head)
        # HEAD <-> X <-> A <-> P <-> N <-> ...
        self._remove_node(node)
        self._add_after_head(node)

    def _pop_tail(self) -> Node:
        # HEAD <-> A <-> B <-> TAIL
        # Pop B
        # HEAD <-> A <-> TAIL
        p = self.tail.prev
        self._remove_node(p)
        return p

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1
        else:
            self._move_to_head(self.hm[key])
            return self.hm[key].value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.value = value
            self._move_to_head(node)
        else:
            node = Node(key, value)
            self.hm[key] = node
            self._add_after_head(node)
            
            if len(self.hm) > self.capacity:
                tail = self._pop_tail()
                del self.hm[tail.key]


# LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
