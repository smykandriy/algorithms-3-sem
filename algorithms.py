import ast

DIRECTION_VECTOR_ROW = [-1, 0, 1, 0]
DIRECTION_VECTOR_COLUMN = [0, 1, 0, -1]


def are_coords_valid_for_matrix(matrix: list[list], color: str, x: int, y: int):
    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
        return matrix[x][y] == color
    return False


def are_coords_valid_for_graph(graph: dict, visited: list, x: int, y: int, color: str = None):
    if (x, y) not in visited and (x, y) in graph.keys():
        if color is None:
            return True
        return graph[(x, y)][0] == color
    return False


def convert_file_to_args(input_file: str):
    with open(input_file, "r") as f:
        lines = f.readlines()
        size = tuple(map(int, lines[0].strip().split(",")))
        start = tuple(map(lambda x: int(x) - 1, lines[1].strip().split(",")))
        color = lines[2].strip().replace("'", "")
        colors = [ast.literal_eval(row) for row in lines[3:]]
        graph = {}

        for row_index in range(len(colors)):
            for column_index in range(len(colors[row_index])):
                current_color = colors[row_index][column_index]
                graph[(row_index, column_index)] = [current_color]
                for index in range(4):
                    x_neighbour = DIRECTION_VECTOR_ROW[index] + row_index
                    y_neighbour = DIRECTION_VECTOR_COLUMN[index] + column_index
                    if are_coords_valid_for_matrix(colors, current_color, x_neighbour, y_neighbour):
                        graph[(row_index, column_index)].append((x_neighbour, y_neighbour))

        return size, start, color, graph


def save_graph_to_file_as_matrix(size: tuple[int, int], graph: dict, output_file: str):
    rows, cols = size
    matrix = [["" for _ in range(cols)] for _ in range(rows)]

    for (x, y), value in graph.items():
        matrix[x][y] = value[0]

    with open(output_file, 'w') as file:
        for row in matrix:
            file.write(str(row) + ",\n")


def flood_fill(size: tuple[int, int], start: tuple[int, int], color: str, graph: dict):
    visited = [start]
    queue = [start]
    graph[start][0] = color

    while queue:
        row_index, column_index = queue.pop(0)
        for x, y in graph[(row_index, column_index)][1:]:
            if are_coords_valid_for_graph(graph, visited, x, y):
                for index in range(4):
                    x_neighbour = DIRECTION_VECTOR_ROW[index] + x
                    y_neighbour = DIRECTION_VECTOR_COLUMN[index] + y
                    if are_coords_valid_for_graph(graph, visited, x_neighbour, y_neighbour, color):
                        graph[(x, y)].append((x_neighbour, y_neighbour))
                        graph[(x_neighbour, y_neighbour)].append((x, y))
                        visited.append((x_neighbour, y_neighbour))
                graph[(x, y)][0] = color
                queue.append((x, y))
                visited.append((x, y))

    return save_graph_to_file_as_matrix(size, graph, "output.txt")


flood_fill(*convert_file_to_args("input.txt"))
