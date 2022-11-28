package main

import (
	"encoding/json"
	"fmt"
	"strings"
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

	printBSTLevelByLevel(bst)

}

func printBSTLevelByLevel(bst *Node) {
	if bst == nil {
		return
	}

	var values []int

	queue := []*Node{bst}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		values = append(values, node.value)
		if node.left != nil {
			queue = append(queue, node.left)
		}
		if node.right != nil {
			queue = append(queue, node.right)
		}
	}
	answer, _ := json.Marshal(values)
	finalStr := strings.ReplaceAll(string(answer), ",", ", ")

	fmt.Printf("%v", finalStr)

}
