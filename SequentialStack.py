class SequentialStack(object):
    def __init__(self, l=None):
        super(SequentialStack, self).__init__()
        self.__stack = []
        self.__top = None
        self.__len = 0
        self.list_change(l)

    def list_change(self, l):
        if l is not None:
            for x in l:
                self.push(x)

    def clear_stack(self):
        self.__stack = []
        self.__top = None
        self.__len = 0

    def push(self, e):
        self.__len += 1
        self.__top = e
        self.__stack.append(self.__top)

    def pop(self):
        self.__len -= 1
        throw = self.__top
        self.__stack = self.__stack[:-1]
        self.__top = self.__stack[self.__len - 1]
        return throw

    def get_top(self):
        return self.__top

    def stack_lengths(self):
        return self.__len

    def stack_empty(self):
        return bool(self.__len)
