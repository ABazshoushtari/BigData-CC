import copy

n_digits = 6


def dict_extractor(graph):
    dicts = []
    for node in graph:
        dicts.append({node: graph.get(node)})

    return dicts


def initializer(graph):
    the_map = {}
    for node in graph:
        the_map.update({node: []})

    return the_map


def mapper(graph):
    print("******** MAP PHASE ********")
    maps = []
    files_info = dict_extractor(graph)
    # the_map = {}
    for f in files_info:
        print(f)
        the_map = {}
        print("MAP")
        for node in f:
            pr = graph.get(node).get("PageRank")
            adjacency_list = graph.get(node).get("AdjacencyList")
            if len(adjacency_list) != 0:
                pr = pr / len(adjacency_list)
                for neighbour in adjacency_list:
                    if neighbour not in the_map:
                        the_map.update({neighbour: 0.0})
                    the_map[neighbour] += pr

                    print(the_map)

            print(f"*OUTPUT OF MAP:\n{the_map}")
            print("-------------")

        maps.append(the_map)

    return maps


def shuffle(map_phase_output):
    shuffled = {}
    for output in map_phase_output:
        for node in output:
            if node not in shuffled:
                shuffled[node] = []
            shuffled[node].append(output.get(node))

    return shuffled


def reducer(shuffled, damping_factor=0.85):  # damping factor is alpha
    # reduced = {}
    # for output in map_phase_output:
    #     for node in output:
    #         print("REDUCE")
    #         if node not in reduced:
    #             reduced[node] = 0.0
    #         reduced[node] += output.get(node)
    #
    #         print(f"node {node}: {reduced[node]}")
    #         print(reduced)
    #         print("-------------")
    #
    # print(f"*FINAL OUTPUT OF REDUCE:\n{reduced}")
    # return reduced
    print("******** REDUCE PHASE ********")
    num_nodes = 1
    # num_nodes = len(shuffled)
    # print(num_nodes)
    reduced = {}
    for node in shuffled:
        print("REDUCE")
        reduced_value = 0.0
        for value in shuffled.get(node):
            reduced_value += value

        reduced[node] = (1 - damping_factor) / num_nodes + damping_factor * round(reduced_value, n_digits)

        print(f"node {node}: {reduced[node]}")
        print(reduced)
        print("-------------")

    print(f"*FINAL OUTPUT OF REDUCE:\n{reduced}")
    return reduced


def update_graph(old_graph, reduce_output_phase):
    updated_graph = copy.deepcopy(old_graph)
    for output in reduce_output_phase:
        updated_graph[output]["PageRank"] = reduce_output_phase.get(output)

    return updated_graph


if __name__ == "__main__":
    graph = {
        "A": {"PageRank": 1.0, "AdjacencyList": ["B", "C"]},
        "B": {"PageRank": 0.5, "AdjacencyList": ["A"]},
        "C": {"PageRank": 0.5, "AdjacencyList": []}
    }

    iteration = 1

    while True:
        print(f"<ITERATION {iteration}>")
        map_output_phase = mapper(graph)
        # print(map_output_phase)
        shuffled = shuffle(map_output_phase)
        # print(shuffled)
        print()
        reduce_output_phase = reducer(shuffled)
        updated_graph = update_graph(graph, reduce_output_phase)
        # print(graph)
        # print(updated_graph)
        if updated_graph == graph:
            print("\nCONVERGED")
            print(updated_graph)
            break

        print()
        graph = updated_graph
        print(f"FINAL OUTPUT OF ITERATION {iteration}:\n{graph}\n")
        iteration += 1
