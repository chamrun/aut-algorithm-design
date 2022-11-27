package main

import "fmt"

func getIntInput(variable *int) {
	_, err := fmt.Scanf("%d", variable)
	if err != nil {
		fmt.Println(err)
	}
}
func getInt8Input(variable *int8) {
	_, err := fmt.Scanf("%d", variable)
	if err != nil {
		fmt.Println(err)
	}
}
func process() int {
	var n int
	var m int
	getIntInput(&n)
	getIntInput(&m)

	var lines []string

	for i := 0; i < n; i++ {
		var line string
		_, err := fmt.Scanf("%s", &line)
		if err != nil {
			return 0
		}
		lines = append(lines, line)
	}

	var allLinesAreTheSame = true

	for i := 1; i < n; i++ {
		for j := 0; j < m; j++ {
			if lines[i][j] != lines[0][j] {
				allLinesAreTheSame = false
				break
			}
		}
	}
	if allLinesAreTheSame {
		return 0
	}

	return 1
}

func main() {
	var t int8
	getInt8Input(&t)

	for i := 0; i < int(t); i++ {
		answer := process()
		fmt.Println("\nCase #", i+1, ": ", answer)
	}
}
