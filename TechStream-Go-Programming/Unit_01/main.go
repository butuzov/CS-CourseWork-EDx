package main

import (
	"bytes"
	"sort"
	"strconv"
)

func ReturnInt() int {
	return int(1)
}

func ReturnFloat() float32 {
	return float32(1.1)
}

func ReturnIntArray() [3]int {
	i := [3]int{1, 3, 4}
	return i
}

func ReturnIntSlice() []int {
	i := []int{1, 2, 3}
	return i
}

func IntSliceToString(nums []int) string {
	var buffer []byte
	var b = bytes.NewBuffer(buffer)
	for _, n := range nums {
		b.WriteString(strconv.Itoa(n))
	}
	return b.String()
}

func MergeSlices(floats []float32, ints []int32) []int {
	var nums []int = make([]int, len(floats)+len(ints))
	for i, nf := range floats {
		nums[i] = int(nf)
	}
	for i, ni := range ints {
		nums[i+len(floats)] = int(ni)
	}

	return nums
}

func GetMapValuesSortedByKey(in map[int]string) []string {
	var out []string = make([]string, len(in))
	var indeces []int

	for i, _ := range in {
		indeces = append(indeces, i)
	}

	sort.Ints(indeces)
	for i, iS := range indeces {
		out[i] = in[iS]
	}
	return out
}

func main() {}
