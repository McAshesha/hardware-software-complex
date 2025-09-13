import argparse


def read_matrices_from_file(file_path):
    '''
    Читает матрицы из файла и возвращает их в виде списков списков.

    Args:
        file_path (str): Путь к файлу с матрицами

    Returns:
        tuple: Две матрицы (matrix_a, matrix_b)

    Raises:
        ValueError: Если файл содержит некорректные данные или матрицы нельзя перемножить
    '''
    with open(file_path, 'r') as file:
        lines = [line.strip() for line in file]

    # Разделяем матрицы (предполагаем, что они разделены пустой строкой)
    separator_index = None
    for i, line in enumerate(lines):
        if not line.replace(' ', '').replace('-', '').isdigit():
            separator_index = i
            break

    if separator_index is None:
        raise ValueError('Файл не содержит разделителя между матрицами')

    # Преобразуем строки в матрицы
    matrix_a = [[int(num) for num in line.split()] for line in lines[:separator_index]]
    matrix_b = [[int(num) for num in line.split()] for line in lines[separator_index + 1:]]

    # Проверяем корректность размерностей
    if not matrix_a or not matrix_b:
        raise ValueError('Одна из матриц пустая')

    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)

    # Проверяем, что все строки матрицы A имеют одинаковую длину
    for row in matrix_a:
        if len(row) != cols_a:
            raise ValueError('Несовместимые размеры строк в матрице A')

    # Проверяем, что все строки матрицы B имеют одинаковую длину
    cols_b = len(matrix_b[0])
    for row in matrix_b:
        if len(row) != cols_b:
            raise ValueError('Несовместимые размеры строк в матрице B')

    # Проверяем возможность умножения матриц
    if cols_a != rows_b:
        raise ValueError(f'Невозможно умножить матрицы: {len(matrix_a)}x{cols_a} и {rows_b}x{cols_b}')

    return matrix_a, matrix_b


def multiply_matrices(matrix_a, matrix_b):
    '''
    Перемножает две матрицы.

    Args:
        matrix_a (list): Первая матрица (m x n)
        matrix_b (list): Вторая матрица (n x p)

    Returns:
        list: Результирующая матрица (m x p)
    '''
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # Инициализируем результирующую матрицу нулями
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Выполняем умножение матриц
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def write_matrix_to_file(matrix, file_path):
    '''
    Записывает матрицу в файл.

    Args:
        matrix (list): Матрица для записи
        file_path (str): Путь к файлу для записи
    '''
    with open(file_path, 'w', encoding='utf-8') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


def main():
    '''Основная функция скрипта.'''
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default='input.txt')
    parser.add_argument('-o', '--output', type=str, default='output.txt')
    args, _ = parser.parse_known_args()

    try:
        # Читаем матрицы из файла
        matrix_a, matrix_b = read_matrices_from_file(args.input)

        # Перемножаем матрицы
        result = multiply_matrices(matrix_a, matrix_b)

        # Записываем результат в файл
        write_matrix_to_file(result, args.output)

        print(args.output)

    except Exception as e:
        print(f'Ошибка: {e}')
        exit(1)


if __name__ == '__main__':
    main()
