package main

import "fmt"

func getInt8Input(variable *int8) {
	_, err := fmt.Scanf("%d", variable)
	if err != nil {
		fmt.Println("Error: ", err)
	}
}

func findAllPrimeNumbersWithNDigits(n int8) {
	var primes []int
	for i := 1; i < n; i++ {
		primes = append(primes, i)
	}
	return primes

}

func main() {
	var n int8
	getInt8Input(&n)
	primes = findAllPrimeNumbersWithNDigits(n)
}
