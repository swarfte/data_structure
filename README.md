# python數據結構
## 線性表(list)
* SqList.py 列表
* LinkList.py 單鏈表
* StaticLinkList.py 靜態鏈表
* CircularLinkList.py 循環鏈表
* DoubleLinkList.py 雙向循環鏈表
* ### 基本功能
  * __init__():初始化
  * list_empty(): 判斷線性表是否為空
  * clear_list(): 清空線性表
  * get_elem(index): 獲取指定index的元素
  * locate_elem(e): 判斷線性表中是否有和e相同的元素,查找成功返回True,否則返回False
  * add_tail(e): 在線性表結尾插入元素e
  * add_head(e): 在線性表開頭插入元素e
  * pop_tail():刪除並返回線性表中最後的元素
  * pop_head():刪除並返回線性表中第一個元素
  * list_insert(index,e): 在線性表中第index位置插入元素e
  * list_delete(index):刪除並返回線性表中第i個位置元素
  * list_length():返回線性表的元素個數
  * get_list():返回整個線性表

## 棧(stack)
* SequentialStack.py 順序棧
* ChainStack.py 鏈棧