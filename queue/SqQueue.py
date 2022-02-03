class SqQueue(object):
    def __init__(self, l: list = None):
        super(SqQueue, self).__init__()
        self.__queue = []
        self.list_convert(l)

    def list_convert(self, l: list) -> None:
        if l is not None:
            for x in l:
                self.enter_queue(x)

    def clear_queue(self) -> None:
        self.__queue = []

    def queue_empty(self) -> bool:
        return not bool(len(self.__queue))

    def get_head(self) -> object:
        return self.__queue[0]

    def enter_queue(self, e: object) -> None:
        self.__queue.append(e)

    def delete_queue(self) -> object:
        return self.__queue.pop(0)

    def queue_length(self) -> int:
        return len(self.__queue)

    def __repr__(self):
        return str(self.__queue)
