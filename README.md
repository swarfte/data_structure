**python數據結構**
=============

## 目錄

> * [list](#線性表list)
>* [stack](#棧stack)
>* [queue](#隊列queue)
>* [tree](#樹tree)
>* [graph](#圖graph)

# 線性表(list)

> * SqList.py 列表
>* LinkList.py 單鏈表
>* StaticLinkList.py 靜態鏈表
>* CircularLinkList.py 循環鏈表
>* DoubleLinkList.py 雙向循環鏈表

* ## 基本功能
  > * __init__():初始化,建立一個空的線性表
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

> * SequentialStack.py 順序棧
>* ChainStack.py 鏈棧

* ## 基本功能
  > * __init__():初始化, 建立一個空棧
  >* clear_stack():將棧清空
  >* stack_empty():若棧為空,返回true,否則返回false
  >* get_top():若棧為非空,返回棧頂的元素
  >* push(e):插入元素e到棧中并成為棧頂元素
  >* pop(e):刪除並設回棧頂元素
  >* stack_lengths():返回棧的長度

# 隊列(queue)

> * SqQueue.py 線性隊列
>* ChainQueue 鏈式隊列

* ## 基本功能
  > * __init__():初始化, 建立一個空隊列
  >* clear_queue():將隊列清空
  >* queue_empty():若隊列為空,返回true,否則返回false
  >* get_head():若隊列為非空,返回隊列的隊頭元素
  >* enter_queue(e):插入元素e至隊列並成為隊尾元素
  >* delete_queue():剛除並返回隊列中的隊頭元素
  >* queue_length():返回隊列的元素個數

# 樹(tree)

> * ParentalNotation.py 雙親表示法
>* ChildNotation.py 孩子表示法
>* KidBrotherNotation.py 孩子兄弟表示法

* ## 基本功能
  > * __init__():初始化,構造一個空樹
  >* clear_tree():若樹存在,把樹變為空樹
  >* tree_empty():若樹為空樹,返回true,否則返回false
  >* tree_depth():返回樹的深度
  >* value(cur_e):cur_e是樹中的一個節點,返回該節點的值
  >* parent(cur_e):若cur_e為樹的非根節點,返回它的雙親,否則返回空
  >* left_child(cur_e):若cur_e有左兄弟,則返回它的左兄弟,否則返回空
  >* right_child(cur_e):若cur_e有右兄弟,則返回它的右兄弟,否則返回空
  >* insert_child(cur_e,c):cur_e為樹中的節點,c為要插在cur_e後的節點
  >* delete_child(p,i):p為樹中某個節點,i為節點p的度,刪除機中p所轉結點的第i棵子樹

# 圖(graph)

* ## 基本功能
  > * __init__():初始化,構造一個圖
  > * create_graph(v,r): 按照頂點v和弧邊r構建圖
  > * destroy_graph(): 若圖存在,則銷毀圖
  > * locate_vex(u):若圖中存在頂點u,返回u在圖中的位置
  > * get_vex(v):返回圖中頂點v的值
  > * put_vex(v,value):對圖中頂點v賦值value
  > * first_AdjVex(v): 返回v的一個鄰近頂點,若沒有鄰近頂點則返回None
  > * next_AdjVex(v,w): 返回頂點v相對於頂點w的下一個鄰接頂點,若w是v的最後一個鄰接點則返回None
  > * insert_vex(v):在圖中增添新頂點v
  > * delete_vex(v): 在圖中刪除頂點v及其相關的弧
  > * insert_arc(v,w): 在圖中增添弧<v,w>,若圖是無向圖,則需要增添對稱弧<w,v>
  > * delete_arc(v,w): 在圖中刪除弧<v,w>,若圖是無向圖,則需要刪除對稱弧<w,v>
  > * dfs_traverse(): 對圖進行深度優先遍歷,在遍歷過程中對每個頂點調用
  > * bfs_traverse(): 對圖進制廣度優先遍歷,在遍歷過程中對每個頂點調用
