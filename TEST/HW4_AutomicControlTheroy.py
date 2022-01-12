import matplotlib.pyplot as plt
import math


def main():
    circle = plt.Circle((-2, 0), math.sqrt(2), color="b", fill=False)
    fig, ax = plt.subplots()
    # note we must use plt.subplots, not plt.subplot
    # (or if you have an existing figure)
    # fig = plt.gcf()
    # ax = fig.gca()
    plt.xlim(-4.0, 0)
    plt.ylim(-2.0, 2.0)
    plt.grid(linestyle='--')
    ax.set_aspect(1)  # let the real axis is in same scale with imaginary axis
    ax.add_patch(circle)
    plt.title('20210705_Hw4', fontsize=8)
    fig.savefig('20210705_plotcircles.png')
    plt.show()


if __name__ == "__main__":
    main()
