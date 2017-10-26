'''
page 13
Example1.3:Tower of Hanoi
'''

def tower_of_hanoi(n, source, aux, destion):
    if n <= 0:
        return
    tower_of_hanoi(n-1, source, destion, aux)
    print("move %d from %s to %s" % (n, source, destion))
    tower_of_hanoi(n-1, aux, source, destion)


if __name__ == "__main__":
    tower_of_hanoi(2, "s", "a", "d")
