package main

import (
	"fmt"
	"time"
)

type Calendar struct {
	time time.Time
}

func NewCalendar(t time.Time) Calendar {
	return Calendar{
		time: t,
	}
}

func (c Calendar) CurrentQuarter() int {
	switch c.time.Month() {
	case time.January, time.February, time.March:
		return 1
	case time.April, time.May, time.June:
		return 2
	case time.July, time.August, time.September:
		return 3
	default:
		return 4
	}
}

func main() {

	parsed, _ := time.Parse("2006-01-02", "2018-01-12")
	calendar := NewCalendar(parsed)

	fmt.Printf("%#v\n", calendar)

	fmt.Printf("%d\n", calendar.CurrentQuarter())

}
