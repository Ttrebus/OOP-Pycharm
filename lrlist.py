import abc


class LRListAlgo(abc.ABC):
    """
    Abstract class for an algorithm on a list.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def empty_case(self, mtlist, inp):
        return

    @abc.abstractmethod
    def non_empty_case(self, nelist, inp):
        return


class LengthAlgo(LRListAlgo):
    """
    Visitor to compute the length of a List
    DO NOT CHANGE THIS CLASS!
    """

    def empty_case(self, mtlist, _):
        """
        The empty list has a length of 0
        :param mtlist: the mtlist
        :param _: not used
        :return: 0

        >>> l = MTList()
        >>> l.execute(LengthAlgo())
        0
        """
        return 0

    def non_empty_case(self, nelist, _):
        """
        Returns the length of a non-empty list
        :param nelist: the non-empty list
        :param _: not used
        :return: the length of a non-empty list

        >>> import random
        >>> rand_lst = list(range(random.randint(4,20)))
        >>> lst = make_list(rand_lst)
        >>> lst.execute(LengthAlgo()) == len(rand_lst)
        True
        """
        return 1 + nelist.get_rest().execute(self)


class ToStringAlgo(LRListAlgo):
    """
    Visitor for implementing __str__ of the List class
    DO NOT CHANGE THIS CLASS!
    """

    class ToStringHelper(LRListAlgo):
        """
        Helper for ToString
        Notice how inp is used to (forward) accumulate the result
        """

        def empty_case(self, mtlist, inp):
            return inp + ")"

        def non_empty_case(self, nelist, inp):
            return nelist.get_rest().execute(
                self,
                inp + ", " + str(nelist.get_elt())
            )

    def empty_case(self, mtlist, _):
        """
        Empty list is easy to generate the string for!
        """
        return "()"

    def non_empty_case(self, nelist, _):
        """
        Executes the helper on the rest,
        while passing "(" + nelist.get_elt() as the parameter
        """
        return nelist.get_rest().execute(self.ToStringHelper(),
                                         "(" + str(nelist.get_elt()))


class MinAlgo(LRListAlgo):
    """
    Finds and returns the smallest (min) value in the list
    DO NOT CHANGE THIS CLASS!

    >>> import random
    >>> rand_lst = [random.randint(1, 10) for _ in range(random.randint(5,10))]
    >>> l = make_list(rand_lst)
    >>> l.execute(MinAlgo()) == min(rand_lst)
    True
    """

    class MinAlgoHelper(LRListAlgo):
        """
        Helper visitor that finds the smallest element in the List
        DO NOT CHANGE THIS CLASS!
        """

        def non_empty_case(self, nelist, smallest_so_far):
            """
            Determine which is smaller, smallest_so_far or the element at this node,
            then recursively call this algorithm on the rest of the list passing
            along the smallest
            :param nelist: the list
            :param smallest_so_far: the smallest value seen so far
            :return: the smallest value in the list
            """
            smallest = min(nelist.get_elt(), smallest_so_far)
            return nelist.get_rest().execute(self, smallest)

        def empty_case(self, mtlist, smallest_so_far):
            """
            We've hit the end of the list, so just return smallest_so_far
            :param mtlist: the emtpy list
            :param smallest_so_far: the smallest value in the list seen
            :return: the smallest value in the list seen
            """
            return smallest_so_far

    def empty_case(self, mtlist, inp):
        """
        Raises a ValueError (exception) since there is no min in an empty list
        :param mtlist: the empty list
        :param inp: not used
        :return: raises a ValueError (exception) since there is no min in an empty list
        """
        raise ValueError("Can't compute min of an empty list!")

    def non_empty_case(self, nelist, inp):
        """
        Returns the smallest element in the list delegating to MinAlgoHelper
        :param nelist: the list to check
        :param inp: not used
        :return: the smallest value in the list
        """
        return nelist.get_rest().execute(self.MinAlgoHelper(), nelist.get_elt())


class MinAndMaxAlgo(LRListAlgo):
    """
    Computes the minimum and maximum of the list in a *single* pass.
    Returns a 2 tuple where the first element of the tuple is the
            minimum value from the list, and the second element
            in the tuple is the maximum value from the list

    >>> import random
    >>> nums = [random.randint(-10,10) for _ in range(random.randint(5, 9))]
    >>> largest = max(nums)
    >>> smallest = min(nums)
    >>> lst = make_list(nums)
    >>> lst.execute(MinAndMaxAlgo()) == (smallest, largest)
    True
    """

    # TODO: replace pass below with your implementation, you may create a nested helper class
    class MinMaxHelper(LRListAlgo):
        """
        Helper visitor to compute the minimum and maximum of the list
        """

        def empty_case(self, mtlist, inp):
            """
            If the list is empty, return (None, None)
            """
            if not mtlist:
                return (None, None)
            else:
                return inp

        def non_empty_case(self, nelist, inp):
            """
            If the list is not empty, compare the current element with the current minimum and maximum,
            and update them accordingly.
            """
            min_val, max_val = inp
            if nelist.get_elt() < min_val:
                min_val = nelist.get_elt()
            if nelist.get_elt() > max_val:
                max_val = nelist.get_elt()
            return nelist.get_rest().execute(self, (min_val, max_val))

    def empty_case(self, mtlist, inp):
        """
        If the list is empty, return (None, None)
        """
        if not mtlist:
            return (None, None)
        else:
            return inp

    def non_empty_case(self, nelist, inp):
        """
        If the list is not empty, delegate to the helper class to compute the minimum and maximum
        """
        return nelist.get_rest().execute(self.MinMaxHelper(), (nelist.get_elt(), nelist.get_elt()))


class InsertInOrder(LRListAlgo):
    """
    Creates a new LRList and inserts elt into the LRList so that it is sorted
    DO NOT CHANGE THIS CLASS!
    >>> lst = MTList()
    >>> lst = lst.execute(InsertInOrder(), 5)
    >>> lst
    LRList (5)
    >>> lst = lst.execute(InsertInOrder(), 7)
    >>> lst
    LRList (5, 7)
    >>> lst = lst.execute(InsertInOrder(), 1)
    >>> lst
    LRList (1, 5, 7)
    >>> lst = lst.execute(InsertInOrder(), 3)
    >>> lst
    LRList (1, 3, 5, 7)
    """

    def empty_case(self, mtlist, elt):
        """
        Inserting into the empty list is easy, just create and return
        a new non-empty list storing elt
        """
        return NEList(elt)

    def non_empty_case(self, nelist, elt):
        if elt < nelist.get_elt():
            return NEList(elt, nelist)
        else:
            return NEList(nelist.get_elt(), nelist.get_rest().execute(self, elt))


class LRList(abc.ABC):
    """
    An abstract class for a list.
    DO NOT CHANGE THIS CLASS!
    """

    @abc.abstractmethod
    def execute(self, algo, inp=None):
        """
        Executes the given algorithm with the specified input on the list
        :param algo: the algorithm to execute
        :param inp: the (optional) input to the algorithm
        :return: the result of the execution
        """
        return

    def __str__(self):
        return self.execute(ToStringAlgo())

    def __repr__(self):
        return 'LRList {}'.format(str(self))


class MTList(LRList):
    """
    The emtpy list.
    DO NOT CHANGE THIS CLASS!
    """

    # There is only 1 emtpy list,
    # so we have implemented it as a singleton
    # based on the Classic singleton at
    # https://www.packtpub.com/books/content/python-design-patterns-depth-singleton-pattern,
    # last access 11/9/2017
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(MTList, cls).__new__(cls)

        return cls.instance

    def execute(self, algo, inp=None):
        return algo.empty_case(self, inp)


class NEList(LRList):
    """
    A non-empty list.
    DO NOT CHANGE THIS CLASS!
    """

    def __init__(self, elt, rest=MTList()):
        self._elt = elt
        self._rest = rest

    def get_elt(self):
        return self._elt

    def get_rest(self):
        return self._rest

    def execute(self, algo, inp=None):
        return algo.non_empty_case(self, inp)


def make_list(elts) -> LRList:
    """
    Helper function to convert an iterable into an LRList
    :param elts: an iterable (list, string, etc)
    :return: an LRList containing all the elements
    DO NOT CHANGE THIS CODE!
    """
    result = MTList()
    elts = reversed(elts)
    for elt in elts:
        result = NEList(elt, result)
    return result


if __name__ == '__main__':
    # this is here for your own use
    pass
