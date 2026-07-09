import utility
from fractions import Fraction

c1 = "𝑎 𝑏 𝑐 𝑑 𝑒 𝑓 𝑔 𝒉 𝑖 𝑗 𝑘 𝑙 𝑚 𝑛 𝑜 𝑝 𝑞 𝑟 𝑠 𝑡 𝑢 𝑣 𝑤 𝑥 𝑦 𝑧"
c2 = "𝑨 𝑩 𝑪 𝑫 𝑬 𝑭 𝑮 𝑯 𝑰 𝑱 𝑲 𝑳 𝑴 𝑵 𝑶 𝑷 𝑸 𝑹 𝑺 𝑻 𝑼 𝑽 𝑾 𝑿 𝒀 𝒁"
d1 = "⁰ ¹ ² ³ ⁴ ⁵ ⁶ ⁷ ⁸ ⁹ ⁻"


print(f"{112.344556788765e8: .12g}")
print(f"{112.344556788765e8:g}")
print(f"{112.344556788765e8: .12f}")
print(f"{112.344556788765e8: .12e}")
print(f"{112.344556788765e8}")
print(f"{112.344556788765: g}")


arr: list[int | str] = [1]


utility.show(
    [
        [Fraction(1), Fraction(0), Fraction(0)],
        [" ", Fraction(1), Fraction(0)],
        [" ", " ", Fraction(1)],
    ],
    3,
    [0, 1, 2],
)

l = [i for x in range(10) for i in range(x)]

