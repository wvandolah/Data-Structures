class Heap:
  def __init__(self):
    self.storage = []
    self.size = -1

  def insert(self, value):
    self.storage.append(value)
    self.size += 1
    self._bubble_up(self.size)

  def delete(self):
    # store our max value in a var to return
    toReturn = self.storage[0]
    # replace storage with last element. causes all to swap and reorder
    self.storage[0] = self.storage[self.size]
    print(self.storage[0])
    self.storage.pop()
    self.size -= 1
    # remove the last element from the heap
    # call _sift_dow to move the element at index 1 down
    self._sift_down(0)
    return toReturn

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      # left side is the value of parent. right is value of chile
      if self.storage[(index - 1) // 2] < self.storage[index]:
        # swap
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2 ], self.storage[index]
      # update index
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= self.size:
      # figure out larger of the two children
      mc = self._max_child(index)
      # check to see if we need to swap
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
        index = mc

  def _max_child(self, index):
    # check if the right child index is out of bounds of our storage array
    if index * 2 + 2 > self.size:
      print(self.storage)
      return index * 2 + 1
    else:
      # return the index correstpoing to the child node that has the larger value
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2

heap = Heap()

heap.insert(6)
print(heap.storage)
heap.insert(7)
print(heap.storage)
heap.insert(20)
print(heap.storage)
heap.insert(2)
print(heap.storage)
print(heap.delete())
print(heap.storage)
print(heap.get_max())