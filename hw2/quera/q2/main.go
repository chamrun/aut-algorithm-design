


package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type condition struct {
	odd  [][]string
	even [][]string
}

func meetsConditions(conditions map[string][]map[string]bool, a, b, c, d int) bool {
	for _, condition := range conditions["odd"] {
		sumOfActs := a

		for act, _ := range condition {
			if act == "b" {
				sumOfActs += b
			} else if act == "c" {
				sumOfActs += c
			} else if act == "d" {
				sumOfActs += d
			}
		}

		if sumOfActs%2 == 0 {
			return false
		}
	}

	for _, condition := range conditions["even"] {
		sumOfActs := a

		for act, _ := range condition {
			if act == "b" {
				sumOfActs += b
			} else if act == "c" {
				sumOfActs += c
			} else if act == "d" {
				sumOfActs += d
			}
		}

		if sumOfActs%2 == 1 {
			return false
		}
	}

	return true
}

func solve(n int, abcd int, ons []int, offs []int) []string {
	conditions := map[string][]map[string]bool{
		"odd":  {},
		"even": {},
	}
	for i := 0; i < n; i++ {
		iChanged := false

		if contains(ons, i) {
			iChanged = false
		} else if contains(offs, i) {
			iChanged = true
		} else {
			continue
		}

		clicksByB := i%2 == 0
		clicksByC := !clicksByB
		clicksByD := i%3 == 0

		clicksBy := map[string]bool{}

		if clicksByB {
			clicksBy["b"] = true
		}
		if clicksByC {
			clicksBy["c"] = true
		}
		if clicksByD {
			clicksBy["d"] = true
		}

		if iChanged {
			conditions["odd"] = append(conditions["odd"], clicksBy)
		} else {
			conditions["even"] = append(conditions["even"], clicksBy)
		}
	}

	possibleStates := []string{}
	for a := 0; a <= abcd; a++ {
		for b := 0; b <= abcd-a; b++ {
			for c := 0; c <= abcd-a-b; c++ {
				d := abcd - a - b - c

				if meetsConditions(conditions, a, b, c, d) {
					act := map[string]int{
						"a": a,
						"b": b,
						"c": c,
						"d": d,
					}

					state := ""
					for i := 0; i < n; i++ {
						if contains(ons, i) {
							state += "1"
						} else if contains(offs, i) {
							state += "0"
						} else {
							clicksByA := true
							clicksByB := i%2 == 0
							clicksByC := !clicksByB
							clicksByD := i%3 == 0

							iIsOn := true

							if clicksByA && act["a"]%2 == 1 {
								iIsOn = !iIsOn
							}
							if clicksByB && act["b"]%2 == 1 {
								iIsOn = !iIsOn
							}
							if clicksByC && act["c"]%2 == 1 {
								iIsOn = !iIsOn
							}
							if clicksByD && act["d"]%2 == 1 {
								iIsOn = !iIsOn
							}

							if iIsOn {
								state += "1"
							} else {
								state += "0"
							}
						}
					}

					possibleStates = append(possibleStates, state)
				}
			}
		}
	}

	return possibleStates
}

func printAnswer(ans []string) {
	if len(ans) == 0 {
		fmt.Println("IMPOSSIBLE")
		return
	}
	ansList := sortStrings(ans)
	for _, s := range ansList {
		fmt.Println(s)
	}
}

func getInput() (int, int, []int, []int) {
	reader := bufio.NewReader(os.Stdin)

	n, _ := strconv.Atoi(readLine(reader))
	abcd, _ := strconv.Atoi(readLine(reader))

	ons := make([]int, 0)
	for _, x := range strings.Split(readLine(reader), " ") {
		i, _ := strconv.Atoi(x)
		ons = append(ons, i-1)
	}
	ons = removeInt(ons, -2)

	offs := make([]int, 0)
	for _, x := range strings.Split(readLine(reader), " ") {
		i, _ := strconv.Atoi(x)
		offs = append(offs, i-1)
	}
	offs = removeInt(offs, -2)

	return n, abcd, ons, offs
}

func readLine(reader *bufio.Reader) string {
	str, _, err := reader.ReadLine()
	if err != nil {
		return ""
	}
	return strings.TrimRight(string(str), "\r\n")
}

func sortStrings(arr []string) []string {
	sorted := make([]string, len(arr))
	copy(sorted, arr)
	sort.Strings(sorted)
	return sorted
}

func removeInt(slice []int, elem int) []int {
	for i, v := range slice {
		if v == elem {
			return append(slice[:i], slice[i+1:]...)
		}
	}
	return slice
}

func contains(slice []int, elem int) bool {
	for _, v := range slice {
		if v == elem {
			return true
		}
	}
	return false
}

func main() {
	n, abcd, ons, offs := getInput()
	ans := solve(n, abcd, ons, offs)
	printAnswer(ans)

}
