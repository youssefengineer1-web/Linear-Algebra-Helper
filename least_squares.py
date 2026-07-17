import utility
from gauss_jordan_elimination import gauss_jordan, print_solution
from matrix_mult import matrix_mult, show_2_matrices
from transpose import transpose
from rich.console import Console

console = Console()


def main() -> None:

    pivot_indices = []

    utility.greeting("Solving System Of Linear Equations With Least Squares :)")

    equation_count = utility.input_int("Enter Number Of Equations : ")
    variables = utility.input_int("Enter Number Of Unknows : ")
    column_count = variables + 1

    equations = utility.read_equations(equation_count, column_count)
    A = [row[:-1] for row in equations]
    b = [row[-1:] for row in equations]
    A_trans = transpose(A)
    A_trans_A = matrix_mult(A_trans, A, show_steps=False)
    A_trans_b = matrix_mult(A_trans, b, show_steps=False)

    console.print("  [bold green]∵ 𝑨ᵀ𝑨 = ")
    show_2_matrices(A_trans, A, [])
    console.print("  [bold green]∴ 𝑨ᵀ𝑨  = ")
    utility.show(A_trans_A, column_count - 1, [], -2)

    console.print("  [bold green]∵ 𝑨ᵀ𝑏 = ")
    show_2_matrices(A_trans, b, [])
    console.print("  [bold green]∴ 𝑨ᵀ𝑏  = ")
    utility.show(A_trans_b, 1, [], -2)

    for i in range(len(A_trans_A)):
        A_trans_A[i].append(A_trans_b[i][0])

    console.print("  [bold green]∵ 𝑨ᵀ𝑨 𝑥* = 𝑨ᵀ𝑏")
    utility.show(A_trans_A, column_count - 1, pivot_indices)

    row, column = gauss_jordan(A_trans_A, pivot_indices) # type: ignore

    utility.show(A_trans_A, column_count - 1, pivot_indices)

    print_solution(A_trans_A, row, column, pivot_indices) # type: ignore

    console.print("[dim]=" * 48)
