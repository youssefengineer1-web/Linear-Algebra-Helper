import utility
from rich.console import Console
from fractions import Fraction

console = Console()


def main() -> None:

    utility.greeting("unit vector 𝑢₁ of 𝐕₁  ⇒ 𝐕 ∈ ℝⁿ  :) ")

    n = utility.input_int("Enter 𝑛 : ")
    vector = utility.read_equations(1, n, msg="Vector")

    utility.show_vectors(vector, [],"𝐕₁ =", is_row_vector=True)

    text1 = " + ".join(f"({utility.show_num(num)})²" for num in vector[0])
    v1 = Fraction(sum(i * i for i in vector[0]) ** 0.5)
    for i in range(len(vector[0])):
        vector[0][i] /= v1

    console.print(f"  ∵ ‖𝐕₁‖ = √({text1}) = {utility.show_num(v1)}")

    console.print("\n  [cyan]∴ 𝑢₁ = 𝐕₁ / ‖𝐕₁‖\n")
    utility.show_vectors(
        vector,[] ,start="∴ 𝑢₁ =", colour="bold green", is_row_vector=True
    )

