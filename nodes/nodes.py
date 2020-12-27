# create a node that contains data and one link to another node.
# you should specify node data, the link can be (optional, linked to another node, or null)
# the null node in Python can be done by assigning it the value of None.

# Create the Node class below:
class Node():
    # define your class function
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node


# access data and link within our  node
# we use the getters methods for this

# Define your get_value and get_link_node methods below:
  def get_value(self):
    return self.value

  def get_link_node(self):
    return self.link_node
