import utility
from rich.console import Console

console = Console()


def matrix_inverse(rows: utility.Matrix, pivot_indices: list[int]) -> int:

    row_count = len(rows)
    column = 0
    row_nums = [
        utility.lower_num(utility.Fraction(1), "𝑅", row + 1) for row in range(row_count)
    ]

    for row in range(row_count):

        # Swap The Rows If The Pivot = 0
        if utility.is_zero(rows[row][column]):
            is_swap = utility.swap_rows(rows, row, column, row_nums)

            if is_swap:
                utility.show(rows, row_count, pivot_indices, row)
            else:  # No Inverse
                return row - 1

        # there is a pivot in this column
        pivot_indices.append(column)

        # If The Pivot != 1 We Divide The Eqution By The Pivot
        if not utility.is_zero(rows[row][column] - 1):
            utility.make_pivot(rows, row, column, row_nums)
            utility.show(rows, row_count, pivot_indices, row)

        # The Elimination Part :)
        num_of_elimination = utility.gauss_jordan_elimination(
            rows, row, column, row_nums
        )

        if num_of_elimination > 0:
            utility.show(rows, row_count, pivot_indices, row)

        num_of_elimination = 0

        # Moving To The Next Pivot
        column += 1

    return row_count


def print_solution(
    rows: utility.Matrix, cur_row: int, pivot_indices: list[int]
) -> None:

    row_count = len(rows)

    if cur_row != row_count:

        console.print("[bold red]  There No Inverse 𝐀⁻¹")
    else:
        console.print("[bold green]  𝐀⁻¹ : ")
        utility.show(rows, row_count, pivot_indices, -2, True)


def main() -> None:

    utility.greeting(
        "Finding the inverse of a 𝐀ₙₓₙ matrix using Gauss Jordan elimination. :)"
    )

    pivot_indices = []

    col_count = row_count = utility.input_int("  Enter 𝑛 : ")

    rows = utility.read_equations(row_count, col_count, True)

    utility.show(rows, row_count, pivot_indices)

    cur_row = matrix_inverse(rows, pivot_indices)

    print_solution(rows, cur_row, pivot_indices)
