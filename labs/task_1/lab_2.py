import argparse

def generate_pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

def format_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))
    formatted = []
    for row in triangle:
        str_row = ' '.join(map(str, row))
        formatted.append(str_row.center(max_width))
    return formatted

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N', type=int, default=10)
    args, _ = parser.parse_known_args()

    triangle = generate_pascal_triangle(args.N)
    formatted = format_triangle(triangle)

    for line in formatted:
        print(line)

if __name__ == '__main__':
    main()
