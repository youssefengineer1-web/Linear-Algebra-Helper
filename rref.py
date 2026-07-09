import utility
from rich.console import Console

console = Console()


def gauss_jordan(
    equations: utility.Matrix,
    pivot_indices: list[int],
) -> tuple[int, int]:

    equation_count = len(equations)
    column_count = len(equations[0])
    row = column = 0
    row_nums = [
        utility.lower_num(utility.Fraction(1), "𝑅", row + 1)
        for row in range(equation_count)
    ]

    while row < equation_count and column < column_count:

        # Moving TO The Another Column If The Pivot == 0
        while  column < column_count and utility.is_zero(equations[row][column]):
            # Swap The Rows If The Pivot = 0
            is_swap = utility.swap_rows(equations, row, column, row_nums)

            if is_swap:
                utility.show(equations, column_count, pivot_indices, row)
            else:
                column += 1

        # If There Isn't Any Pivots Left
        if column == column_count:
            break

        # there is a pivot in this column
        pivot_indices.append(column)

        # If The Pivot != 1 We Divide The Eqution By The Pivot
        if not utility.is_zero(equations[row][column] - 1):

            utility.make_pivot(equations, row, column, row_nums)
            utility.show(equations, column_count, pivot_indices, row)

        # The Elimination Part :)
        num_of_elimination = utility.gauss_jordan_elimination(
            equations, row, column, row_nums
        )

        if num_of_elimination > 0:
            utility.show(equations, column_count, pivot_indices, row)

        # Moving To The Next Pivot
        row += 1
        column += 1

    return row, column


def main() -> None:

    pivot_indices = []

    utility.greeting("Reduced Row Echelon Form With Gauss Jordan Elimination :)")

    equation_count = utility.input_int("Enter Number Of Rows : ")
    column_count = utility.input_int("Enter Number Of Columns : ")

    equations = utility.read_equations(equation_count, column_count)

    utility.show(equations, column_count, pivot_indices)

    gauss_jordan(equations, pivot_indices)

    console.print(f"  [green]𝑹𝑹𝑬𝑭  : ")

    utility.show(equations, column_count, pivot_indices)
