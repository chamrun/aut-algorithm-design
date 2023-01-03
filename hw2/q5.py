def main():
    numbers = [2, 4, 1, 3, 5, 6, 7, 3, 1, 2, 4]

    k = 3
    tree = make_tree(numbers)
    print(find_kth_largest(tree, k))


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def make_tree(numbers):
    root = Node(numbers[0])
    for i in range(1, len(numbers)):
        current = root
        while True:
            if numbers[i] > current.data:
                if current.right is None:
                    current.right = Node(numbers[i])
                    break
                else:
                    current = current.right
            else:
                if current.left is None:
                    current.left = Node(numbers[i])
                    break
                else:
                    current = current.left
    return root


def find_kth_largest(root, k):
    if root is None:
        return None
    if k < 1:
        return None
    if root.right is None and root.left is None:
        if k == 1:
            return root.data
        else:
            return None
    if root.right is None:
        if k == 1:
            return root.data
        else:
            return find_kth_largest(root.left, k - 1)
    if root.left is None:
        if k == 1:
            return root.data
        else:
            return find_kth_largest(root.right, k - 1)
    if k == 1:
        return root.data
    else:
        return find_kth_largest(root.right, k - 1)


if __name__ == '__main__':
    main()
