#!/usr/bin/env python3

import sys

DEBUG = True


class Node(object):
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


def are_identical(root1, root2):
    # Base Case
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False

    # Check if the data of both roots is same and data of left and right subtrees are also same
    return (
        root1.name == root2.name
        and are_identical(root1.left, root2.left)
        and are_identical(root1.right, root2.right)
    )


def is_subtree(t, s):
    # Base Case
    if s is None:
        return True
    if t is None:
        return False

    # Check the tree with root as current node
    if are_identical(t, s):
        return True

    # If the tree with root as current node doesn't match then try left and right subtreee one by one
    return is_subtree(t.left, s) or is_subtree(t.right, s)


def get_enclosing(string):
    assert string[0] == "("
    assert string[-1] == ")"

    c = 0
    o = ""
    left = None
    right = None
    for s in string:
        o += s
        if s == "(":
            c += 1
        elif s == ")":
            c -= 1
        else:
            pass

        if c == 0:
            if left is None:
                left = o[1:-1]
                o = ""
            elif right is None:
                right = o[1:-1]
                o = ""
            else:
                raise ValueError

    return left, right


def build_tree(descriptor, node=None):

    if descriptor[1:] == "":
        return node

    current = Node(descriptor[0])
    if node is None:
        node = current

    left, right = get_enclosing(descriptor[1:])

    if len(left) > 0:
        node.left = build_tree(left, current)

    if len(right) > 0:
        node.right = build_tree(right, current)

    return current


def main():

    if DEBUG:
        sys.stdin = open("samples/12_input.txt")

    tree1 = build_tree(input())
    tree2 = build_tree(input())

    if is_subtree(tree1, tree2):
        print("true")
    elif is_subtree(tree2, tree1):
        print("true")
    else:
        print("false")

    raise NotImplementedError("Do not check for complete subtree!")


if __name__ == "__main__":
    main()
