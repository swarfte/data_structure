**python數據結構**
=============
## 目錄
>* [線性表(list)](#線性表(list))
>* [棧(stack)](#棧(stack))
>* [隊列(queue)](#隊列(queue))
# 線性表(list)
>* SqList.py 列表
>* LinkList.py 單鏈表
>* StaticLinkList.py 靜態鏈表
>* CircularLinkList.py 循環鏈表
>* DoubleLinkList.py 雙向循環鏈表
* ## 基本功能
  >* __init__():初始化,建立一個空的線性表
  >* list_empty(): 判斷線性表是否為空
  >* clear_list(): 清空線性表
  >* get_elem(index): 獲取指定index的元素
  >* locate_elem(e): 判斷線性表中是否有和e相同的元素,查找成功返回True,否則返回False
  >* add_tail(e): 在線性表結尾插入元素e
  >* add_head(e): 在線性表開頭插入元素e
  >* pop_tail():刪除並返回線性表中最後的元素
  >* pop_head():刪除並返回線性表中第一個元素
  >* list_insert(index,e): 在線性表中第index位置插入元素e
  >* list_delete(index):刪除並返回線性表中第i個位置元素
  >* list_length():返回線性表的元素個數
  >* get_list():返回整個線性表
# 棧(stack)
>* SequentialStack.py 順序棧
>* ChainStack.py 鏈棧
* ## 基本功能
  >* __init__():初始化, 建立一個空棧
  >* clear_stack():將棧清空
  >* stack_empty():若棧為空,返回true,否則返回false
  >* get_top():若棧為非空,返回棧頂的元素
  >* push(e):插入元素e到棧中并成為棧頂元素
  >* pop(e):刪除並設回棧頂元素
  >* stack_lengths():返回棧的長度
# 隊列(queue)
>* SqQueue.py 線性隊列
* ## 基本功能
  >* __init__():初始化, 建立一個空隊列
  >* clear_queue():將隊列清空
  >* queue_empty():若隊列為空,返回true,否則返回false
  >* get_head():若隊列為非空,返回隊列的隊頭元素
  >* en_queue(e):插入元素e至隊列並成為隊尾元素
  >* de_queue():剛除並返回隊列中的隊頭元素
  >* queue_length():返回隊列的元素個數