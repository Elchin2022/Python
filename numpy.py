
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "sans-serif"
plt.rcParams["font.sans-serif"] = "OpenSans-Regular"

FONTSIZE = 16


L = 30
x = np.linspace(0, L / 2, num=2 ** 10)
V = lambda x, L: (L - 2 * x) ** 2 * x

fig = plt.figure(figsize=(5, 4))
plt.title("Volume as a function of $x$", fontsize=FONTSIZE)

plt.plot(x, V(x, L), label="$V(x)$", lw=3)
plt.scatter(L / 6, V(L / 6, L), lw=3, color="red", zorder=15)
plt.plot([L / 6, L / 6], [0, V(L / 6, L)], "--", lw=2, color="red", zorder=15)

plt.legend(loc="best", fontsize=FONTSIZE)
plt.xlabel("$x$", fontsize=FONTSIZE)
plt.ylabel("Volume of box", fontsize=FONTSIZE)

plt.xticks(
    [0, L / 6, 2 * L / 6, L / 2], ["0", "$L/6$", "$L/3$", "$L/2$"], fontsize=FONTSIZE
)

arr, labels = plt.yticks()
plt.yticks(arr, ["" for i in arr])

plt.grid(True, zorder=-15, ls="--")
plt.tight_layout()
#plt.savefig("paper_box_volume.pdf")
plt.show()
