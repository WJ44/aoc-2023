from random import choices, choice

start_graph = {}

with open("./25/input.txt", "r") as file:
    for line in file:
        vertex, neighbours = line.rstrip().split(":")
        neighbours = neighbours.split()
        if vertex not in start_graph:
            start_graph[vertex] = neighbours
        else:
            start_graph[vertex].extend(neighbours)
        for neighbour in neighbours:
            if neighbour not in start_graph:
                start_graph[neighbour] = [vertex]
            else:
                start_graph[neighbour].append(vertex)

found = False
while not found:
    graph = start_graph.copy()
    while len(graph) > 2:
        vertex = choices(list(graph.keys()), weights=[len(neighbours) for vertex, neighbours in graph.items()], k=1)[0]
        neighbour = choice(list(graph[vertex]))
        graph[neighbour] = [v for v in graph[neighbour] if v != vertex]
        graph[vertex] = [v for v in graph[vertex] if v != neighbour]
        for key in graph:
            graph[key] = [vertex + neighbour if (v == neighbour or v == vertex) else v for v in graph[key]]
        graph[vertex + neighbour] = graph[vertex].copy()
        del graph[vertex]
        graph[vertex + neighbour].extend(graph[neighbour])
        del graph[neighbour]

    count = 1
    for vertex in graph:
        if len(graph[vertex]) == 3:
            found = True
        count *= len(vertex)//3

print(count)