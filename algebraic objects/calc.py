def lcm(x: int, y: int):
    largest = max(x, y)
    candidate = largest
    while candidate%x != 0 or candidate%y != 0:
        candidate += largest
    return candidate
