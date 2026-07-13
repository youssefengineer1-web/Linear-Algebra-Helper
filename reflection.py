import utility
from rich.console import Console
import projection

console = Console()


def vector(about_plane: bool):

    msg = "a plane ⊥ 𝑽" if about_plane else "𝑽"

    vectors = projection.vector("proj(𝑿)", f"Reflection of 𝑿 about {msg} ⇒ 𝐕 ∈ ℝⁿ  :)")

    if about_plane:

        for i in range(len(vectors[0])):
            vectors[0][i] -= 2 * vectors[1][i]

        console.print(f"\n  [bold cyan]∵ 𝑻(𝑿) = 𝑿 - 2 * proj(𝑿)\n")

    else:
        for i in range(len(vectors[0])):
            vectors[0][i] = 2 * vectors[1][i] - vectors[0][i]

        console.print(f"\n  [bold cyan]∵ 𝑻(𝑿) = 2 * proj(𝑿) - 𝑿\n")

    utility.show_vectors(vectors[:1], [],"∴ 𝑻(𝑿) = ", is_row_vector=True)


def matrix(about_plane: bool):

    msg = "a plane ⊥ 𝑽" if about_plane else "𝑽"

    identity, proj_matrix = projection.matrix(
        "proj", f"Reflection Matrix about {msg} ⇒ 𝐕 ∈ ℝⁿ  :)"
    )
    n = len(proj_matrix)

    if about_plane:

        for i in range(n):
            for j in range(n):
                identity[i][j] -= 2 * proj_matrix[i][j]

        console.print(f"\n  [bold cyan]∵ ref(𝑨) = 𝑰 - 2 * proj(𝑨)\n")

    else:

        for i in range(n):
            for j in range(n):
                identity[i][j] = 2 * proj_matrix[i][j] - identity[i][j]

        console.print(f"\n  [bold cyan]∵ ref(𝑨) = 2 * proj(𝑨) - 𝑰\n")

    console.print("  [bold green]∴ ref(𝑨) = \n")

    utility.show(identity, n, [], -2)

