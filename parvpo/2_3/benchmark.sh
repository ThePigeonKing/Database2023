#!/bin/bash

# pointer
echo -e  "--- POINTER ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ./pointer

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

# nopointer
echo -e  "--- NOPOINTER ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ./nopointer

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

