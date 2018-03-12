package main

import (
	"fmt"
	"math"
	"unsafe"
)

// TODO: DO a Square Root calculation using Newton algorithm
// But, do not use `math` package

// Sqrt - calculate Sqrt using Newton algorithm.
func Sqrt(x float64) float64 {

	if x < 0 {
		// thanks for forbiding using math.
		// I was just going to use math.NaN()
		var b uint64 = 0x7FF8000000000001
		return *(*float64)(unsafe.Pointer(&b))

	} else if x == 0 {
		return 0
	}

	var sqrtN0 float64 = .00001
	var sqrtN1 float64 = sqrtN0

	for {
		sqrtN1 = (sqrtN0 + x/sqrtN0) * .5
		if sqrtN0 == sqrtN1 {
			break
		}
		sqrtN0 = sqrtN1
	}

	return sqrtN0
}

func main() {
	fmt.Println(math.Sqrt(0))
	fmt.Println(Sqrt(0))
}
