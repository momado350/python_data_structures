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

    """
    Nodes Python Setter
We are only allowing the value of the node to be set upon creation. However, we want to allow updating the link of the node.
 For this, we will use a setter to modify the self.link_node attribute.

The method should be called .set_link_node() and should take link_node as an argument. It should then update the self.link_node attribute as appropriate.
"""

# Define your set_link_node method below:

  def set_link_node(self, link_node):
     self.link_node = link_node

#instantiate three nodes. None have an argument for link_node
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

"""
Now let’s give these nodes some responsibilities! yacko can keep track of dot and dot can keep up with wacko. wacko can’t keep track of anything though.

Below the newly created nodes, use your .set_link_node() method to give:

yacko a link_node of dot
dot a link_node of wacko
"""

dot.set_link_node(wacko)
yacko.set_link_node(dot)

"""
Create two new variables, dots_data, and wackos_data. Use both getter methods to get dot‘s value from yacko and get wacko‘s value from dot. Print dots_data and wackos_data to the console to see the results!

When your code is passing, take a moment to consider:

How would you get yacko‘s value?
How could you get from yacko to wacko‘s value?
How do you think nodes could be helpful for keeping track of and storing information?
"""

dots_data = yacko.get_link_node().get_value()
wackos_data = dot.get_link_node().get_value()

print(dots_data)
print(wackos_data)

