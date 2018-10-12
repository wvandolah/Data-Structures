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
    new_node = Node(value)
    if self.head is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.set_next(new_node)
      self.tail = new_node

  def remove_head(self):
    if self.head is None:
      return None
    deleted = self.head.get_value()
    self.head = self.head.get_next()
    if self.head is None:
      self.tail = None
    return deleted

  def contains(self, value):
    current = self.head
    found = False
    while current and found is False:
      if current.get_value() == value:
        found = True
      else:
        current = current.get_next()
    return found

  def get_max(self):
    if self.head:
      head = self.head
      result = head.get_value()
      while head is not None:
        if head.value > result:
          result = head.value
        head = head.get_next()
      return result

# # creating a linked list class
# ll = LinkedList()
# # adding to tail
# ll.add_to_tail(1)
# print('head', ll.head.get_value())
# print('tail', ll.tail.get_value())
# ll.add_to_tail(2)
# # notice that the value of head never changes but tail is always the last value added
# print('head', ll.head.get_value())
# print('tail', ll.tail.get_value())
# ll.add_to_tail(3)
# print('head', ll.head.get_value())
# print('tail', ll.tail.get_value())
# ll.add_to_tail(4)
# print('head', ll.head.get_value())
# print('tail', ll.tail.get_value())
# print(ll.contains(5))

# print('current', ll.head.get_value(), 'next', ll.head.get_next().get_value())
# print('current', ll.head.get_next().get_value(), 'next', ll.head.get_next().get_next().get_value())
# print('current', ll.head.get_next().get_next().get_value(), 'next', ll.head.get_next().get_next().get_next().get_value())