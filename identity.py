import utility
from rich.console import Console

console = Console()


def main() -> None:

    utility.greeting("Create Identity Matrix 𝑰  :)")

    row_count = utility.input_int("Enter number of rows : ")
    column_count = utility.input_int("Enter number of columns : ")

    console.print("[dim]=" * 48)

    I = utility.identity_matrix(row_count, column_count)

    utility.show(I, column_count, list(range(row_count)), -2)
