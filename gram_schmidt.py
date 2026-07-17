import utility
from rref import gauss_jordan as reduced_row_echelon_form
from transpose import transpose
from unit_vector import unit_vector
from dot_product import dot
from ker_img import show_kernel
from gauss_jordan_elimination import gauss_jordan
from rich.console import Console

console = Console()


def show_dependent(
    rref: utility.Matrix, vector_count: int, pivot_indices: list[int]
) -> list[int]:

    dependent_vectors = [i for i in range(vector_count) if i not in pivot_indices]

    console.print("  [bold yellow] Dependent Vectors : \n")
    for v in dependent_vectors:
        equ = []

        for i, pivot in enumerate(pivot_indices):
            if not utility.is_zero(rref[i][v]):
                equ.append(
                    utility.lower_num(utility.Fraction(rref[i][v]), "𝑽", pivot + 1)
                )

        console.print(
            f"  [bold cyan] {utility.lower_num(utility.Fraction(1),"𝑽",v+1)} = {' + '.join(equ) if equ else '0'}"
        )

    console.print("[dim]=" * 48)

    return dependent_vectors


def gram_schmidt(vectors: utility.Matrix, unit_vectors: utility.Matrix, start: int = 1):

    vectors = [vector.copy() for vector in vectors]

    sym_u = [
        f" {utility.lower_num(utility.Fraction(1),"𝑢",v+1)} ="
        for v in range(len(vectors))
    ]
    low_num = [str(v + 1).translate(utility.SUB) for v in range(len(vectors))]

    for i in range(start, len(vectors)):

        text_1 = [f"∵ 𝐕{low_num[i]}⊥ = 𝐕{low_num[i]}"]
        v = ",".join(
            f"[bold cyan]{utility.show_num(n)}[/bold cyan]" for n in vectors[i]
        )
        text_2 = [f"∴ 𝐕{low_num[i]}⊥ = ({v})"]

        for j in range(i):
            u = ",".join(
                f"[bold cyan]{utility.show_num(n)}[/bold cyan]" for n in unit_vectors[j]
            )
            text_1.append(f"(𝑢{low_num[j]}·𝐕{low_num[i]})𝑢{low_num[j]}")
            text_2.append(f"(({u})·({v}))({u})")
            prod = dot([unit_vectors[j], vectors[i]])
            gram = [n * prod for n in unit_vectors[j]]

            for k in range(len(vectors[i])):
                vectors[i][k] -= gram[k]

        console.print(f"  [bold cyan]{" - ".join(text_1)}\n")
        console.print(f"  [bold]{" - ".join(text_2)}\n")
        utility.show_vectors(
            [vectors[i]], [], f"∴ 𝐕{low_num[i]}⊥ =", is_row_vector=True
        )
        unit_vectors.append(unit_vector(vectors[i], i + 1))

    utility.show_vectors(
        unit_vectors,
        sym_u[1:],
        sym_u[0],
        "    ,",
        is_row_vector=True,
    )


def main() -> None:

    pivot_indices = []

    utility.greeting("Gram Schmidt :)")

    vector_count = utility.input_int("Enter Number Of Vectors : ")
    dim = utility.input_int("Enter Vectors Diminsions : ")

    vectors = utility.read_equations(vector_count, dim, msg="Vector")
    matrix = transpose(vectors)
    rref = [row.copy() for row in matrix]

    utility.show(matrix, vector_count, pivot_indices)

    reduced_row_echelon_form(rref, pivot_indices)

    utility.show(rref, vector_count, pivot_indices)

    rank = len(pivot_indices)
    nullity = vector_count - rank

    console.print(f"  [bold cyan]Rank    = {rank}")
    console.print(f"  [bold cyan]Nullity = {nullity}\n")
   

    if nullity != 0:
        dependent_vectors = show_dependent(rref, vector_count, pivot_indices)

        for v in reversed(dependent_vectors):
            del vectors[v]
            

    console.print(f"  [bold green]Linear Independent Vectors :")
    independent_vectors = [
        f" {utility.lower_num(utility.Fraction(1),"𝑽",pivot+1)} ="
        for pivot in pivot_indices
    ]
    utility.show_vectors(
        vectors,
        independent_vectors[1:],
        independent_vectors[0],
        "    ,",
        is_row_vector=True,
    )

    orthonormal_basis = [unit_vector(vectors[0].copy())]
    gram_schmidt(vectors, orthonormal_basis)

    if len(vectors) < len(vectors[0]):

        console.print("  [bold green]Orthogonal Complements : \n")

        pivot_indices = []
        A = [vector.copy() + [utility.Fraction(0)] for vector in vectors]
        gauss_jordan(A, pivot_indices)
        kernel = show_kernel(A, pivot_indices, "𝑾 ⊥")
        vectors.extend(kernel)
        orthonormal_basis.append(unit_vector(kernel[0], len(orthonormal_basis) + 1))
        gram_schmidt(vectors, orthonormal_basis, len(orthonormal_basis))
