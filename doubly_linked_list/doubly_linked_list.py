class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    # add after the calling node
    # new node takes the calling nodes next, and the calling node as prev.
    # calling node needs to have the new node set as its next
    new_node = ListNode(value)
    new_node.next = self.next
    new_node.prev = self
    self.next = new_node

  def insert_before(self, value):
    # add before calling node
    # new node will take the calling nodes prev and the calling node as next
    # calling node prev will become the new_node
    new_node = ListNode(value)
    new_node.prev = self.prev
    new_node.next = self
    self.prev = new_node

  def delete(self):
    # just taking the calling nodes prev.next to its next and the next.prev to its prev
    # prob need to check for None here
    if self.prev is not None:
      self.prev.next = self.next
    if self.next is not None:
      self.next.prev = self.prev

class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    self.head.insert_before(value)
    self.head = self.head.prev

  def remove_from_head(self):
    # save head.next and head.value to vars
    # called delete on head
    # change head to next head var
    # return value of old head
    old_head = self.head
    self.head.delete()
    self.head = old_head.next
    return old_head.value

  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail = self.tail.next

  def remove_from_tail(self):
    old_tail = self.tail
    self.tail.delete()
    self.tail = old_tail.prev
    return old_tail.value

  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node.value)

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node.value)

  def delete(self, node):
    node.delete()
