class SequentialStack(object):
    def __init__(self, l: list = None):
        super(SequentialStack, self).__init__()
        self.__stack = []
        self.__top = None
        self.__len = 0
        self.list_convert(l)

    def list_convert(self, l: list) -> None:
        if l is not None:
            for x in l:
                self.push(x)

    def clear_stack(self) -> None:
        self.__stack = []
        self.__top = None
        self.__len = 0

    def push(self, e: object) -> None:
        self.__len += 1
        self.__top = e
        self.__stack.append(self.__top)

    def pop(self) -> object:
        self.__len -= 1
        throw = self.__top
        self.__stack = self.__stack[:-1]
        if self.__len > 0:
            self.__top = self.__stack[self.__len - 1]
        else:
            self.__top = None
        return throw

    def get_top(self) -> object:
        return self.__top

    def stack_lengths(self) -> int:
        return self.__len

    def stack_empty(self) -> bool:
        return not bool(self.__len)


class Postfix(object):  # 用於把中綴表達式轉換為後綴表達式
    def __init__(self, infix_sentence: str = None):
        super(Postfix, self).__init__()
        self.__stack = SequentialStack()  # 用於處理表達式
        self.__high = ["*", "/", "%", "("]  # 高優先度
        self.__low = ["+", "-", ")"]  # 低優先度
        self.__prior_is_number = False  # 判斷是否為連續數字
        self.__prior_is_bracket = False  # 判斷是否是在括號內
        self.__postfix_sentence = ""  # 存放後綴表達式
        self.__symbol = ["+", "-", "*", "/", "%"]  # 用於存放運算符號
        self.__number_stack = SequentialStack()  # 表達式運算用
        self.__prior_number = ""  # 存放連續的數字
        if infix_sentence is not None:  # 初始化轉為中綴表達式(可選)
            self.infix_to_postfix(infix_sentence)

    def __priority(self, symbol: str) -> int:  # 用於判斷符號的優先度
        if symbol in self.__high:
            return 1
        elif symbol in self.__low:
            return 0

    def __infix_to_postfix_digit(self, number: str) -> None:  # 把中綴表達式的數字轉換為後綴表達式的形式
        if len(self.__postfix_sentence) == 0:  # 第一個數字的時候(中綴表達式開頭必為數字或括號)
            self.__postfix_sentence += number
        else:
            if self.__prior_is_number:
                self.__postfix_sentence += number
            else:  # 如果前一個元素為符號 則為空格分隔
                self.__postfix_sentence += " " + number
        self.__prior_is_number = True  # 用於判斷是否為連續數字

    def __infix_to_postfix_stack_empty(self, symbol: str) -> None:  # 空棧時壓入當前符號
        self.__stack.push(symbol)

    def __infix_to_postfix_greater(self, symbol: str) -> None:  # 如果當前的符號優先度大於棧頂時壓入當前符號
        if self.__priority(symbol) == self.__priority(self.__stack.get_top()) \
                and not self.__prior_is_bracket and symbol != "(":  # 如果同為高優先度符號
            self.__postfix_sentence += " " + self.__stack.pop()
        self.__stack.push(symbol)
        self.__prior_is_bracket = False
        if symbol == "(":
            self.__prior_is_bracket = True

    def __infix_to_postfix_lower(self, symbol: str) -> None:  # #棧頂為高優先度符號 目前元素為低優先度符號
        if symbol == ")":
            self.__infix_to_postfix_lower_bracket(symbol)  # 針對右括號的操作
        else:
            self.__infix_to_postfix_lower_operate(symbol)

    def __infix_to_postfix_lower_operate(self, symbol: str) -> None:  # 常規低優先度符號操作
        while not self.__stack.stack_empty():
            if self.__priority(symbol) < self.__priority(self.__stack.get_top()) and not self.__prior_is_bracket:
                self.__postfix_sentence += " " + self.__stack.pop()
            else:
                break
        # self.__postfix_sentence += " " + self.__stack.pop()
        self.__stack.push(symbol)

    def __infix_to_postfix_lower_bracket(self) -> None:  # 當前符號為右括號的情況
        while not self.__stack.stack_empty():
            if self.__stack.get_top() != "(":
                self.__postfix_sentence += " " + self.__stack.pop()
            else:
                break

    def __infix_to_postfix_symbol(self, symbol: str) -> None:  # 把中綴表達式的符號轉換為後綴表達式
        self.__prior_is_number = False
        if self.__stack.stack_empty():  # 如果為空棧
            self.__infix_to_postfix_stack_empty(symbol)
        else:  # 非空棧的情況
            if self.__priority(symbol) > self.__priority(self.__stack.get_top()) \
                    or self.__priority(symbol) == self.__priority(self.__stack.get_top()) \
                    and symbol != ")":  # 如果當前的符號優先度大於棧頂
                self.__infix_to_postfix_greater(symbol)
            else:
                self.__infix_to_postfix_lower(symbol)

    def __infix_to_postfix_final(self) -> None:  # 在表達式的最後把棧中全部符號按輸序輸出
        while not self.__stack.stack_empty():
            self.__postfix_sentence += " " + self.__stack.pop()
        self.__postfix_sentence = self.__postfix_sentence.replace(" (", "").replace(" )", "")
        self.__prior_is_number = False
        self.__prior_is_bracket = False

    def infix_to_postfix(self, infix_sentence: str) -> None:  # 中綴表達式轉後綴表達式
        for x in infix_sentence:
            # print("symbol : ", x) #測試用 用於觀察當前的符號
            if x.isdigit():
                self.__infix_to_postfix_digit(x)
            else:
                self.__infix_to_postfix_symbol(x)
            # print(self.__postfix_sentence) # 測試用 用於檢測當前表達式的狀態
        self.__infix_to_postfix_final()

    def get_postfix(self) -> str:  # 回傳後綴表達式
        return self.__postfix_sentence

    def postfix(self, postfix_sentence: str):
        self.__postfix_sentence = postfix_sentence

    def calc(self) -> str:  # 使用後綴表達式進行運算
        for x in self.__postfix_sentence:
            if x.isdigit():  # 數字的情況
                self.__calc_digits(x)  # 加入數字(未入棧)
            elif x != " ":
                self.__calc_symbol(x)  # 進行符號運算
            else:
                self.__calc_continuous()  # 把待入棧的數字壓棧
        return self.__number_stack.pop()

    def __calc_continuous(self) -> None:  # 處理連續的數字
        if self.__prior_is_number:
            self.__number_stack.push(self.__prior_number)
            self.__prior_number = ""
            self.__prior_is_number = False

    def __calc_digits(self, symbol: str) -> None:  # 當前元素為數字的處理
        self.__prior_number += symbol
        self.__prior_is_number = True

    def __calc_symbol(self, symbol: str) -> None:  # 當前元素為符號的處理
        last_num = float(self.__number_stack.pop())
        prior_num = float(self.__number_stack.pop())
        new_num = self.__symbol_operate(last_num, prior_num, symbol)
        self.__number_stack.push(new_num)

    def __symbol_operate(self, last_num: float, prior_num: float, symbol: str) -> str:  # 用於不同符號的運算
        new_num = 0
        if symbol == self.__symbol[0]:  # 加法
            new_num = prior_num + last_num
        elif symbol == self.__symbol[1]:  # 減法
            new_num = prior_num - last_num
        elif symbol == self.__symbol[2]:  # 乘法
            new_num = prior_num * last_num
        elif symbol == self.__symbol[3]:  # 除法
            new_num = prior_num / last_num
        elif symbol == self.__symbol[4]:  # 餘法
            new_num = prior_num % last_num
        return str(new_num)
