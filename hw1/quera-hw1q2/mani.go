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
func getLines() []string {
	var n int
	var m int
	getIntInput(&n)
	getIntInput(&m)

	var lines []string

	for i := 0; i < n; i++ {
		var line string
		_, err := fmt.Scanf("%s", &line)
		if err != nil {
			return []string{}
		}
		lines = append(lines, line)
	}

	return lines
}

func findLeastSubstringChangesToMakeAllLinesTheSame(lines []string) int {
	var answer int

	for i := 0; i < len(lines); i++ {
		var zeros int
		var ones int

		for j := len(lines[0]) - 1; j >= 0; j-- {
			if lines[i][j] == '0' {
				zeros++
			} else {
				ones++
			}
		}
		if zeros > ones {
			answer += ones
		} else {
			answer += zeros
		}
	}
	return answer
}

func main() {
	var t int8
	getInt8Input(&t)

	for i := 0; i < int(t); i++ {
		lines := getLines()
		if i == 2 {
			answer := findLeastSubstringChangesToMakeAllLinesTheSame(lines)
			fmt.Println("\nCase #", i+1, ": ", answer)
		}

		//answer := findLeastSubstringChangesToMakeAllLinesTheSame(lines)
		//fmt.Println(answer)
	}
}
