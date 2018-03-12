package main

import (
	"fmt"
	"sync"
)

type job func(in, out chan interface{})

func Pipe(funcs ...job) {

	var wg sync.WaitGroup
	wg.Add(len(funcs))

	in := make(chan interface{})
	out := make(chan interface{})
	for i, f := range funcs {

		go func(wg *sync.WaitGroup, f job, in, out chan interface{}) {
			f(in, out)
			wg.Done()
			close(out)
		}(&wg, f, in, out)

		if i+1 != len(funcs) {
			in = out
			out = make(chan interface{})
		}

	}

	wg.Wait()

}

func main() {
	res := []interface{}{}

	case1 := []job{
		job(func(in, out chan interface{}) {
			for i := 0; i < 10; i++ {
				out <- i
			}
		}),

		job(func(in, out chan interface{}) {
			for i := range in {
				if s, ok := i.(int); ok && (s%3 == 0) {
					out <- i
				}
			}
		}),

		job(func(in, out chan interface{}) {
			for value := range in {
				out <- interface{}(value.(int) * 10)
			}
		}),

		job(func(in, out chan interface{}) {
			for val := range in {
				res = append(res, val)
			}
		}),
	}
	Pipe(case1...)

	fmt.Printf("%v\n", res)

}
