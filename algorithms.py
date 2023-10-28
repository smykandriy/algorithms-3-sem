import ast


def convert_file_to_args(input_file):
    with open(input_file, "r") as f:
        lines = f.readlines()
        size = tuple(map(int, lines[0].strip().split(",")))
        start = list(map(int, lines[1].strip().split(",")))
        start[0] -= 1
        start[1] -= 1
        color = lines[2].strip().replace("'", "")
        colors = [ast.literal_eval(row) for row in lines[3:]]
    return size, tuple(start), color, colors


def write_to_output_file(output_file, colored_array):
    with open(output_file, "w") as file:
        for row in colored_array:
            quoted_row = [f'"{element}"' for element in row]
            file.write("[" + ", ".join(quoted_row) + "],\n")


def is_coords_valid(
    array: list[list],
    visited: list[tuple],
    color: str,
    x: int,
    y: int,
):
    if (x, y) not in visited:
        if 0 <= x < len(array) and 0 <= y < len(array[x]):
            return array[x][y] is color
    return False


def flood_fill(size: tuple[int, int], start: tuple[int, int], color: str, colors):
    visited = queue = []
    direction_vector_row = [-1, 0, 1, 0]
    direction_vector_column = [0, 1, 0, -1]
    row_index, column_index = start

    current_color = colors[row_index][column_index]
    colors[row_index][column_index] = color
    visited.append(start)
    queue.append(start)

    while queue:
        row_index, column_index = queue.pop(0)

        for index in range(4):
            x_neighbour = direction_vector_row[index] + row_index
            y_neighbour = direction_vector_column[index] + column_index
            if is_coords_valid(
                colors, visited, current_color, x_neighbour, y_neighbour
            ):
                colors[x_neighbour][y_neighbour] = color
                queue.append((x_neighbour, y_neighbour))
                visited.append((x_neighbour, y_neighbour))

    return write_to_output_file("output.txt", colors)


flood_fill(*convert_file_to_args("input.txt"))
