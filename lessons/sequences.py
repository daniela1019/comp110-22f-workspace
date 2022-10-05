"""Examples of the tuple and range sequences."""

# An example of a tuple without type aliasing
goat: tuple[str, int] = ("MJ", 23)

# Tuples are sequences, so they are 0-indexed
print(goat[0])
print(goat[1])

# Sequences have lengths
print(len(goat))

# Sequences are iterable with for...in loops
# Meaning you can loop over them
for item in goat:
    print(item)

# Tuples, unlike lists, are immutable
# Which means we cannot reassign items, nor append, nor pop...
# Ex. goat[0] = "LBJ" is not allowed
Player = tuple[str, int]

# Once we've aliased a type, we can create variables of that type
unc_poy: Player = ("Bacot", 5)

# In a strange works, where jersey number changes...
unc_poy = (unc_poy[0], unc_poy[1] + 1)
 

# A range is another common sequence type
# (start, stop, step)
# The step is an optional argument; if you don't include it, the step will automatically be 1
# The default start for ranges is often 0, so if you write range(stop), the step of 1 and start of zero will be implied
zero_to_nine: range = range(0, 10, 1)

# We can access items of the range
print(zero_to_nine[0])
print(zero_to_nine[9])

for i in zero_to_nine:
    print(i)

# We can have different steps for more control
odds_to_99: range = range(1, 100, 2)
for i in odds_to_99:
    print(i)


# Prints out index of every name along with the name
names: list[str] = ["Kris", "Alyssa", "Michael", "Lebron"]
for i in range(len(names)):
    print(f"{i}. {names[i]}")


# Prints out every othre name and index
for i in range(0, len(names), 2):
    print(f"{i}. {names[i]}")

# Prints end value for the given range
print(odds_to_99.stop)