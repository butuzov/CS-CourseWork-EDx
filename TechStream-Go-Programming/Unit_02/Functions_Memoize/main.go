package main

import (
	"bytes"
	"fmt"
	"strings"
)

// Types definitions in this code changed, for a reason
// mail.ru team just copy-paste Mark Summerfield code
// (which also isn't perfect) with no clear reason to use
// second (variadic argument for memoization funtion).

type memoizeFunction func(int) interface{}

var fibonacci memoizeFunction
var romanForDecimal memoizeFunction

func memoize(function memoizeFunction) memoizeFunction {

	mapa := make(map[int]interface{})

	return func(n int) interface{} {

		// Cache look up
		if value, ok := mapa[n]; ok == true {
			return value
		}

		// Executing callback and putting it cache
		mapa[n] = function(n)
		return mapa[n]
	}
}

// TODO обернуть функции fibonacci и roman в memoize

func init() {

	// Fibonachi memoizer (Actually Classic recursive Fibonacci)
	fibonacci = memoize(func(n int) interface{} {
		if n < 2 {
			return 1
		}
		return fibonacci(n-1).(int) + fibonacci(n-2).(int)
	})

	// romansFOrDecimal written in way to be recursive.
	romanForDecimal = memoize(func(n int) interface{} {
		if n <= 0 || n > 3999 {
			panic("Not supported")
		}

		var buffer bytes.Buffer

		switch n {
		case 1:
			buffer.WriteByte('I')
		case 5:
			buffer.WriteByte('V')
		case 10:
			buffer.WriteByte('X')
		case 50:
			buffer.WriteByte('L')
		case 100:
			buffer.WriteByte('C')
		case 500:
			buffer.WriteByte('D')
		case 1000:
			buffer.WriteByte('M')
		default:
			// magic here
			for grade := 1000; grade > 0; grade /= 10 {
				var step = n / grade

				switch step {
				case 1, 2, 3, 4:
					buffer.WriteString(strings.Repeat(romanForDecimal(grade).(string), step))
				case 6, 7, 8:

					buffer.WriteString(romanForDecimal(5 * grade).(string))
					buffer.WriteString(strings.Repeat(romanForDecimal(grade).(string), step-5))
				case 9:
					buffer.WriteString(romanForDecimal(grade).(string))
					buffer.WriteString(romanForDecimal(step + 1).(string))
				}

				n = n % grade
			}
		}

		return buffer.String()
	})
}

func main() {

	fmt.Println("Fibonacci(45) =", fibonacci(45).(int))

	romans := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
		14, 15, 16, 17, 18, 19, 20, 25, 30, 40, 50, 60, 69, 70, 80,
		90, 99, 100, 200, 300, 400, 500, 600, 666, 700, 800, 900,
		1000, 1009, 1444, 1666, 1945, 1997, 1999, 2000, 2008, 2010,
		2012, 2500, 3000, 3999}

	for _, x := range romans {
		fmt.Printf("%4d = %s\n", x, romanForDecimal(x).(string))
	}
}
