import utility, gauss_jordan_elimination, inverse, determinant, rank, rref, transpose, identity, LUDecomposition, ker_img, ref
import dot_product, cross_product, angle_bet_vectors, unit_vector
import projection, reflection, rotation
from rich.console import Console
from pyfiglet import figlet_format

console = Console()


def vector_functions() -> None:

    vector_options = [
        "Dot Product .",
        "Cross Product ⨯",
        "Angle between two vectors θ",
        "Unit Vector 𝑢",
        "Projection onto a vector 𝑽",
        "Reflection about a vector 𝑽",
        "Reflection about a plane ⊥ 𝑽",
        "Rotation by θ to vector 𝑽",
    ]

    vector_fun = [
        dot_product.main,
        cross_product.main,
        angle_bet_vectors.main,
        unit_vector.main,
        projection.vector,
        lambda: reflection.vector(about_plane=False),
        lambda: reflection.vector(about_plane=True),
        rotation.rotation,
    ]

    console.print(f"  [bold magenta]Vector Functions :")

    for i, option in enumerate(vector_options, 1):
        console.print(f"  [magenta]{i}) {option}")

    choose = utility.input_int("\n  [magenta]Choose : ") - 1
    console.print("")

    if choose in range(len(vector_fun)):
        vector_fun[choose]()
    else:
        console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")


def matrix_functions() -> None:

    matrix_options = [
        "Solving Systems Of Linear Equations 𝑨𝑿 = 𝑩",
        "Matrix Inverse 𝑨⁻¹",
        "Determinant det(𝑨)",
        "Matrix Rank 𝑟(𝑨)",
        "Row Echelon Form 𝑹𝑬𝑭",
        "Reduced Row Echelon Form 𝑹𝑹𝑬𝑭",
        "Kernel And Image of 𝑨",
        "Matrix Transpose 𝑨ᵀ",
        "Identity Matrix 𝑰",
        "LU Decomposition 𝑨 = 𝑳𝑼",
        "Projection Matrix proj(𝑨)",
        "Reflection Matrix about a vector 𝑽 ref(𝑨)",
        "Reflection Matrix about a plane ⊥ 𝑽 ref(𝑨)",
    ]

    matrix_fun = [
        gauss_jordan_elimination.main,
        inverse.main,
        determinant.main,
        rank.main,
        ref.main,
        rref.main,
        ker_img.main,
        transpose.main,
        identity.main,
        LUDecomposition.main,
        projection.matrix,
        lambda: reflection.matrix(about_plane=False),
        lambda: reflection.matrix(about_plane=True),
    ]

    console.print(f"  [bold magenta]Matrix Functions :")

    for i, option in enumerate(matrix_options, 1):
        console.print(f"  [magenta]{i}) {option}")

    choose = utility.input_int("\n  [magenta]Choose : ") - 1

    console.print("")

    if choose in range(len(matrix_fun)):
        matrix_fun[choose]()

    else:
        console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")


utility.greeting("Welcome To Linear Algebra Helper, My Summer Project :)")

mod_options = ["Matrix []", "Vector →"]
mod_fun = [matrix_functions, vector_functions]

console.print(f"  [bold magenta]Mods : ")

for i, option in enumerate(mod_options, 1):
    console.print(f"  [magenta]{i}) {option}")

choose = utility.input_int("\n  [magenta]Choose : ") - 1
console.print("")


if choose in range(len(mod_fun)):
    mod_fun[choose]()
else:
    console.print(f"[yellow]{figlet_format("Linear Algebra Helper")}")
