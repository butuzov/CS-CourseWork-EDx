package main

import (
	"fmt"
	"sync"
)

type RoundRobinBalancer struct {
	nodes    []int
	next     int
	requests chan bool
	node     chan int
	stop     chan bool
}

func (rrb *RoundRobinBalancer) Init(n int) {

	// notal nodes
	rrb.nodes = make([]int, n)
	rrb.requests = make(chan bool)
	rrb.node = make(chan int)

	go func() {
		var node int

		for range rrb.requests {
			node = rrb.next
			rrb.nodes[rrb.next]++
			rrb.next = (rrb.next + 1) % len(rrb.nodes)
			rrb.node <- node
		}
	}()

}

func (rrb *RoundRobinBalancer) GiveNode() int {
	rrb.requests <- true
	return <-rrb.node
}

func (rrb *RoundRobinBalancer) GiveStat() []int {
	return rrb.nodes
}

func (rrb *RoundRobinBalancer) Stop() {
	rrb.stop <- true
}

func main() {

	var servers int = 2
	var clients int = 2
	var requests int = 100

	balancer := new(RoundRobinBalancer)
	balancer.Init(servers)

	wg := &sync.WaitGroup{}

	for i := 0; i < clients; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			for req := 0; req < requests; req++ {
				balancer.GiveNode()
			}
		}()
	}
	wg.Wait()

	fmt.Println("Returned", balancer.GiveStat())

}
