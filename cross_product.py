import utility
from rich.console import Console

console = Console()


def main() -> None:

    utility.greeting("Cross Product 𝐕 ⨯ 𝐕  ⇒ 𝐕 ∈ ℝ³  :) ")

    vectors = utility.read_equations(2, 3, msg="Vector")

    utility.show([["𝐢", "𝐣", "𝐤"], *vectors], 3, [], cur_row=-2)  # type: ignore

    strings = [[utility.show_num(num) for num in vector] for vector in vectors]

    widths = utility.get_widths(strings)
    print_num = lambda num, colour, i: f"[{colour}]{num:^{widths[i]}s}[/{colour}]"

    console.print(
        f"            |{print_num(strings[0][1],'cyan',1)} {print_num(strings[0][2],'yellow',2)}|    |{print_num(strings[0][0],'cyan',0)} {print_num(strings[0][2],'yellow',2)}|    |{print_num(strings[0][0],'cyan',0)} {print_num(strings[0][1],'yellow',1)}|"
    )
    console.print(
        f"  [yellow]∵ 𝐕 ⨯ 𝐕 = [/yellow]|{print_num(strings[1][1],'yellow',1)} {print_num(strings[1][2],'cyan',2)}|𝐢 - |{print_num(strings[1][0],'yellow',0)} {print_num(strings[1][2],'cyan',2)}|𝐣 + |{print_num(strings[1][0],'yellow',0)} {print_num(strings[1][1],'cyan',1)}|𝐤"
    )

    console.print(
        f"\n  [bold cyan]∴ 𝐕 ⨯ 𝐕 = ({strings[0][1]} * {strings[1][2]} - {strings[0][2]} * {strings[1][1]})𝐢 - ({strings[0][0]} * {strings[1][2]} - {strings[0][2]} * {strings[1][0]})𝐣 + ({strings[0][0]} * {strings[1][1]} - {strings[0][1]} * {strings[1][0]})𝐤"
    )

    console.print(
        f"\n  [bold green]∴ 𝐕 ⨯ 𝐕 = {utility.show_num(vectors[0][1] * vectors[1][2] - vectors[0][2] * vectors[1][1])}𝐢 + {utility.show_num(-vectors[0][0] * vectors[1][2] + vectors[0][2] * vectors[1][0])}𝐣 + {utility.show_num(vectors[0][0] * vectors[1][1] - vectors[0][1] * vectors[1][0])}𝐤"
    )

    console.print("[dim]=" * 48)
