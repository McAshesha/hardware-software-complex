import argparse


def read_matrices_from_file(file_path):
    '''
    Читает матрицы из файла и возвращает их в виде списков списков.

    Args:
        file_path (str): Путь к файлу с матрицами

    Returns:
        tuple: Две матрицы (matrix, kernel)

    Raises:
        ValueError: Если файл содержит некорректные данные или ядро больше матрицы
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
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
    matrix = [[int(num) for num in line.split()] for line in lines[:separator_index]]
    kernel = [[int(num) for num in line.split()] for line in lines[separator_index + 1:]]

    # Проверяем корректность размерностей
    if not matrix or not kernel:
        raise ValueError('Одна из матриц пустая')

    # Проверяем, что все строки матрицы имеют одинаковую длину
    matrix_cols = len(matrix[0])
    for row in matrix:
        if len(row) != matrix_cols:
            raise ValueError('Несовместимые размеры строк в матрице')

    # Проверяем, что все строки ядра имеют одинаковую длину
    kernel_cols = len(kernel[0])
    for row in kernel:
        if len(row) != kernel_cols:
            raise ValueError('Несовместимые размеры строк в ядре')

    # Проверяем, что ядро не больше матрицы
    if len(kernel) > len(matrix) or len(kernel[0]) > len(matrix[0]):
        raise ValueError('Ядро свертки не может быть больше матрицы')

    return matrix, kernel


def convolve(matrix, kernel):
    '''
    Выполняет операцию свёртки матрицы с ядром.

    Args:
        matrix (list): Исходная матрица
        kernel (list): Ядро свёртки

    Returns:
        list: Результирующая матрица после свёртки
    '''
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    kernel_rows = len(kernel)
    kernel_cols = len(kernel[0])

    # Вычисляем размеры результирующей матрицы
    result_rows = matrix_rows - kernel_rows + 1
    result_cols = matrix_cols - kernel_cols + 1

    # Инициализируем результирующую матрицу нулями
    result = [[0 for _ in range(result_cols)] for _ in range(result_rows)]

    # Выполняем свёртку
    for i in range(result_rows):
        for j in range(result_cols):
            total = 0
            for k in range(kernel_rows):
                for l in range(kernel_cols):
                    total += matrix[i + k][j + l] * kernel[k][l]
            result[i][j] = total

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
        # Читаем матрицу и ядро из файла
        matrix, kernel = read_matrices_from_file(args.input)

        # Выполняем свёртку
        result = convolve(matrix, kernel)

        # Записываем результат в файл
        write_matrix_to_file(result, args.output)

        print(args.output)

    except Exception as e:
        print(f'Ошибка: {e}')
        exit(1)


if __name__ == '__main__':
    main()
