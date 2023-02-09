#!/usr/bin/env python3
# reverse.py

# Showing 3 ways to achieve the same task
def reverse_str(a):
    b = ""
    # Manually reversing a and adding each character to b
    for i in range(len(a) - 1, -1, -1):
        b += a[i]
    return b


def reverse_str2(a):
    b = ""
    # Using the reverse function to do the work and adding each character to b
    for i in reversed(range(len(a))):
        b += a[i]
    return b


def reverse_str3(a):
    b = ""
    # for character in a
    for c in a:
        # Add them to b in reverse order
        b = c + b
    return b


def main():
    s = "Forever Young"
    print(s)
    print(f"Number of characters: {len(s)}")

    print(reverse_str(s))
    print(reverse_str2(s))
    print(reverse_str3(s))

    print("".join(reversed(s)))
    print(s[::-1])


if __name__ == "__main__":
    main()
