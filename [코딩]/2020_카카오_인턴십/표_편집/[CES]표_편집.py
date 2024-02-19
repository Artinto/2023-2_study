class Node:
    def __init__(self, value):
        self.up = None
        self.down = None
        self.value = value

class LinkedList:
    def __init__(self, node):
        self.head = node;

        
def solution(n, k, cmd):

    isDelete = [False] * n
    stack = []
    linkedList = LinkedList(Node(0))
    now_node = linkedList.head
    for i in range(1, n): # 각각의 노드 이어주는 과정
        node = Node(i)
        now_node.down = node
        node.up = now_node
        now_node = node
    
    now_node = linkedList.head
    for _ in range(k):
        now_node = now_node.down

    
    def down(x): # 선택된 행에서 x칸 밑으로
        nonlocal now_node
        # nonlocal -> 이와 같은 중첩 함수에서 외부 함수의 변수를 참조하기 위해 사용
        for _ in range(x):
            now_node = now_node.down
        
    def up(x): # # 선택된 행에서 x칸 위로
        nonlocal now_node
        for _ in range(x):
            now_node = now_node.up
    
    def delete():
        nonlocal now_node
        stack.append(now_node) # 나중에 복구할 때를 대비하여 일단 stack list에 저장
        isDelete[now_node.value] = True # 제거 됨을 표시
        
        upNode = now_node.up
        downNode = now_node.down
        
        # 삭제된 행을 기준으로 위 node와 아래 node를 이어주기 위한 코드
        if upNode:
            upNode.down = downNode
        if downNode:
            downNode.up = upNode
            now_node = downNode # 최종적으로 now node는 한 칸 아래의 노드가 되어야 함
        else:
            now_node = upNode
            
    def restore():
        nonlocal now_node
        reNode = stack.pop() # 가장 최근 들어온 Node가 reNode에 저장
        isDelete[reNode.value] = False
        upNode = reNode.up
        downNode = reNode.down
        if upNode:
            upNode.down = reNode
        if downNode:
            downNode.up = reNode
        
    
    for com in cmd:
        if com[0] == "U":
            c, x = com.split()
            up(int(x))
        elif com[0] == "D":
            c, x = com.split()
            down(int(x))
        elif com[0] == "C":
            delete()
        else:
            restore()
    
        
    answer = ""
    for i in isDelete:
        if i == False:
            answer += "O"
        else:
            answer += "X"
            
    return answer
