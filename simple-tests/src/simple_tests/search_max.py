# На вход подается строка вида '10 3 2 500 0 8'
# надо найти максимальное число в этой строке


def search_max(s: str) -> int:
    x = [int(i) for i in s.split()]
    m = x[0]
    for i in x[1:]:
        if i > m:
            m = i
    return m
