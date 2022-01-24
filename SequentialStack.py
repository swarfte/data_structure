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
        if self.__len > 0:
            self.__top = self.__stack[self.__len - 1]
        else:
            self.__top = None
        return throw

    def get_top(self):
        return self.__top

    def stack_lengths(self):
        return self.__len

    def stack_empty(self):
        return not bool(self.__len)


class Postfix(object):  # 用於把中綴表達式轉換為後綴表達式
    def __init__(self, infix_sentence: str = None):
        super(Postfix, self).__init__()
        self.__stack = SequentialStack()
        self.__high = ["*", "/", "%", "("]  # 高優先度
        self.__low = ["+", "-", ")"]  # 低優先度
        self.__prior_is_number = False
        self.__prior_is_bracket = False
        self.__postfix_sentence = ""
        if infix_sentence is not None:
            self.infix_to_postfix(infix_sentence)

    def __priority(self, symbol: str):  # 用於判斷符號的優先度
        if symbol in self.__high:
            return 1
        elif symbol in self.__low:
            return 0

    def __infix_to_postfix_digit(self, number: str):  # 把中綴表達式的數字轉換為後綴表達式的形式
        if len(self.__postfix_sentence) == 0:  # 第一個數字的時候(中綴表達式開頭必為數字或括號)
            self.__postfix_sentence += number
        else:
            if self.__prior_is_number:
                self.__postfix_sentence += number
            else:  # 如果前一個元素為符號 則為空格分隔
                self.__postfix_sentence += " " + number
        self.__prior_is_number = True  # 用於判斷是否為連續數字

    def __infix_to_postfix_stack_empty(self, symbol: str):  # 空棧時壓入當前符號
        self.__stack.push(symbol)

    def __infix_to_postfix_greater(self, symbol: str):  # 如果當前的符號優先度大於棧頂時壓入當前符號
        if self.__priority(symbol) == self.__priority(self.__stack.get_top()) \
                and not self.__prior_is_bracket and symbol != "(":  # 如果同為高優先度符號
            self.__postfix_sentence += " " + self.__stack.pop()
        self.__stack.push(symbol)
        self.__prior_is_bracket = False
        if symbol == "(":
            self.__prior_is_bracket = True

    def __infix_to_postfix_lower(self, symbol: str):  # #棧頂為高優先度符號 目前元素為低優先度符號
        if symbol == ")":
            self.__infix_to_postfix_lower_bracket(symbol)  # 針對右括號的操作
        else:
            self.__infix_to_postfix_lower_operate(symbol)

    def __infix_to_postfix_lower_operate(self, symbol: str):  # 常規低優先度符號操作
        while not self.__stack.stack_empty():
            if self.__priority(symbol) < self.__priority(self.__stack.get_top()) and not self.__prior_is_bracket:
                self.__postfix_sentence += " " + self.__stack.pop()
            else:
                break
        # self.__postfix_sentence += " " + self.__stack.pop()
        self.__stack.push(symbol)

    def __infix_to_postfix_lower_bracket(self, symbol: str):  # 當前符號為右括號的情況
        while not self.__stack.stack_empty():
            if self.__stack.get_top() != "(":
                self.__postfix_sentence += " " + self.__stack.pop()
            else:
                break

    def __infix_to_postfix_symbol(self, symbol: str):  # 把中綴表達式的符號轉換為後綴表達式
        self.__prior_is_number = False
        if self.__stack.stack_empty():  # 如果為空棧
            self.__infix_to_postfix_stack_empty(symbol)
        else:  # 非空棧的情況
            if self.__priority(symbol) > self.__priority(self.__stack.get_top()) \
                    or self.__priority(symbol) == self.__priority(self.__stack.get_top())\
                    and symbol != ")":  # 如果當前的符號優先度大於棧頂
                self.__infix_to_postfix_greater(symbol)
            else:
                self.__infix_to_postfix_lower(symbol)

    def __infix_to_postfix_final(self):  # 在表達式的最後把棧中全部符號按輸序輸出
        while not self.__stack.stack_empty():
            self.__postfix_sentence += " " + self.__stack.pop()
        self.__postfix_sentence = self.__postfix_sentence.replace(" (", "").replace(" )", "")

    def infix_to_postfix(self, infix_sentence: str):  # 中綴表達式轉後綴表達式
        for x in infix_sentence:
            print("symbol : ", x)
            if x.isdigit():
                self.__infix_to_postfix_digit(x)
            else:
                self.__infix_to_postfix_symbol(x)
            print(self.__postfix_sentence)
        self.__infix_to_postfix_final()

    def get_postfix(self):  # 回傳後綴表達式
        return self.__postfix_sentence
