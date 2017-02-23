## Problem Set 3 - Find (less comfortable)

### Problem Detailed Information
[Problem Set 3 - Find (less comfortable) at cs50.net](http://docs.cs50.net/problems/find/less/find.html)

### Specification
Complete the implementation of `find` by completing the implementation of `search` and `sort` in `helpers.c`.

`search`

  * Your implementation must return `false` immediately if n is non-positive.
  * Your implementation must return `true` if value is in `values` and `false` if `value` is not in `values`.
  * The running time of your implementation must be in _O_(log _n_).
  * You may not alter the function’s declaration. Its prototype must remain:

```c
    bool search(int value, int values[], int n);
```


`sort`

  * Your implemenation must sort, from smallest to largest, the array of numbers that it’s  passed.
  * The running time of your implementation must be in _O_(_n²_), where _n_ is the array’s size.
  * You may not alter the function’s declaration. Its prototype must remain:

```c
    void sort( int values[], int n );
```


## Solution.
 Implement `search` using [Binary search](https://en.wikipedia.org/wiki/Binary_search_algorithm) algoritm and `sort` using [Bubble](https://en.wikipedia.org/wiki/Bubble_sort) sort.

## Testing
	./generate 1000 50 | ./find 127

## CS50x Testing
	check50 2016.find.less helpers.c
