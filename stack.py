import abc
import lrlist


class Stack(abc.ABC):
    """
    Abstract class for a stack.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def push(self, elt):
        """
        Pushes an element onto the top of the stack
        :param elt: the element to add to the stack
        """
        return

    @abc.abstractmethod
    def pop(self):
        """
        Removes the top element from the stack
        """
        return

    @abc.abstractmethod
    def top(self):
        """
        Returns the top element on the stack (without removing it)
        :return: the top element on the stack (without removing it)
        """
        return

    @abc.abstractmethod
    def is_empty(self):
        """
        Returns True if and only if the stack is empty
        :return: True if and only if the stack is empty
        """
        return

    @abc.abstractmethod
    def __str__(self):
        return

    @abc.abstractmethod
    def __repr__(self):
        return


class LRStack(Stack):
    """
    A stack implementation based on an LRList.
    NOTE: You do not need to create/use any of the LRListAlgos to implement this.
    """

    def __init__(self):
        """
        Creates a new list with _elements set to the empty list and the _count set to 0
        >>> s = LRStack()
        >>> s._elements == lrlist.MTList()
        True
        >>> s._count
        0
        """
        # TODO: replace pass below with your implementation
        self._elements = lrlist.MTList()  # create a new empty instance of a lrlist
        self._count = 0

    def push(self, elt):
        """
        Pushes an element onto the top of the stack
        :param elt: the element to add to the stack

        >>> import random
        >>> s = LRStack()
        >>> elt = random.randint(-100, 100)
        >>> s.push(elt)
        >>> s._elements.get_elt() == elt
        True
        >>> s._count
        1
        >>> elt = random.randint(-100, 100)
        >>> s.push(elt)
        >>> s._elements.get_elt() == elt
        True
        >>> s._count
        2
        """
        # TODO: replace pass below with your implementation
        self._elements = lrlist.NEList(elt, self._elements)
        self._count += 1

    def pop(self):
        """
        Removes (and returns) the top element from the stack

        >>> import random
        >>> elt = random.randint(-100, 100)
        >>> s = LRStack()
        >>> s.push(elt)
        >>> s.pop() == elt
        True
        >>> s._count
        0

        Test popping stack of length 2
        >>> s.push(elt)
        >>> elt = random.randint(-100, 100)
        >>> s.push(elt)
        >>> s.pop() == elt
        True
        >>> s._count
        1

        Test popping an empty stack -- should throw an exception (as below)
        >>> s = LRStack()
        >>> s.pop()
        Traceback (most recent call last):
        ...
        AttributeError: 'MTList' object has no attribute 'get_elt'
        """
        # TODO: replace pass below with your implementation
        if self.is_empty():
            raise AttributeError("'MTList' object has no attribute 'get_elt'")
        else:
            top = self._elements.get_elt()
            self._elements = self._elements.get_rest()
            self._count -= 1
            return top

    def top(self):
        """
        Returns the top element on the stack (without removing it)
        :return: the top element on the stack (without removing it)

        >>> import random
        >>> elt = random.randint(-100, 100)
        >>> s = LRStack()
        >>> s.push(elt)
        >>> s.top() == elt
        True
        >>> s._count
        1

        Test top of empty stack -- should throw an exception (as below)
        >>> s = LRStack()
        >>> s.top()
        Traceback (most recent call last):
        ...
        AttributeError: 'MTList' object has no attribute 'get_elt'
        """
        # TODO: replace pass below with your implementation
        if self.is_empty():
            raise AttributeError("'MTList' object has no attribute 'get_elt'")
        else:
            return self._elements.get_elt()

    def is_empty(self):
        """
        Returns True if and only if the stack is empty
        :return: True if and only if the stack is empty

        >>> s = LRStack()
        >>> s.is_empty()
        True
        >>> s.push('foo')
        >>> s.is_empty()
        False
        """
        # TODO: replace pass below with your implementation
        if self._count == 0:
            return True
        else:
            return False

    def size(self):
        """
        Returns the number of elements in the stack
        :return: the number of elements in the stack

        >>> s = LRStack()
        >>> s.size()
        0
        >>> s.push('bar')
        >>> s.size()
        1
        """
        # TODO: replace pass below with your implementation
        return self._count

    def __str__(self):
        """
        Returns a string suitable for viewing by users
        >>> s = LRStack()
        >>> print(s)
        ()
        >>> s.push('fee')
        >>> print(s)
        (fee)
        >>> s.push('fi')
        >>> print(s)
        (fi, fee)
        """
        # TODO: replace pass below with your implementation
        return str(self._elements)

    def __repr__(self):
        """
        Returns a string for viewing by developers

        >>> s = LRStack()
        >>> s
        LRStack LRList ()
        >>> s.push('foo')
        >>> s
        LRStack LRList (foo)
        >>> s.push('bar')
        >>> s
        LRStack LRList (bar, foo)
        """
        # TODO: replace pass below with your implementation
        result = "LRStack LRList "
        result += str(self._elements)
        return result

if __name__ == '__main__':
    # This is here for your own use
    pass
