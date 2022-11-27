package main

import (
	"encoding/json"
	"fmt"
)

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

func sortArray(arr []int) []int {
	for i := 0; i < len(arr); i++ {
		for j := i + 1; j < len(arr); j++ {
			if arr[i] > arr[j] {
				arr[i], arr[j] = arr[j], arr[i]
			}
		}
	}
	return arr
}

func main() {
	numbers := getInputUntilEOF()

	sortedNumbers := sortArray(numbers)

	//input := getInputUntilEOF()
	//fmt.Println(input)

	bst := convertArrayToBST(sortedNumbers)

	//fmt.Println("\n\n\n")

	beatifyBST(bst)

}


}
