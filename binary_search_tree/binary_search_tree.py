class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # print("parent value", self.value, "insert Value", value)
    if value < self.value:
      if self.left is None:
        # print("left create")
        self.left = BinarySearchTree(value)
      else:
        # print("left insert")
        self.left.insert(value)
    else:
      if self.right is None:
        # print("right create")
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)
        # print("right insert")

  def contains(self, target):
    if self.value == target:
      return True
    elif target < self.value:
      if self.left is not None:
        return self.left.contains(target)
      else:
        return False
    else:
      if self.right is not None:
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    current = self
    while current.right is not None:
      current = current.right
    return current.value
