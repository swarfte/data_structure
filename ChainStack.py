class Node(object):  # 創建一個節點
    def __init__(self, e=None, n=None):  # 預設生成空節點
        super(Node, self).__init__()
        self.element = e  # 數據域
        self.next = n  # 指針域


class ChainStack(object):
    def __init__(self, l=None):
        super(ChainStack, self).__init__()
        self.__head = None
        self.__len = 0
        self.list_change(l)

    def list_change(self, l):
        if l is not None:
            for x in l:
                self.push(x)

    def clear_stack(self):
        self.__head = Node()
        self.__len = 0

    def stack_empty(self):
        return not bool(self.__len)

    def stack_lengths(self):
        return self.__len

    def get_top(self):
        return self.__head

    def push(self, e):
        self.__len += 1
        new_node = Node(e)
        new_node.next = self.__head
        self.__head = new_node

    def pop(self):
        self.__len -= 1
        throw = self.__head.element
        self.__head = self.__head.next
        return throw


class Postfix(object): #TODO
    def __init__(self, infix_sentence: str = None):
        super(Postfix, self).__init__()
        self.__stack = ChainStack()
        self.__high = ["*", "/", "%", "("]  # 高優先度
        self.__low = ["+", "-", ")"]  # 低優先度
        self.__prior_is_number = False
        self.__postfix_sentence = ""
        if infix_sentence is not None:
            self.infix_to_postfix(infix_sentence)

    def __priority(self, symbol: str):
        if symbol in self.__high:
            return 1
        else:
            return 0

    def __infix_to_postfix_digit(self, number: str):  # 把中綴表達式的數字轉換為後綴表達式的形式
        if len(self.__postfix_sentence) == 0:  # 第一個數字的時候(中綴表達式開頭必為數字或括號)
            self.__postfix_sentence += number
        else:
            if self.__prior_is_number:
                self.__postfix_sentence += number
            else:  # 如果之一個元素為符號 則為空格分隔
                self.__postfix_sentence += " " + number
        self.__prior_is_number = True  # 用於判斷是否為連續數字

    def __infix_to_postfix_stack_empty(self, symbol: str):  # 空棧時壓入當前符號
        self.__stack.push(symbol)

    def __infix_to_postfix_greater(self, symbol: str):  # 如果當前的符號優先度大於棧頂時壓入當前符號
        self.__stack.push(symbol)

    def __infix_to_postfix_lower(self, symbol: str):
        if symbol == ")":
            self.__infix_to_postfix_lower_bracket(symbol)
        else:
            self.__infix_to_postfix_lower_operate(symbol)

    def __infix_to_postfix_lower_operate(self, symbol: str):
        while self.__priority(symbol) > self.__priority(self.__stack.get_top()) and not self.__stack.stack_empty():
            self.__postfix_sentence += " " + self.__stack.pop()
        self.__stack.push(symbol)

    def __infix_to_postfix_lower_bracket(self, symbol: str):  # 當前符號為右括號的情況
        while self.__stack.get_top() != "(" and not self.__stack.stack_empty():
            self.__postfix_sentence += " " + self.__stack.pop()

    def __infix_to_postfix_symbol(self, symbol: str):  # 把中綴表達式的符號轉換為後綴表達式
        self.__prior_is_number = False
        if self.__stack.stack_empty():  # 如果為空棧
            self.__infix_to_postfix_stack_empty(symbol)
        else:
            if self.__priority(symbol) > self.__priority(self.__stack.get_top()):  # 如果當前的符號優先度大於棧頂
                self.__infix_to_postfix_greater(symbol)
            else:
                self.__infix_to_postfix_lower(symbol)

    def __infix_to_postfix_final(self):
        while not self.__stack.stack_empty():
            self.__postfix_sentence += " " + self.__stack.pop()

    def infix_to_postfix(self, infix_sentence: str):  # 中綴表達式轉後綴表達式
        for x in infix_sentence:
            if x.isdigit():
                self.__infix_to_postfix_digit(x)
            else:
                self.__infix_to_postfix_symbol(x)
            print(self.__postfix_sentence)
        self.__infix_to_postfix_final()

    def get_postfix(self):
        return self.__postfix_sentence
