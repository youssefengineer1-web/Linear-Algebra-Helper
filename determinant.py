import utility
from rich.console import Console

console = Console()


def determinant(rows: utility.Matrix, pivot_indices: list[int]) -> int:

    num_of_elimination = 0
    num_of_swap = 0
    column_count = row_count = len(rows)
    column = 0
    row_nums = [
        utility.lower_num(utility.Fraction(1), "𝑅", row + 1) for row in range(row_count)
    ]

    for row in range(row_count):

        # Swap The Rows If The Pivot = 0
        if utility.is_zero(rows[row][column]):
            is_swap = utility.swap_rows(rows, row, column, row_nums)

            if is_swap:
                num_of_swap += 1
                utility.show(rows, column_count, pivot_indices, row)
            else:
                return num_of_swap

        # there is a pivot in this column
        pivot_indices.append(column)

        # The Elimination Part :)
        for j in range(row + 1, row_count):

            coefficient = rows[j][column] / rows[row][column]

            # No Elimination needed if the coefficient = 0
            if not utility.is_zero(coefficient):

                num_of_elimination += 1

                # Printing The Steps
                console.print(
                    f"[bright_magenta]  {row_nums[j]} = {row_nums[j]} + {utility.lower_num(-coefficient, '𝑅',row + 1)}"
                )

                for k in range(column, column_count):
                    rows[j][k] += -coefficient * rows[row][k]

        if num_of_elimination > 0:
            utility.show(rows, column_count, pivot_indices, row)

        num_of_elimination = 0

        # Moving To The Next Pivot
        column += 1

    return num_of_swap


def print_solution(rows: utility.Matrix, k: int, pivot_indices: list[int]) -> None:

    col_count = row_count = len(rows)

    console.print("[bold green]  𝐔 : ")
    utility.show(rows, col_count, pivot_indices, row_count)

    console.print(f"  [bold green]Number of Swaps ⇒ 𝑘 = {k}")
    console.print("  [bold cyan]∵ det(𝐀) = (−1)ᵏ × ∏ 𝐔ᵢᵢ")

    det = (-1) ** k
    for i, row in enumerate(rows):
        det *= row[i]

    console.print(f"  [bold green]∴ det(𝐀) = {utility.show_num(det)}")


def main() -> None:

    utility.greeting(
        "Finding the Determinant of a 𝐀ₙₓₙ matrix using Gauss Elimination :)"
    )

    pivot_indices = []

    col_count = row_count = utility.input_int("  Enter 𝑛 : ")

    rows = utility.read_equations(row_count, col_count)

    utility.show(rows, col_count, pivot_indices)

    k = determinant(rows, pivot_indices)

    print_solution(rows, k, pivot_indices)

    console.print("[dim]=" * 48)
