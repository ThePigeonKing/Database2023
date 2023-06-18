#!/bin/bash

# cdecl
echo -e  "--- CDECL ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/cdecl

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

# cdecl_o3
echo -e  "--- CDECL_O3 ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/cdecl

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

# stdcall
echo -e  "--- STDCALL ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/stdcall

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

# stdcall_o3
echo -e  "--- STDCALL_O3 ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/stdcall_o3

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

: '
# fastcall
echo -e  "--- FASTCALL ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/fastcall

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"

# fastcall_o3
echo -e  "--- FASTCALL_O3 ---"
total_time=0

for ((i=1; i<=10; i++))
do
    start_time=$(date +%s.%N)

    ../binary/fastcall_o3

    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc -l)

    total_time=$(echo "$total_time + $execution_time" | bc -l)
done

average_time=$(echo "scale=4; $total_time / 10" | bc -l)
echo "Average execution time: $average_time seconds"
'
