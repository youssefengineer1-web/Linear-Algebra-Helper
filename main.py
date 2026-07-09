import utility, gauss_jordan_elimination, inverse, determinant, rank, rref, transpose, identity, LUDecomposition
import dot_product, cross_product, angle_bet_vectors, unit_vector
from rich.console import Console
from pyfiglet import figlet_format

console = Console()


def vector_functions() -> None:

    vector_options = [
        "Dot Product .",
        "Cross Product ⨯",
        "Angle between two vectors θ",
        "Unit Vector 𝑢",
    ]

    console.print(f"  [bold magenta]Vector Functions :")

    for i, option in enumerate(vector_options, 1):
        console.print(f"  [magenta]{i}) {option}")

    choose = utility.input_int("\n  [magenta]Choose : ")
    console.print("")

    if choose == 1:
        dot_product.main()
    elif choose == 2:
        cross_product.main()
    elif choose == 3:
        angle_bet_vectors.main()
    elif choose == 4 : 
        unit_vector.main()
    else:
        console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")


def matrix_functions() -> None:

    matrix_options = [
        "Solving System Of Linear Equations 𝑨𝑿 = 𝑩",
        "Matrix Inverse 𝑨⁻¹",
        "Determinant det(𝑨)",
        "Matrix Rank 𝑟(𝑨)",
        "Reduced Row Echelon Form 𝑹𝑹𝑬𝑭",
        "Matrix Transpose 𝑨ᵀ",
        "Identity Matrix 𝑰",
        "LU Decomposition 𝑨 = 𝑳𝑼",
    ]

    console.print(f"  [bold magenta]Matrix Functions :")

    for i, option in enumerate(matrix_options, 1):
        console.print(f"  [magenta]{i}) {option}")

    choose = utility.input_int("\n  [magenta]Choose : ")
    console.print("")

    if choose == 1:
        gauss_jordan_elimination.main()
    elif choose == 2:
        inverse.main()
    elif choose == 3:
        determinant.main()
    elif choose == 4:
        rank.main()
    elif choose == 5:
        rref.main()
    elif choose == 6:
        transpose.main()
    elif choose == 7:
        identity.main()
    elif choose == 8:
        LUDecomposition.main()
    else:
        console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")


utility.greeting("Welcome To Linear Algebra Helper, My Summer Project :)")

mod_options = ["Matrix []", "Vector →"]

console.print(f"  [bold magenta]Mods : ")

for i, option in enumerate(mod_options, 1):
    console.print(f"  [magenta]{i}) {option}")

choose = utility.input_int("\n  [magenta]Choose : ")
console.print("")


if choose == 1:
    matrix_functions()
elif choose == 2:
    vector_functions()
else:
    console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")
