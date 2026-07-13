import utility
import math
from rich.console import Console
from transpose import transpose
from dot_product import dot

console = Console()


def rotation():

    utility.greeting("Rotation by θ to a Vector 𝑽 ⇒ 𝐕 ∈ ℝⁿ  :)")

    while (n := utility.input_int("Enter 𝑛 : ")) < 1:
        console.print("  [bold red]𝑛 must be > 0")

    vector = utility.read_equations(1, n, msg="Vector")

    u = v = 0

    if n == 1:
        console.print(f"  [bold green]∴ 𝑻(𝑿) = [{vector[0][0]}]")
        return

    elif n == 2:

        u, v = 0, 1

    elif n == 3:

        planes = {"x": (1, 2), "y": (0, 2), "Z": (0, 1)}

        while (axis := input("Choose axis of rotation : ").strip().lower()) not in (
            "x",
            "y",
            "z",
        ):
            console.print("  [bold red]Wrong Axis")

        u, v = planes[axis]

    else:

        console.print("  [bold cyan]Rotaion about 𝑥ᵤ𝑥ᵥ plane")

        while (u := utility.input_int("Enter 𝑢 : ") - 1) < 0 or u >= n:
            console.print("  [bold red] 0 < 𝑢 <= 𝑛")

        while (v := utility.input_int("Enter 𝑣 : ") - 1) < 0 or v >= n or v == u:
            if v < 0 or v >= n:
                console.print("  [bold red] 0 < 𝑣 <= 𝑛")
            else:
                console.print("  [bold red]𝑣 should not equal to 𝑢")

    while (mod := utility.input_int("rad ⇒ 1, degree ⇒ 2\nChoose Mode : ")) not in (
        1,
        2,
    ):
        console.print(" [bold red]Wrong Mode")

    while True:
        try:
            theta = utility.Fraction(console.input("\n[bold cyan]Enter θ : ").strip())
            break
        except ValueError:
            console.print("  [bold red]Could Not Convert To Float")

    rotation_matrix = utility.identity_matrix(n, n)
    rotation_matrix[u][u] = f"cos({utility.show_num(theta)})"  # type: ignore
    rotation_matrix[u][v] = f"-sin({utility.show_num(theta)})"  # type: ignore
    rotation_matrix[v][u] = f"sin({utility.show_num(theta)})"  # type: ignore
    rotation_matrix[v][v] = f"cos({utility.show_num(theta)})"  # type: ignore

    if mod == 2:
        theta = math.radians(theta)

    console.print("\n  [cyan]∵𝑻(𝑿) = 𝑨𝑿\n")
    utility.show(
        [[*r1, *r2] for r1, r2 in zip(rotation_matrix, transpose(vector))],
        n,
        [i for i in range(n)],
        -2,
        two_show=True,
    )

    c = utility.Fraction(math.cos(theta))
    s = utility.Fraction(math.sin(theta))

    rotation_matrix[u][u] = c
    rotation_matrix[u][v] = -s
    rotation_matrix[v][u] = s
    rotation_matrix[v][v] = c

    trans = [dot([rotation_matrix[i], vector[0]]) for i in range(n)]

    utility.show_vectors([trans], [],"∴ 𝑻(𝑿) =", colour="green", is_row_vector=True)
