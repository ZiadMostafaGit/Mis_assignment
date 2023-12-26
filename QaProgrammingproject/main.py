class Hungarian:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = [0] * 3
        self.columns = [0] * 3
        self.final_answer = 0

    def row_reduction(self, input_matrix):
        for i in range(3):
            min_val = min(input_matrix[i])
            for k in range(3):
                input_matrix[i][k] -= min_val

    def col_reduction(self, input_matrix):
        for i in range(3):
            min_val = min(row[i] for row in input_matrix)
            for k in range(3):
                input_matrix[k][i] -= min_val

    def print_2d_matrix(self, matrix):
        for row in matrix:
            print(" ".join(map(str, row)))

    def number_of_zeros_in_row(self, input_matrix):
        for i in range(3):
            self.rows[i] = input_matrix[i].count(0)

    def number_of_zeros_in_column(self, input_matrix):
        for i in range(3):
            self.columns[i] = sum(1 for row in input_matrix if row[i] == 0)

    def test_for_optimal_assignment(self, input_matrix):
        self.number_of_zeros_in_row(input_matrix)
        self.number_of_zeros_in_column(input_matrix)

        number_of_zeros = sum(self.rows)
        for i in range(3):
            for j in range(3):
                if self.rows[i] + self.columns[j] == number_of_zeros:
                    return True
        return False

    def change_the_matrix(self, input_matrix):
        intersect_row = self.rows.index(max(self.rows))
        intersect_col = self.columns.index(max(self.columns))

        min_of_unlined_cells = min(
            input_matrix[i][j]
            for i in range(3)
            for j in range(3)
            if input_matrix[i][j] == 0 and not (i == intersect_row and j == intersect_col)
        )

        for i in range(3):
            for j in range(3):
                if input_matrix[i][j] == 0 and not (i == intersect_row and j == intersect_col):
                    input_matrix[i][j] -= min_of_unlined_cells

        input_matrix[intersect_row][intersect_col] += min_of_unlined_cells

    def prepare_matrix_to_final_step(self, input_matrix):
     while self.test_for_optimal_assignment(input_matrix):
        previous_matrix = [row[:] for row in input_matrix]  # Copy the matrix
        self.change_the_matrix(input_matrix)
        
        # Break the loop if no changes were made in the last iteration
        if input_matrix == previous_matrix:
            break

    def making_the_final_assignment(self, input_matrix):
        index = [0] * 3
        for i in range(3):
            for j in range(3):
                if input_matrix[i][j] != 0:
                    input_matrix[i][j] = 0
                elif index[j] == 0:
                    input_matrix[i][j] = self.matrix[i][j]
                    index[j] = 1
                    while j < 2 and i < 2:
                        input_matrix[i][j + 1] = 0
                        i += 1

    def count_the_final_assignment(self, input_matrix):
        self.final_answer = sum(sum(row) for row in input_matrix)

    def the_hungarian_algorithm(self, input_matrix):
        self.row_reduction(input_matrix)
        self.col_reduction(input_matrix)
        self.prepare_matrix_to_final_step(input_matrix)
        self.making_the_final_assignment(input_matrix)
        self.count_the_final_assignment(input_matrix)
        return self.final_answer


if __name__ == "__main__":
    matrix = [
        [30, 25, 10],
        [15, 10, 20],
        [25, 20, 15]
    ]

    hungarian = Hungarian(matrix)
    result = hungarian.the_hungarian_algorithm([row[:] for row in matrix])

    print("Result is:", result)
