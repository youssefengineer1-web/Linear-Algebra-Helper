import utility
from rich.console import Console
from dot_product import dot_product, dot
from transpose import transpose

console = Console()


def vector(
    text: str = "𝑻(𝑿)", msg: str = "Projection of 𝑿 into  𝐕 ⇒ 𝐕 ∈ ℝⁿ  :)"
) -> utility.Matrix:

    utility.greeting(msg)
    dot, vectors = dot_product("𝑿", "𝐕")
    norm_sq = utility.Fraction(sum(i * i for i in vectors[1]))
    scale = dot / norm_sq

    console.print(
        f"\n  ∵ ‖𝐕‖² = {' + '.join(f'({utility.show_num(i)})²' for i in vectors[1])} = {utility.show_num(norm_sq)}"
    )

    for i in range(len(vectors[1])):
        vectors[1][i] *= scale

    console.print(f"\n  [bold cyan]∵ {text} = (𝑿·𝐕 / ‖𝐕‖²)𝐕")

    console.print(f"\n  [green]∴ {text} = ({utility.show_num(scale)})𝐕\n")

    utility.show_vectors(vectors[1:], [],f"∴ {text} = ", is_row_vector=True)

    return vectors


def matrix(
    text: str = "𝑻", msg: str = "Projection Matrix into 𝑽 ⇒ 𝐕 ∈ ℝⁿ  :)"
) -> tuple[utility.Matrix, utility.Matrix]:

    utility.greeting(msg)

    n = utility.input_int("Enter 𝑛 : ")
    vectors = utility.read_equations(1, n, msg="Vector")

    I = transpose(utility.identity_matrix(n, n))
    norm_sq = utility.Fraction(sum(i * i for i in vectors[0]))  # ‖𝐕‖²
    proj_matrix = []
    vector_str = f"({','.join(str(a) for a in vectors[0])})"

    utility.show_vectors(vectors,[],"𝐕 = ", is_row_vector=True)

    console.print(f"  [bold cyan]∵ {text}(𝑿) = (𝑿·𝐕 / ‖𝐕‖²)𝐕")

    console.print(
        f"\n  ∵ ‖𝐕‖² = {' + '.join(f'({utility.show_num(i)})²' for i in vectors[0])} = {utility.show_num(norm_sq)}"
    )
    console.print("[dim]=" * 48)

    for i in range(n):
        v1 = I[i]
        dot_pro = dot([v1, vectors[0]])
        if norm_sq == 0:
            raise ValueError("Cannot project onto the zero vector.")
        scale = dot_pro / norm_sq
        proj_matrix.append([x * scale for x in vectors[0]])

        show_v1 = f"({",".join(str(a) for a in v1)})"

        dot_msg = (
            f"  [cyan]∵ {show_v1}.{vector_str} = "
            + " + ".join(
                f"({utility.show_num(x)} * {utility.show_num(y)})"
                for x, y in zip(v1, vectors[0])
            )
            + f" = {utility.show_num(dot_pro)}"
        )
        console.print(dot_msg)

        console.print(
            f"\n  [green]∴ {text}({show_v1}) = ({utility.show_num(dot_pro)} / {utility.show_num(norm_sq)})𝐕\n"
        )

        utility.show_vectors(
            proj_matrix[i:], [],f"∴ {text}({show_v1}) = ", is_row_vector=True
        )

    console.print("  [bold green]∴ proj(𝑨) = \n")
    utility.show(proj_matrix, n, [], -2)

    return I, proj_matrix
