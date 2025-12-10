#!/usr/bin/env python3
import sys

def distance(box1, box2):
    return (box1[0] - box2[0]) ** 2 + (box1[1] - box2[1]) ** 2 + (box1[2] - box2[2]) ** 2

def main():
    print("input > ", flush=True)  # Indicate input reading
    input_data = sys.stdin.read().strip().split("\n")
    junction_boxes = [tuple(map(int, line.split(","))) for line in input_data]

    # Step 2: Create edges and sort by distance
    edges = []
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            dist = distance(junction_boxes[i], junction_boxes[j])
            edges.append((dist, i, j))
    edges.sort()

    # Step 3: Create an array of sets for circuits
    circuits = [set([i]) for i in range(len(junction_boxes))]

    # Step 4-6: Process edges to form 10 connections
    for step, (dist, i, j) in enumerate(edges):
        # Find the circuits containing i and j
        circuit_i = next((c for c in circuits if i in c), None)
        circuit_j = next((c for c in circuits if j in c), None)

        if circuit_i is not circuit_j:
            circuit_i.update(circuit_j)
            circuits.remove(circuit_j)
        
        if step == 999:
            # Calculate the product of the sizes of the three largest circuits
            largest_circuits = sorted([len(c) for c in circuits], reverse=True)
            result = largest_circuits[0] * largest_circuits[1] * largest_circuits[2]
            print(result)

        if len(circuits) == 1:
            print(junction_boxes[i][0] * junction_boxes[j][0])
            break


if __name__ == "__main__":
    main()