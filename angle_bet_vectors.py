import utility
from rich.console import Console
from fractions import Fraction
from math import acos, degrees
from dot_product import dot_product

console = Console()


def main() -> None:

    utility.greeting("Angle Between 𝐕₁ & 𝐕₂  ⇒ 𝐕 ∈ ℝⁿ  :) ")

    dot, vectors = dot_product()

    text1 = " + ".join(f"({utility.show_num(num)})²" for num in vectors[0])
    text2 = " + ".join(f"({utility.show_num(num)})²" for num in vectors[1])

    v1 = Fraction(sum(i * i for i in vectors[0]) ** 0.5)
    v2 = Fraction(sum(i * i for i in vectors[1]) ** 0.5)

    cos = dot / (v1 * v2)
    angle = acos(cos)

    console.print(f"\n  ∵ ‖𝐕₁‖ = √({text1}) = {utility.show_num(v1)}")
    console.print(f"  ∵ ‖𝐕₂‖ = √({text2}) = {utility.show_num(v2)}\n")

    console.print("  [cyan]∵ 𝐕₁·𝐕₂ = ‖𝐕₁‖‖𝐕₂‖ * cos(θ)")
    console.print("  [cyan]∴ cos(θ) = 𝐕₁·𝐕₂ / (‖𝐕₁‖‖𝐕₂‖)\n")

    console.print(
        f"  [green]∴ cos(θ) = {utility.show_num(dot)} / ({utility.show_num(v1)} * {utility.show_num(v2)})"
    )

    console.print(f"  [green]∴ cos(θ) = {utility.show_num(cos)}\n")

    console.print(
        f"  [bold green]∴ θ = {utility.show_num(Fraction(angle))} rad = {utility.show_num(Fraction(degrees(angle)))}°"
    )

    console.print("[dim]=" * 48)
