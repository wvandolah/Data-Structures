"""
Class that represents a single linked
list node that holds a single value
and a reference to the next node in the list
"""
class Node:
  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_tail(self, value):
    node = Node(value)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node

  def remove_head(self):
    if self.head == None:
      return None
    deleted = self.head.get_value()
    self.head = self.head.get_next()
    return deleted

  def contains(self, value):
    head = self.head
    while head != None:
      if head.value == value:
        return True
      head = head.next_node
    return False

  def get_max(self):
    head = self.head    
    if head == None:
      return None
    maxValue = self.head.value
    while head != None:
      if head.value > maxValue:
        maxValue = head.value
      head = head.next_node
    return maxValue


