import utility
from gauss_jordan_elimination import gauss_jordan
from rich.console import Console

console = Console()


# Check Solution Type
def print_solution(
    rows: utility.Matrix,
    A: utility.Matrix,
    pivot_indices: list[int],
) -> None:

    set_pivots = set(pivot_indices)
    column_count = len(rows[0])

    if len(pivot_indices) == column_count - 1:
        console.print("[bold green]  ker(𝑨) = {O\u0302}\n")
        console.print("[bold green]  img(𝑨) = span {")

        utility.show_vectors(A, [], x="[bold green]  } [/bold green] \n")

    else:

        # Printing The Solution

        kernel_basis = []

        for i, col in enumerate(zip(*rows)):
            pivot_row = 0
            basis_vector = []
            if i == column_count - 1 and all(
                n == 0 for n in col
            ):  # Ignore the augmented column if it is all zeros
                break
            if i not in set_pivots:
                for n in range(column_count - 1):
                    if i == n:
                        basis_vector.append(utility.Fraction(1))
                    elif n not in set_pivots:
                        basis_vector.append(utility.Fraction(0))
                    else:
                        if i == column_count - 1:
                            basis_vector.append(col[pivot_row])
                        else:
                            basis_vector.append(-col[pivot_row])
                        pivot_row += 1

                kernel_basis.append(basis_vector)

        console.print("[bold green]  ker(𝑨) = span {")
        utility.show_vectors(
            kernel_basis, [], is_row_vector=True, x="[bold green]  } [/bold green] \n"
        )

        img_A = [[row[i] for i in pivot_indices] for row in A]

        console.print("[bold green]  img(𝑨) = span {")

        utility.show_vectors(img_A, [], x="[bold green]  } [/bold green] \n")


def main() -> None:

    pivot_indices = []

    utility.greeting("Finding the kernel and image of 𝑨 :)")

    row_count = utility.input_int("Enter Number Of Rows : ")
    column_count = utility.input_int("Enter Number Of Columns : ")
    aug_count = column_count + 1

    rows = utility.read_equations(row_count, column_count)
    A = [row.copy() for row in rows]

    for row in range(len(rows)):
        rows[row].append(utility.Fraction(0))

    utility.show(rows, aug_count - 1, pivot_indices)

    gauss_jordan(rows, pivot_indices)

    utility.show(rows, aug_count - 1, pivot_indices)

    print_solution(rows, A, pivot_indices)

