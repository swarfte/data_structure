class SqQueue(object):
    def __init__(self):
        self.__len = 0
        self.__queue = []

    def clear_queue(self) -> None:
        self.__len = 0
        self.__queue = []

    def queue_empty(self) -> bool:
        return not bool(self.__len)

    def get_head(self) -> object:
        return self.__queue[0]

    def en_queue(self, e: object) -> None:
        self.__queue.append(e)

    def de_queue(self) -> object:
        return self.__queue.pop(0)

    def queue_length(self) -> int:
        return self.__len
