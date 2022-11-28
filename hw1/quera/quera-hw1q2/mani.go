package main

import (
	"fmt"
)

func getIntInput(variable *int) {
	_, err := fmt.Scanf("%d", variable)
	if err != nil {
		//pn(err)
	}
}
func getInt8Input(variable *int8) {
	_, err := fmt.Scanf("%d", variable)
	if err != nil {
		//pn(err)
	}
}
func getLines() [][]rune {
	var n int
	var m int
	getIntInput(&n)
	getIntInput(&m)

	var lines [][]rune

	for i := 0; i < n; i++ {
		var line string
		_, err := fmt.Scanf("%s", &line)
		if err != nil {
			return [][]rune{}
		}

		lineChars := []rune(line)
		lines = append(lines, lineChars)
	}

	return lines
}

//func pn(s any) {
//	//fmt.Println(s)
//}

func findLeastSubstringChangesToMakeAllLinesTheSame(lines [][]rune) int {
	answer := 0

	for j := len(lines[0]) - 1; j >= 0; j-- {
		//pn("current answer: ")
		//pn(answer)
		printState(lines)
		var zeros int
		var ones int

		for i := 0; i < len(lines); i++ {
			if lines[i][j] == '0' {
				zeros++
			} else {
				ones++
			}
		}
		var onesAreLess bool
		if ones < zeros {
			onesAreLess = true
			answer += ones
		} else {
			onesAreLess = false
			answer += zeros
		}

		for i := 0; i < len(lines); i++ {
			if lines[i][j] == '1' && onesAreLess {
				for k := 0; k <= j; k++ {
					if lines[i][k] == '0' {
						lines[i][k] = '1'
					} else if lines[i][k] == '1' {
						lines[i][k] = '0'
					}
				}
			} else if lines[i][j] == '0' && !onesAreLess {
				for k := 0; k <= j; k++ {
					if lines[i][k] == '0' {
						lines[i][k] = '1'
					} else if lines[i][k] == '1' {
						lines[i][k] = '0'
					}
				}
			}
		}
	}
	//pn("final answer: ")
	//pn(answer)
	//pn("\n\n-------------\n\n")
	return answer
}

func printState(lines [][]rune) {
	//pn("\nState: ")
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[0]); j++ {
			//fmt.Print(string(lines[i][j]))
		}
		//pn("")
	}
	//pn("")

}

func main() {
	var t int8
	getInt8Input(&t)

	for i := 0; i < int(t); i++ {
		lines := getLines()
		//if i == 2 {
		answer := findLeastSubstringChangesToMakeAllLinesTheSame(lines)
		//pn("\nCase #", i+1, ": ", answer)
		//}

		//answer := findLeastSubstringChangesToMakeAllLinesTheSame(lines)
		fmt.Println(answer)
	}
}
