import utility
from rich.console import Console

console = Console()


def ludecomposition(
    u: utility.Matrix, l: utility.Matrix_show, pivot_indices: list[int]
) -> utility.Matrix:

    column_count = row_count = len(u)
    num_of_elimination = 0
    column = 0
    p = utility.identity_matrix(row_count, column_count)
    row_nums = [
        utility.lower_num(utility.Fraction(1), "𝑅", row + 1) for row in range(row_count)
    ]

    for row in range(row_count):

        # there is a pivot in this column
        pivot_indices.append(column)

        # Swap The Rows If The Pivot = 0
        if utility.is_zero(u[row][column]):
            is_swap = False
            # Swap The Rows If The Pivot = 0
            for j in range(row + 1, row_count):
                if not utility.is_zero(u[j][column]):

                    is_swap = True

                    # Printing The Steps
                    console.print(
                        f"[bright_magenta]  {row_nums[row]} <=> {row_nums[j]}"
                    )

                    u[row], u[j] = u[j], u[row]
                    p[row], p[j] = p[j], p[row]
                    for k in range(column):
                        l[row][k], l[j][k] = l[j][k], l[row][k]

                    break

            if is_swap:
                console.print("  [bold green]𝐔 & 𝐋:")
                utility.show(
                    [[*r1, *r2] for r1, r2 in zip(u, l)],
                    column_count,
                    pivot_indices,
                    row,
                    two_show=True,
                )
            else:
                column += 1
                continue

        # The Elimination Part :)
        for j in range(row + 1, row_count):

            coefficient = u[j][column] / u[row][column]
            l[j][column] = coefficient

            # No Elimination needed if the coefficient = 0
            if not utility.is_zero(coefficient):

                num_of_elimination += 1

                # Printing The Steps
                console.print(
                    f"[bright_magenta]  {row_nums[j]} = {row_nums[j]} + {utility.lower_num(-coefficient, '𝑅',row + 1)}"
                )

                for k in range(column, column_count):
                    u[j][k] += -coefficient * u[row][k]

        if num_of_elimination > 0:
            console.print("  [bold green]𝐔 & 𝐋:")
            utility.show(
                [[*r1, *r2] for r1, r2 in zip(u, l)],
                column_count,
                pivot_indices,
                row,
                two_show=True,
            )

        num_of_elimination = 0

        # Moving To The Next Pivot
        column += 1

    return p


def main() -> None:

    utility.greeting("LU Decomposition of a 𝐀ₙₓₙ matrix using Gauss Elimination :)")

    pivot_indices = []

    col_count = row_count = utility.input_int("  Enter 𝑛 : ")

    u = utility.read_equations(row_count, col_count)
    l = utility.lower_triangle_matrix(row_count, col_count)

    console.print("  [bold green]𝐔 & 𝐋:")
    utility.show(
        [[*r1, *r2] for r1, r2 in zip(u, l)], col_count, pivot_indices, two_show=True
    )

    p = ludecomposition(u, l, pivot_indices)

    console.print("  [bold cyan]∵ 𝐏𝐀 = 𝐋𝐔 \n")

    console.print("  [bold green]∴ 𝐋 =")
    utility.show(l, col_count, pivot_indices)
    console.print("  [bold green]∴ 𝐔 =")
    utility.show(u, col_count, pivot_indices)
    console.print("  [bold green]∴ 𝐏 =")
    utility.show(p, col_count, pivot_indices)
