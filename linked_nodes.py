# Define your Node class below:
class Node():
    # define __init__() method that takes two parameters: vlaue and next_node
  def __init__(self, value, next_node=None):
      # save our vars to self
    self.value = value
    self.next_node = next_node


    #define get_value and next node and return their corresponding values from self
  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node

# define set_next_node() method that takes two params self and next_node, and allow for updting to next node
  def set_next_node(self, next_node):
      self.next_node = next_node

"""
create an instance of Node called my_node with a value of 44.

Use .get_value() to print the value of my_node
"""
  my_node = Node(44)
  print(my_node.get_value())