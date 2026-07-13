import utility
from dot_product import dot
from transpose import transpose
from rich.console import Console

console = Console()


def show_2_matrices(
    m1: utility.Matrix,
    m2: utility.Matrix,
    pivot_indices: list[int],
    cur_row: int = -1,
) -> None:

    r1 = len(m1)
    c1 = len(m1[0])
    r2 = len(m2)
    c2 = len(m2[0])
    row_count = max(r1, r2)
    pivots = len(pivot_indices)

    # Change Every Number to Fraction string

    str_m1 = [[utility.show_num(col) for col in row] for row in m1]
    str_m2 = [[utility.show_num(col) for col in row] for row in m2]

    # Calculate The Width of The Longest Number in The Column
    wid_m1 = utility.get_widths(str_m1)
    wid_m2 = utility.get_widths(str_m2)

    for row in range(row_count):

        row_colour = (
            utility.CURRENT_ROW_COLOR if row == cur_row or cur_row == -2 else utility.DEFAULT_COLOR
        )
        end = "" if row < r2 else "\n"
        space = "" if row < r1 else " " * (sum(wid_m1) + c1 + 4)

        # Determin The Closing And Ending of Every Row
        left, right = utility.brackets(row, r1)

        if row < r1:
            console.print(left, end=" ")
            # Printing The Equations
            for col in range(c1):

                text = f"[{row_colour}]{str_m1[row][col]:^{wid_m1[col]}s}"
                console.print(text, end=" ")  # ^{width[col_index]} => num of Chars

            console.print(right, end=end)

        left, right = utility.brackets(row, r2)

        if row < r2:
            console.print(space + left, end=" ")
            # Printing The Equations
            for col in range(c2):

                is_pivot = row < pivots and col == pivot_indices[row]

                colour = utility.PIVOT_COLOR if is_pivot else utility.DEFAULT_COLOR

                text = f"[{colour}]{str_m2[row][col]:^{wid_m2[col]}s}"
                console.print(text, end=" ")  # ^{width[col_index]} => num of Chars

            console.print(right)

    console.print("[dim]=" * 48)


def matrix_mult(m1: utility.Matrix, m2: utility.Matrix):

    r1 = len(m1)
    r2 = len(m2)
    c2 = len(m2[0])
    m2_trans = transpose(m2)

    res: utility.Matrix_show = [[" " for _ in range(c2)] for _ in range(r1)]

    for c in range(c2):
        for r in range(r1):
            res[r][c] = dot([m1[r], m2_trans[c]])

        console.print("  [bold green]𝑴₁𝑴₂ = ")
        show_2_matrices(m1, m2, [c for _ in range(r2)], cur_row=-2)
        console.print("  [bold green]'Matrix Ans' = ")
        utility.show(res, c2, [c for _ in range(r1)], -2)


def main():

    utility.greeting("Matrix Mulipilcation 𝑴₁𝑴₂ :)")
    r1 = utility.input_int("Enter Number of Rows of 𝑴₁ : ")
    c1 = utility.input_int("Enter Number of Columns of 𝑴₁ : ")
    r2 = utility.input_int("Enter Number of Rows of 𝑴₂ : ")
    c2 = utility.input_int("Enter Number of Columns of 𝑴₂ : ")

    if c1 != r2:
        console.print("  [bold red] Number of Columns of 𝑴₁ != Number of Rows of 𝑴₂")
        return

    console.print("[dim]=" * 48)
    m1 = utility.read_equations(r1, c1, msg="Row of 𝑴₁")
    m2 = utility.read_equations(r2, c2, msg="Row of 𝑴₂")

    matrix_mult(m1, m2)
