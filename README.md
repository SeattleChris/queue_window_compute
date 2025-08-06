# queue_window_compute

Consider an `n`-integer sequence, `A`. We perform a query on `A` with an integer, `d` representing the size of (overlapping) subsequences of `A`. Each subsequent `d`-sized subsequence starts one index position higher than the previous subsequence. Determine the maximum for each `d` length subsequence, and then the minimum value of that collection of maximums is the result for that particular query. For a given `A` sequence, there will be one or more queries to perform. So the expected result is a sequence of solutions (1 for each query).

## Function Description

Parameters:

* int arr[n]: an array of integers
* int queries[q]: the lengths of subsequences to query

Returns:

* int[q]: the answers to each query

## Constraints

* 1 <= n <= 10^5
* 0 <= arr[i] <= 10^6
* 1 <= q <= 100
* 1 <= d <= n
