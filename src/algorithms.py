from itertools import combinations


def convert_args_to_graph(file_path: str = "../input_6_workers.txt"):
    with open(file_path, "r") as file:
        lines = file.readlines()

    size = tuple(map(int, lines[0].strip().split()))
    input_list = tuple(map(str, lines[1].strip().split()))
    workers_count, b = size

    if 0 <= workers_count <= 50 and 0 <= b <= 50:
        graph = dict()
        for i in range(b):
            graph[i] = list()
            for answer_index in range(len(input_list)):
                if input_list[answer_index][i] == "Y":
                    graph[i].append(answer_index)

        return graph, workers_count
    return -1


def write_output_to_file(file_path: str, result: int):
    with open(file_path, "w") as file:
        file.write(str(result))


def generate_combinations_from_integers_tuple(
    tuple_of_integers: tuple[int] = (0, 1, 2), combination_length: int = 2
):
    return list(combinations(tuple_of_integers, combination_length))


def get_minimum_beer_types_amount(beers_graph: dict, workers_count: int):
    result, index = -1, 1
    queue = [
        generate_combinations_from_integers_tuple(tuple(beers_graph.keys()), i + 1)
        for i in range(len(beers_graph.keys()))
    ]

    while queue:
        combinations = queue.pop(0)
        workers = set()
        for combination in combinations:
            for index in combination:
                workers.update(beers_graph[index])
            if len(workers) == workers_count:
                result = len(combination)
                queue.clear()
                break
            workers.clear()

    return result


graph, workers_count = convert_args_to_graph()

for key, value in graph.items():
    print(key, value)

result = get_minimum_beer_types_amount(graph, workers_count)
write_output_to_file("../output.txt", result)
