"""Example implementing a list utility function."""

# Function name: contains
# We have 2 parameters: needle (str), haystack (list[str])
# Return type bool
def contains(needle: str, haystack: list[str]) -> bool:
    i: int = 0
    while i < len(haystack):
        if haystack[i] == needle:
        # We found it! No more work to do!
            return True
        i += 1
    return False