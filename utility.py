from fractions import Fraction
from rich.console import Console
from transpose import transpose
from typing import Sequence

console = Console()
type Matrix = list[list[Fraction]]
type Matrix_show = list[list[Fraction | str]]
PRECISION = 14
SUB = str.maketrans("0123456789-+", "₀₁₂₃₄₅₆₇₈₉₋₊")
EPS = 10**-PRECISION
PIVOT_COLOR = "bold yellow"
CURRENT_ROW_COLOR = "cyan"
DEFAULT_COLOR = "white"


def lower_num(coff: Fraction, sym: str, num: int) -> str:
    if is_zero(abs(coff) - 1):
        if coff > 0:
            return f"{sym}{str(num).translate(SUB)}"
        else:
            return f"-{sym}{str(num).translate(SUB)}"

    return f"{show_num(coff)}{sym}{str(num).translate(SUB)}"


def is_zero(x: Fraction) -> bool:
    return abs(x) < EPS


def input_int(message: str) -> int:
    while True:
        try:
            return int(console.input(f"[magenta]{message}"))
        except ValueError:
            console.print("[yellow]could not convert to Integer")


# Changing the way we Show The Number
def show_num(num: Fraction) -> str:

    frac = Fraction(num).limit_denominator()

    if is_zero(num):
        return "0"

    if round(num, PRECISION).is_integer():
        return str(int(round(num, PRECISION)))

    if frac.denominator > 100:
        return f"{float(round(num, PRECISION)):g}"

    return str(frac)


# Printing The Equations & The Cost of style Is High :)


def get_widths(strings: Sequence[Sequence[Fraction | str]]) -> list[int]:

    return [max(max(len(num), 3) for num in column) for column in zip(*strings)]


def brackets(row_index: int, rows: int) -> tuple[str, str]:

    if row_index == 0:
        return " ⌈", "⌉"

    if row_index == rows - 1:
        return " ⌊", "⌋"

    return " |", "|"


def show(
    rows: Matrix_show | Matrix,
    col_aug: int,
    pivot_indices: list[int],
    cur_row: int = -1,
    no_augmented: bool = False,
    two_show: bool = False,
) -> None:

    row_count = len(rows)
    pivots = len(pivot_indices)

    # Change Every Number to Fraction string
    if no_augmented:
        strings = [
            [show_num(col) if type(col) == Fraction else col for col in row[col_aug:]]
            for row in rows
        ]
    else:
        strings = [
            [show_num(col) if type(col) == Fraction else col for col in row]
            for row in rows
        ]

    # Calculate The Width of The Longest Number in The Column
    widths = get_widths(strings)

    for row_index, row in enumerate(strings):

        row_colour = (
            CURRENT_ROW_COLOR
            if row_index == cur_row or cur_row == -2
            else DEFAULT_COLOR
        )

        # Determin The Closing And Ending of Every Row
        left, right = brackets(row_index, row_count)

        console.print(left, end=" ")

        # Printing The Equations
        for col_index, (value, w) in enumerate(zip(row, widths)):

            if col_index == col_aug:
                if two_show:
                    console.print(f"{right} {left}", end=" ")  # augmented part
                else:
                    console.print(f"¦", end=" ")  # augmented part

            is_pivot = row_index < pivots and col_index == pivot_indices[row_index]

            colour = PIVOT_COLOR if is_pivot else row_colour

            text = f"[{colour}]{value:^{w}s}"
            console.print(text, end=" ")  # ^{width[col_index]} => num of Chars

        console.print(right)

    console.print("[dim]=" * 48)


def show_vectors(
    vectors: Matrix,
    vars: list,
    start: str = "",
    separator: str = " ,",
    colour: str = "bold cyan",
    is_row_vector: bool = False,
    end: str = "",
    x: str = "",
) -> None:

    if is_row_vector:
        vectors = transpose(vectors)  # old column vector :)

    vector_count = len(vectors)

    # Change Every Number to Fraction string

    strings = [
        [num if type(num) == str else show_num(num) for num in vector]
        for vector in vectors
    ]

    # Calculate The Width of The Longest Number in The Column
    widths = get_widths(strings)

    # Printing The vectors
    for vector_index, vetctor in enumerate(strings):

        # Determin The Closing And Ending of Every Row
        left, right = brackets(vector_index, vector_count)
        sym = separator if vector_index == vector_count // 2 else " " * len(separator)
        s = start if vector_index == vector_count // 2 else " " * len(start)
        e = end if vector_index == vector_count // 2 else ""
        console.print("  " + s, end="")
        console.print(left, end="")

        text = f"{right}{sym}{left}".join(
            f"[{colour}]{num:^{widths[i]}s}[/{colour}]" for i, num in enumerate(vetctor)
        )
        if vars and sym == separator:
            for var in vars:
                text = text.replace(sym, var, 1)
        console.print(text, end="")  # ^{width[col_index]} => num of Chars

        console.print(right + e)

    console.print(x + "[dim]=" * 48)


