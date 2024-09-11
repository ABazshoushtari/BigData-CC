import json
from collections import defaultdict


def mapper(graph):
    map_output = []
    for node, value in graph.items():
        map_output.append((node, value))

        if value['Distance'] != float('inf'):
            for adjacent_node, weight in value.get('AdjacencyList', {}).items():
                new_distance = value['Distance'] + weight
                new_path = value['Path'] + [adjacent_node]
                map_output.append((adjacent_node, {'Distance': new_distance, 'Path': new_path}))
    return map_output


def reducer(map_output):
    # somehow shuffling
    grouped_data = defaultdict(list)
    for key, value in map_output:
        grouped_data[key].append(value)

    # print(grouped_data)
    # print(grouped_data.items())

    reduced_output = {}
    for node, values in grouped_data.items():
        min_distance, min_path = min(
            ((value['Distance'], value.get('Path', [node])) for value in values if 'Distance' in value),
            key=lambda x: x[0]
        )
        adjacency_list = next((value['AdjacencyList'] for value in values if 'AdjacencyList' in value), {})
        reduced_output[node] = {'Distance': min_distance, 'Path': min_path, 'AdjacencyList': adjacency_list}
    return reduced_output


def map_reduce(graph):
    iteration = 1
    previous_graph = None
    current_graph = graph

    # Initialize paths
    for node in current_graph:
        current_graph[node]['Path'] = [node]

    while current_graph != previous_graph:
        print(f"Iteration {iteration} - Map Phase Output:")
        map_output = mapper(current_graph)
        for output in map_output:
            print(f"  {output[0]}: {json.dumps(output[1])}")

        print(f"Iteration {iteration} - Reduce Phase Output:")
        previous_graph = current_graph
        current_graph = reducer(map_output)
        for node, value in current_graph.items():
            print(f"  {node}: {json.dumps(value)}")

        iteration += 1

    return current_graph


if __name__ == "__main__":
    graph = {
        "A": {"Distance": 0, "AdjacencyList": {"B": 10, "C": 5}},
        "B": {"Distance": float('inf'), "AdjacencyList": {"C": 2, "D": 1}},
        "C": {"Distance": float('inf'), "AdjacencyList": {"E": 2, "B": 3, "D": 9}},
        "D": {"Distance": float('inf'), "AdjacencyList": {"E": 4}},
        "E": {"Distance": float('inf'), "AdjacencyList": {"A": 7, "D": 6}}
    }

    # graph = {
    #     'A': {"Distance": 0, "AdjacencyList": {'B': 3, 'C': 2}},
    #     'B': {"Distance": float('inf'), "AdjacencyList": {'A': 3, 'C': 7, 'D': 2}},
    #     'C': {"Distance": float('inf'), "AdjacencyList": {'A': 2, 'B': 7, 'D': 1}},
    #     'D': {"Distance": float('inf'), "AdjacencyList": {'B': 2, 'C': 1}}
    # }

    final_result = map_reduce(graph)
    print("\nFinal Result (Shortest Paths and Distances):")
    for node, value in final_result.items():
        print(f"Node {node}: Distance = {value['Distance']}, Path = {' -> '.join(value['Path'])}")
