import utility
from rich.console import Console
from fractions import Fraction

console = Console()


def dot(vectors: utility.Matrix) -> Fraction:
    return Fraction(sum(x * y for x, y in zip(*vectors)))


def dot_product(v1: str = "𝐕₁", v2: str = "𝐕₂") -> tuple[Fraction, utility.Matrix]:

    n = utility.input_int("Enter 𝑛 : ")
    vectors = utility.read_equations(2, n, msg="Vector")

    utility.show_vectors(vectors, f"{v1} =", f" {v2} =", is_row_vector=True)

    dot_msg = f"  ∵ {v1}.{v2} = " + " + ".join(
        f"({utility.show_num(x)} * {utility.show_num(y)})" for x, y in zip(*vectors)
    )
    console.print(f"[bold cyan]{dot_msg}", end="\n\n")

    product = dot(vectors)

    console.print(f"  [bold green]∴ {v1}.{v2} = {utility.show_num(product)}")

    return (product, vectors)


def main() -> None:

    utility.greeting("Dot Product 𝐕.𝐕₂  ⇒ 𝐕 ∈ ℝⁿ  :) ")

    dot_product()

    console.print("[dim]=" * 48)