def make_identity_row(row_count: int, cur_row: int) -> list:

    return ["1" if i == cur_row else "0" for i in range(row_count)]


def identity_matrix(row_count: int, column_count: int) -> Matrix:

    matrix = [[Fraction(0)] * column_count for _ in range(row_count)]

    for i in range(row_count):
        if i < column_count:
            matrix[i][i] = Fraction(1)

    return matrix


def lower_triangle_matrix(row_count: int, column_count: int) -> Matrix_show:

    matrix = [
        [Fraction(0) if j >= i else " " for j in range(column_count)]
        for i in range(row_count)
    ]

    for i in range(row_count):
        if i < column_count:
            matrix[i][i] = Fraction(1)

    return matrix


def read_equations(
    row_count: int, col_count: int, is_inverse=False, msg: str = "Row Coefficients"
) -> Matrix:

    rows = []

    # Asking The User To Enter The Equations
    def get_order(num: int) -> str:
        return f"{num+1}{['st', 'nd', 'rd', 'th'][3 if num>= 3 else num]}"

    for i in range(row_count):
        while True:
            try:
                row = console.input(f"[magenta]Enter {get_order(i)} {msg} : ").split()

                # Check The Number Of Columns
                if len(row) != col_count:
                    console.print(f"[yellow]Error: Expected {col_count} numbers.")
                    continue

                if is_inverse:
                    row.extend(make_identity_row(col_count, i))  # rows

                rows.append([Fraction(number) for number in row])

                break
            except ValueError:
                console.print(
                    "[yellow]Error: Could not convert one or more values to float."
                )

    console.print("[dim]=" * 48)

    return rows


def swap_rows(
    equations: Matrix,
    row: int,
    column: int,
    row_nums: list[str],
) -> bool:

    equation_count = len(equations)
    is_swap = False
    # Swap The Rows If The Pivot = 0
    for j in range(row + 1, equation_count):
        if not is_zero(equations[j][column]):

            is_swap = True

            # Printing The Steps
            console.print(
                f"[bright_magenta]  {row_nums[row]} [bold]↔[/bold] {row_nums[j]}"
            )

            equations[row], equations[j] = equations[j], equations[row]

            break
    return is_swap


def make_pivot(
    equations: Matrix,
    row: int,
    column: int,
    row_nums: list[str],
):

    column_count = len(equations[0])
    pivot = equations[row][column]

    # Printing The Steps
    console.print(
        f"[bright_magenta]  {row_nums[row]} = {row_nums[row]}/({show_num(pivot)})"
    )

    for j in range(column, column_count):
        equations[row][j] /= pivot


def gauss_jordan_elimination(
    equations: Matrix, row: int, column: int, row_nums: list[str]
) -> int:

    num_of_elimination = 0
    equation_count = len(equations)
    column_count = len(equations[0])

    for j in range(equation_count):
        if j != row:
            coefficient = equations[j][column]

            # No Elimination needed if the coefficient = 0
            if not is_zero(coefficient):

                num_of_elimination += 1

                # Printing The Steps
                console.print(
                    f"[bright_magenta]  {row_nums[j]} = {row_nums[j]} + {lower_num(-coefficient, '𝑅',row + 1)}"
                )

                for k in range(column, column_count):
                    equations[j][k] += -coefficient * equations[row][k]

    return num_of_elimination


def gauss_elimination(
    equations: Matrix, row: int, column: int, row_nums: list[str]
) -> int:

    num_of_elimination = 0
    equation_count = len(equations)
    column_count = len(equations[0])

    for j in range(row + 1, equation_count):
        coefficient = equations[j][column]

        # No Elimination needed if the coefficient = 0
        if not is_zero(coefficient):

            num_of_elimination += 1

            # Printing The Steps
            console.print(
                f"[bright_magenta]  {row_nums[j]} = {row_nums[j]} + {lower_num(-coefficient, '𝑅',row + 1)}"
            )

            for k in range(column, column_count):
                equations[j][k] += -coefficient * equations[row][k]

    return num_of_elimination


def greeting(msg: str) -> None:

    console.print("[dim]=" * 48)
    console.print(f"[bold cyan]{msg}")
    console.print("[dim]=" * 48)
