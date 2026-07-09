import utility
from rich.console import Console

console = Console()


def transpose(rows: utility.Matrix) -> utility.Matrix:
    return [list(col) for col in zip(*rows)]


def main() -> None:

    utility.greeting("Matrix 𝑻ranspose :)")

    row_count = utility.input_int("Enter Number Of Rows : ")
    col_count = utility.input_int("Enter Number Of Columns : ")

    rows = utility.read_equations(row_count, col_count)

    utility.show(rows, col_count, [])
    trans = transpose(rows)
    console.print("  [green] 𝑻ranspose : ")
    utility.show(trans, col_count, [], -2)
