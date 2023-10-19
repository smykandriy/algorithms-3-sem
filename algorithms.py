def get_max_objects_in_the_area(desk_length: int, width: int, height: int):
    objects_per_row = desk_length // width
    max_rows = desk_length // height
    return objects_per_row * max_rows


def get_min_desk_length(n: int, width: int, height: int):
    if all([
        1 <= n <= 1012,
        1 <= width <= 109,
        1 <= height <= 109,
    ]):
        min_desk_length = 1
        desk_length = height * n if height >= width else width * n

        while min_desk_length < desk_length:
            mid = (desk_length + min_desk_length) // 2

            if get_max_objects_in_the_area(mid, width, height) >= n:
                desk_length = mid
                continue
            min_desk_length = mid + 1

        return min_desk_length
    return -1


def can_store(sections: list[int], distance: int, n, c) -> bool:
    count = 1
    prev = sections[0]

    for current_section in range(1, n):
        current = sections[current_section]

        if current - prev >= distance:
            prev = current
            count += 1

    if count >= c:
        return True
    return False


def get_min_distance_between_cows(n: int = 5, c: int = 3, free_sections=None) -> int:
    result = -1
    if all([
        2 <= n <= 100000,
        2 <= c <= n
    ]):
        if free_sections is None:
            free_sections = [1, 2, 8, 4, 9]
        sorted_sections = sorted(free_sections)

        min_distance = 1
        max_distance = sorted_sections[-1] - sorted_sections[0]

        while min_distance <= max_distance:
            mid = min_distance + (max_distance - min_distance) // 2

            if can_store(sorted_sections, mid, n, c):
                result = mid
                min_distance = mid + 1
                continue
            max_distance = mid - 1
    return result

