class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  
  def insert(self, value):
    if value < self.value:
      if self.left != None:
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if self.right != None:
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    print('start of def: self.value', self.value,'target', target)
    if target == self.value:
      return True
    if target < self.value:
      if self.left:
        print('had a left')
        return self.left.contains(target)        
      else:
        return False
    else:
      if self.right:
        print('had a right')
        return self.right.contains(target)
      else:
        return False

  def get_max(self):
    current = self    
    while current.right:
      current = current.right
    return current.value
