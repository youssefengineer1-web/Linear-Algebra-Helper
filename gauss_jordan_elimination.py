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
        while utility.is_zero(equations[row][column]) and column < column_count - 1:
            # Swap The Rows If The Pivot = 0
            is_swap = utility.swap_rows(equations, row, column, row_nums)

            if is_swap:
                utility.show(equations, column_count - 1, pivot_indices, row)
            else:
                column += 1

        # If There Isn't Any Pivots Left
        if column == column_count - 1:
            break

        # there is a pivot in this column
        pivot_indices.append(column)

        # If The Pivot != 1 We Divide The Eqution By The Pivot
        if not utility.is_zero(equations[row][column] - 1):

            utility.make_pivot(equations, row, column, row_nums)
            utility.show(equations, column_count - 1, pivot_indices, row)

        # The Elimination Part :)
        num_of_elimination = utility.gauss_jordan_elimination(
            equations, row, column, row_nums
        )

        if num_of_elimination > 0:
            utility.show(equations, column_count - 1, pivot_indices, row)

        # Moving To The Next Pivot
        row += 1
        column += 1

    return row, column


# Check Solution Type
def print_solution(
    equations: utility.Matrix,
    row: int,
    column: int,
    pivot_indices: list[int],
) -> None:

    set_pivots = set(pivot_indices)
    column_count = len(equations[0])

    if any(
        all(utility.is_zero(i) for i in equ[column:-1]) and not utility.is_zero(equ[-1])
        for equ in equations[row:]
    ):
        console.print("[bold red]  No Solution")

    elif len(pivot_indices) == column_count - 1:
        console.print("[bold green]  One Solution")

        for col in range(column_count - 1):
            console.print(
                f"[cyan]  {utility.lower_num(utility.Fraction(1),'𝑥',col + 1)} = {utility.show_num(equations[col][-1])}"
            )

    else:
        console.print("[yellow]  Many Solution")

        # Printing The Solution
        free_variables = ["[bold green]  = [/bold green]"]

        console.print("[yellow]  Free Variables :", end="")

        unkonws = [
            utility.lower_num(utility.Fraction(1), "𝑥", i + 1)
            for i in range(column_count - 1)
        ]
        many_sol = [unkonws]

        end = ""

        for i, col in enumerate(zip(*equations)):
            j = 0
            vector = []
            if i == column_count - 1 and all(n == 0 for n in col):
                end = free_variables[-1].split("+")[0]
                break
            if i not in set_pivots:
                if i < column_count - 1:
                    free_variables.append(f"[bold green]{unkonws[i]} +[/bold green]")
                    console.print(f" [bold yellow]{unkonws[i]}", end="")
                for n in range(column_count - 1):
                    if i == n:
                        vector.append(utility.Fraction(1))
                    elif n not in set_pivots:
                        vector.append(utility.Fraction(0))
                    else:
                        if i == column_count - 1:
                            vector.append(col[j])
                        else:
                            vector.append(-col[j])
                        j += 1

                many_sol.append(vector)

        console.print(f"\n")

        utility.show_vectors(many_sol, free_variables, separator="   +", end=end, is_row_vector=True)  # type: ignore


def main() -> None:

    pivot_indices = []

    utility.greeting(
        "Solving System Of Linear Equations With Gauss Jordan Elimination :)"
    )

    equation_count = utility.input_int("Enter Number Of Equations : ")
    variables = utility.input_int("Enter Number Of Unknows : ")
    column_count = variables + 1

    equations = utility.read_equations(equation_count, column_count)

    utility.show(equations, column_count - 1, pivot_indices)

    row, column = gauss_jordan(equations, pivot_indices)

    utility.show(equations, column_count - 1, pivot_indices)

    print_solution(equations, row, column, pivot_indices)

    console.print("[dim]=" * 48)
