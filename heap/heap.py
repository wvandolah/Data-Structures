class Heap:
  def __init__(self):
    # storage starts with an unused 0 to make 
    # integer division simpler later on
    self.storage = [0]
    self.size = 0

  def insert(self, value):
    self.storage.append(value)
    self.size += 1

    #call bubble to place the value in valid spot
    self._bubble_up(self.size)

  def delete(self):
    # store our max value in a var to reture
    retval = self.storage[1]
    # replace storage with last element. causes all to swap and reorder
    self.storage[1] = self.storage[self.size]
    self.size -= 1
    # remove the last element from the heap
    self.storage.pop()
    # call _sift_dow to move the element at index 1 down
    self._sift_down(1)
    return retval

  def get_max(self):
    return self.storage[1]

  def get_size(self):
    return self.size

  def _bubble_up(self, index):
    # keep bubbling the element at the given index up the heap
    # loop until no longer have vaild indes
    # // = floor division
    while index // 2 > 0:
      if self.storage[index // 2] < self.storage[index]:
        # we need to swap
        self.storage[index // 2], self.storage[index] = self.storage[index], self.storage[index // 2]
        #update our index value to parent's index
      else:
        break
      index = index // 2


  def _sift_down(self, index):
    while (index * 2 ) <= self.size:
      #find larger child
      mc = self._max_child(index)
      # check if mc and current need a good swapping
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      else:
        break
      # update index
      index = mc

  def _max_child(self, index):
    if index * 2 + 1 > self.size:
      return index * 2
    else:
      # return child with larger value
      return index * 2 if self.storage[index * 2] > self.storage[index * 2 + 1] else index * 2 + 1
