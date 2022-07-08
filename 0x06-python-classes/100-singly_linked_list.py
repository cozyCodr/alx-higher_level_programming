#!/usr/bin/python3
"""Node of a Singly Linked List"""


class Node:
    """ Node class """
    def __init__(self, data, next_node=None):
        """ initializes private variable data"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """creates a sorted linked list"""
    def __init__(self):
        self.__head = Node(0)

    """prints list"""
    def print_list(self):
        while True:
            if(self.__head.next_node is None):
                print("{}".format(self.__head.data), end="")
                break
            else:
                print("{}".format(self.__head.data))
                self.__head = self.__head.next_node
        return ""

    """prints string representation of list"""
    def __repr__(self):
        return str(self.print_list())

    """sorts node into appropriate place in linked list"""
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head.next_node is None and self.__head.data == 0:
            self.__head.next_node = new_node
        else:
            save_head = Node(0)
            save_head = self.__head
            if self.__head.data < value:
                while self.__head.data <= value:
                    if self.__head.next_node is not None:
                        if self.__head.next_node.data >= value:
                            new_node.next_node = self.__head.next_node
                            self.__head.next_node = new_node
                            break
                    if self.__head.next_node is None:
                        self.__head.next_node = new_node
                        break
                    self.__head = self.__head.next_node
                self.__head = save_head
            elif self.__head.data > value:
                new_node.next_node = self.__head
                self.__head = new_node
