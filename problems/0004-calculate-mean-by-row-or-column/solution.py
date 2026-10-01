def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	result = []
	row = len(matrix)
	column = len(matrix[0])
	if mode == 'row':
		for i in range(row):
			sum_row = 0
			for j in range(column):
				sum_row += matrix[i][j]
			result.append(sum_row/column)

	if mode == 'column':
		for j in range(column):
			sum_column = 0
			for i in range(row):
				sum_column += matrix[i][j]
			result.append(sum_column/row)
	return result