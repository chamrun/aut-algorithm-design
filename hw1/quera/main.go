package main

import "fmt"

type Node struct {
	value int
	left  *Node
	right *Node
}

func convertArrayToBST(arr []int) *Node {
	if len(arr) == 0 {
		return nil
	}

	mid := len(arr) / 2
	root := &Node{arr[mid], nil, nil}
	root.left = convertArrayToBST(arr[:mid])
	root.right = convertArrayToBST(arr[mid+1:])
	return root
}

func beatifyBST(root *Node) {
	if root == nil {
		return
	}

	beatifyBST(root.left)
	fmt.Println(root.value)
	beatifyBST(root.right)
}

func getInputUntilEOF() []int {
	var input int
	var arr []int
	for {
		_, err := fmt.Scanf("%d", &input)
		if err != nil {
			break
		}
		arr = append(arr, input)
	}
	return arr
}

func main() {
	numbers := getInputUntilEOF()

	//input := getInputUntilEOF()
	//fmt.Println(input)

	bst := convertArrayToBST(numbers)

	beatifyBST(bst)

}
