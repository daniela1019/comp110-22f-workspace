"""Example of writing a test subject."""
# Part of LS16 notes

def sum(xs: list[float]) -> float:
    """Complete the sum of a list."""
    total: float = 0.0
    for x in xs:
        total += x
    # Below is the same thing as the for..in loop, just as a while loop
    # i: int = 0
    # while i < len(xs):
    #     total += xs[i]
    #     i += 1
    return total