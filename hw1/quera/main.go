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

func main() {
	numbers := []int{
		-5,
		-10,
		0,
		15,
		20,
		100,
		-100,
	}

	//input := getInputUntilEOF()
	//fmt.Println(input)

	bst := convertArrayToBST(numbers)

	beatifyBST(bst)

}
