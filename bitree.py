import abc


class BiTreeAlgo(abc.ABC):
    """
    Abstract class for an algorithm on a binary tree.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def empty_case(self, mt_node, inp):
        return

    @abc.abstractmethod
    def non_empty_case(self, data_node, inp):
        return


class PrefixToString(BiTreeAlgo):
    """
    Does a pre-order traversal of the tree to produce a
    string in prefix (function call) order

    >>> t = MTNode()
    >>> t.execute(PrefixToString())
    ''

    >>> t = DataNode('*', DataNode(3), DataNode(4))
    >>> t.execute(PrefixToString())
    '*(3, 4)'

    >>> t = DataNode('+', DataNode('*', DataNode(3), DataNode(4)), DataNode(-5))
    >>> t.execute(PrefixToString())
    '+(*(3, 4), -5)'
    """
    # TODO: replace pass below with your implementation
    def empty_case(self, mt_node, inp):
        return ''

    def non_empty_case(self, data_node, inp):
        left = data_node.get_left().execute(self, inp)
        right = data_node.get_right().execute(self, inp)
        return str(data_node.get_data()) + '(' + left + ', ' + right + ')' if left or right else str(data_node.get_data())


class PostfixToString(BiTreeAlgo):
    """
    Does a post-order traversal of the tree to produce a
    string in postfix (Reverse Polish Notation) order

    >>> t = MTNode()
    >>> t.execute(PostfixToString())
    ''

    >>> t = DataNode('*', DataNode(3), DataNode(4))
    >>> t.execute(PostfixToString())
    '3 4*'

    >>> t = DataNode('+', DataNode('*', DataNode(3), DataNode(4)), DataNode(-5))
    >>> t.execute(PostfixToString())
    '3 4* -5+'
    """
    # TODO: replace pass below with your implementation
    def empty_case(self, mt_node, inp):
        return ''

    def non_empty_case(self, data_node, inp):
        left = data_node.get_left().execute(self, inp)
        right = data_node.get_right().execute(self, inp)
        operator = data_node.get_data()
        if left and right:
            return str(left) + ' ' + str(right) + str(operator)
        else:
            return str(left) + str(right) + str(operator)


class VerticalStringAlgo(BiTreeAlgo):
    """
    Prints a binary string vertically with the left subtree as the first one vertically
    DO NOT CHANGE THIS CLASS!
    """

    class VerticalStringHelper(BiTreeAlgo):
        def empty_case(self, mt_node, _):
            return "|_ []"

        def non_empty_case(self, data_node, left_lead):
            left_string = data_node.get_left().execute(self, left_lead + "|  ")
            right_string = data_node.get_right().execute(self, left_lead + "   ")
            return str("|_ " + str(data_node.get_data())) + "\n" \
                   + left_lead + left_string + "\n" \
                   + left_lead + right_string

    def empty_case(self, mt_node, inp):
        return "[]"

    def non_empty_case(self, data_node, inp):
        left_string = data_node.get_left().execute(self.VerticalStringHelper(), "|  ")
        right_string = data_node.get_right().execute(self.VerticalStringHelper(), "   ")
        return str(data_node.get_data()) + "\n" \
               + left_string + "\n" + right_string


class BSTInsert(BiTreeAlgo):
    """
    Inserts an element into a binary search tree
    DO NOT CHANGE THIS CLASS!
    """

    def empty_case(self, mt_node, elt):
        """
        Inserting into an empty tree returns a new data node storing the specified input
        :param mt_node: the empty node that we are inserting into
        :param elt: the value to insert
        :return: a new data node storing the specified input
        """
        return DataNode(elt)

    def non_empty_case(self, data_node, elt):
        """
        Inserts into a non-empty binary search tree.
        :param data_node: the data node that we are inserting into
        :param elt: the value to insert
        :return: a new data node that stores the element per the BST invariant
        """
        if elt < data_node.get_data():
            # insert into left subtree
            return DataNode(data_node.get_data(),
                            data_node.get_left().execute(self, elt),
                            data_node.get_right())
        else:
            # insert into right subtree
            return DataNode(data_node.get_data(),
                            data_node.get_left(),
                            data_node.get_right().execute(self, elt))


class BiTree(abc.ABC):
    """
    An abstract class for a binary tree.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def execute(self, algo: BiTreeAlgo, inp=None):
        """
        Executes the given algorithm with the specified input on the list
        :param algo: the algorithm to execute
        :param inp: the (optional) input to the algorithm
        :return: the result of the execution
        """
        return

    @abc.abstractmethod
    def is_leaf(self):
        """Returns true if and only if both subtrees are empty"""
        return

    def __str__(self):
        return self.execute(VerticalStringAlgo())

    def __repr__(self):
        return 'BiTree:\n' + str(self)


class MTNode(BiTree):
    """
    The emtpy tree
    DO NOT CHANGE THIS CLASS!
    """

    # There is only 1 emtpy node,
    # so we have implemented it as a singleton
    # based on the Classic singleton at
    # https://www.packtpub.com/books/content/python-design-patterns-depth-singleton-pattern,
    # last access 11/9/2017
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MTNode, cls).__new__(cls)

        return cls.instance

    def is_leaf(self):
        return False

    def execute(self, algo: BiTreeAlgo, inp=None):
        """
        Executes the BiTreeAlgo (visitor) on the data node by delegating to the
        empty_case method of the visitor
        :param algo: the BiTreeAlgo (visitor) to execute
        :param inp: the optional parameter
        :return: the result of executing the visitor on the tree
        """
        return algo.empty_case(self, inp)


class DataNode(BiTree):
    """
    A non-empty tree that stores some data together with (possibly empty) left and right subtrees
    DO NOT CHANGE THIS CLASS!
    """

    def __init__(self, data, left: BiTree = MTNode(), right: BiTree = MTNode()):
        """

        :param data:
        :param left:
        :param right:
        """
        self._data = data
        self._left = left
        self._right = right

    def get_data(self):
        return self._data

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def is_leaf(self):
        return self._left is MTNode() and self._right is MTNode()

    def execute(self, algo: BiTreeAlgo, inp=None):
        """
        Executes the BiTreeAlgo (visitor) on the data node by delegating to the
        non_empty_case method of the visitor
        :param algo: the BiTreeAlgo (visitor) to execute
        :param inp: the optional parameter
        :return: the result of executing the visitor on the tree
        """
        return algo.non_empty_case(self, inp)


if __name__ == '__main__':
    # This is here for your own use
    """
    tree = MTNode()
    while True:
        print(tree.execute(VerticalStringAlgo()))
        val_to_insert = input('Insert a number: ')

        if val_to_insert.lower() == 'q':
            break
        val_to_insert = int(val_to_insert)
        tree = tree.execute(BSTInsert(), val_to_insert)
    """