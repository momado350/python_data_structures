# to create a Node in Python first you need to create a class
# the class takes params for the First node and the Link to next node
# linked node is optional and when initiated it might have the value of None in this case it means that is the end
class Node:
    def __init__(self, value, link_node=None):
        self.value = value
        self.link_node = link_node

    # after we create our Node class we need a way access our data (value, link_node) from our self method
    # we use getters to do so .get_value() and .get_link_node()
    def get_value(self):
        return self.value

    def get_link_node(self):
        return self.link_node

    # the value is set upon creation of the Node but we want to update our link_node sometimes
    # we use the .setter() method: and takes the link_node as parameter and updates our self.link_node

    def set_link_node(self, link_node):
        self.link_node = link_node


if __name__ == '__main__':
    # now create our nodes, only initiate values, no link for now
    yacko = Node("likes to yak")
    wacko = Node("has a penchant for hoarding snacks")
    dot = Node("enjoys spending time in movie lots")

    # link our nodes
    dot.set_link_node(wacko)
    yacko.set_link_node(dot)
    # time to put our node and link_node to test
    dots_data = yacko.get_link_node().get_value()
    wackos_data = dot.get_link_node().get_value()
    yackos_data = yacko.get_value()

    # print values from getter method
    print(dots_data)
    print(wackos_data)
    print(yackos_data)

