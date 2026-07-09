import utility
from rich.console import Console
from fractions import Fraction

console = Console()


def dot(vectors: utility.Matrix) -> Fraction:
    return Fraction(sum(x * y for x, y in zip(*vectors)))


def dot_product() -> tuple[Fraction, utility.Matrix]:

    n = utility.input_int("Enter 𝑛 : ")
    vectors = utility.read_equations(2, n, msg="Vector")

    utility.show_vectors(vectors, "𝐕₁ =", " 𝐕₂ =", is_row_vector=True)

    dot_msg = "  ∵ 𝐕₁.𝐕₂ = " + " + ".join(
        f"({utility.show_num(x)} * {utility.show_num(y)})" for x, y in zip(*vectors)
    )
    console.print(f"[bold cyan]{dot_msg}", end="\n\n")

    product = dot(vectors)

    console.print(f"  [bold green]∴ 𝐕₁.𝐕₂ = {utility.show_num(product)}")

    return (product, vectors)


def main() -> None:

    utility.greeting("Dot Product 𝐕.𝐕₂  ⇒ 𝐕 ∈ ℝⁿ  :) ")

    dot_product()

    console.print("[dim]=" * 48)
