def compute_lps(needle: str) -> list[int] | int:
    if needle:
        lps = [0] * len(needle)
        prev_lps = 0
        index = 1

        while index < len(needle):
            if needle[index] == needle[prev_lps]:
                prev_lps += 1
                lps[index] = prev_lps
                index += 1
            elif prev_lps == 0:
                lps[index] = 0
                index += 1
            else:
                prev_lps = lps[prev_lps - 1]

        return lps
    return 0


def kmp_search(
    haystack: str = "ABABABBABBAAB", needle: str = "BAAB"
) -> list[tuple[int, int]]:
    if needle == "":
        return [(0, 0)]

    lps = compute_lps(needle)
    i = j = 0
    result = []
    needle_length = len(needle)

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]

        if j == needle_length:
            result.append((i - needle_length, i))
            j = 0

    return result if result else [(-1, -1)]
