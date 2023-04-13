import itertools


def land_perimeter(arr):
    shifts = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    return f"Total land perimeter: {sum(4 for i, j in itertools.product(range(len(arr)), range(len(arr[0]))) if arr[i][j] == 'X') - sum(1 for i, j in itertools.product(range(len(arr)), range(len(arr[0]))) if arr[i][j] == 'X' for x, y in shifts if 0 <= i + x < len(arr) and 0 <= j + y < len(arr[0]) and arr[i+x][j+y] == 'X')}"
