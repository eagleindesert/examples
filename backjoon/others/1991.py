import sys

input = sys.stdin.readline


class Node:
    def __init__(self, value: str):
        self.value = value
        self.leftchild = None
        self.rightchild = None


def pre_order(node: Node, selected):
    if node is not None:
        selected.append(node.value)
        pre_order(node.leftchild, selected)
        pre_order(node.rightchild, selected)


def in_order(node: Node, selected):
    if node is not None:
        in_order(node.leftchild, selected)
        selected.append(node.value)
        in_order(node.rightchild, selected)


def post_order(node: Node, selected):
    if node is not None:
        post_order(node.leftchild, selected)
        post_order(node.rightchild, selected)
        selected.append(node.value)


def main():
    N = int(input())

    tree = {}

    example = Node("A")

    # tree["A"] = example
    # print(tree["A"].value)

    input_list = []
    for i in range(N):
        input_list.append(list(map(str, input().split())))

    # 노드 생성 과정
    # ex) tree["A"] = Node(A)
    # 처음 Node에 접근 할 수 있도록 하는 과정임
    for line in input_list:

        if line[0] not in tree:
            tree[line[0]] = Node(line[0])

        if line[1] not in tree and line[1] != ".":
            tree[line[1]] = Node(line[1])

        if line[2] not in tree and line[2] != ".":
            tree[line[2]] = Node(line[2])

        # 부모 노드에 자식 노드 추가
        tree[line[0]].leftchild = tree[line[1]] if line[1] != "." else None
        tree[line[0]].rightchild = tree[line[2]] if line[2] != "." else None

    pre_selected = []
    pre_order(tree["A"], pre_selected)
    print("".join(map(str, pre_selected)))

    in_selected = []
    in_order(tree["A"], in_selected)
    print("".join(map(str, in_selected)))

    post_selected = []
    post_order(tree["A"], post_selected)
    print("".join(map(str, post_selected)))


main()
