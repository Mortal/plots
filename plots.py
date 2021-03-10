import re

import matplotlib

with open("figureheight.tex") as fp:
    figureheight_tex, legendheight_tex = fp.readlines()[:2]

fig_height_pt = float(re.search(r"(\d+\.?\d*)pt", figureheight_tex).group(1))
legend_height_pt = float(re.search(r"(\d+\.?\d*)pt", legendheight_tex).group(1))


def matplotlib_setup():
    fig_width_pt = 341.0 * 0.5
    inches_per_pt = 1.0 / 72.27
    # golden_mean = (math.sqrt(5) - 1.0) / 2.0
    fig_width = fig_width_pt * inches_per_pt
    # fig_height = fig_width * golden_mean
    fig_height = fig_height_pt * inches_per_pt
    # print(fig_height / inches_per_pt)
    fig_size = [fig_width, fig_height]

    matplotlib.use("ps")
    matplotlib.rc("font", size=6, family="serif")
    matplotlib.rc("axes", labelsize=6)
    matplotlib.rc("legend", fontsize=8)
    matplotlib.rc("xtick", labelsize=6)
    matplotlib.rc("ytick", labelsize=6)
    matplotlib.rc("text", usetex=True)
    matplotlib.rc("figure", figsize=fig_size)
    matplotlib.rc("savefig", dpi=300)
    # matplotlib.rc('text.latex', preamble=r'\usepackage[T1]{fontenc}')


matplotlib_setup()

import matplotlib.pyplot as plt


def plot_init(xlabel, ylabel, legend_rows=1):
    inches_per_pt = 1.0 / 72.27
    legend_width_pt = 341.0
    legend_size = [
        legend_width_pt * inches_per_pt,
        legend_height_pt * inches_per_pt * legend_rows,
    ]
    figlegend = plt.figure(figsize=legend_size)

    fig, ax = plt.subplots()
    fig.subplots_adjust(left=0.19, bottom=0.15, right=0.95, top=0.96)
    ax.grid()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax, figlegend


fig, ax, figlegend = plot_init(r"My $x$ label", r"My $y$ label")
ax.plot([0, 1, 1, 0], [0, 0, 1, 1], "rx-", label="Some data")
ax.legend(loc="upper right")
fig.savefig("plot.pdf")
