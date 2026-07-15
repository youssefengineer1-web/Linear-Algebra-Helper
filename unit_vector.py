import utility
from rich.console import Console
from fractions import Fraction

console = Console()


def unit_vector(vector: list[Fraction], n=1) -> list[Fraction]:

    low_num = str(n).translate(utility.SUB)
    text1 = " + ".join(f"({utility.show_num(num)})²" for num in vector)
    v1 = Fraction(sum(i * i for i in vector) ** 0.5)
    for i in range(len(vector)):
        vector[i] /= v1

    console.print(f"  [bold cyan]∵ 𝑢{low_num} = 𝐕{low_num} / ‖𝐕{low_num}‖\n")

    console.print(f"  ∵ ‖𝐕{low_num}‖ = √({text1}) = {utility.show_num(v1)}\n")
    utility.show_vectors(
        [vector], [], start=f"∴ 𝑢{low_num} =", colour="bold green", is_row_vector=True
    )

    return vector


def main() -> None:

    utility.greeting("unit vector 𝑢₁ of 𝐕₁  ⇒ 𝐕 ∈ ℝⁿ  :) ")

    n = utility.input_int("Enter 𝑛 : ")
    vector = utility.read_equations(1, n, msg="Vector")

    utility.show_vectors(vector, [], "𝐕₁ =", is_row_vector=True)

    unit_vector(vector[0])
