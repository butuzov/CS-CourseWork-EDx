package main

import (
	"reflect"
)

func showMeTheType(i interface{}) string {
	return reflect.TypeOf(i).String()
}

func main() {}
