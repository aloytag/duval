# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


def graficar_duval(concentraciones_relativas):
    A = np.array([[5, 2.5, 50], [0, 5 * np.sqrt(3) / 2, 50], [0, 0, 1]])
    p = np.array([
        [0, 0, 1],  # 0-p1
        [0, 100, 1],  # 1-p2
        [100, 0, 1],  # 2-p3
        [0, 87, 1],  # 3-p4
        [0, 96, 1],  # 4-p5
        [0, 98, 1],  # 5-p6
        [2, 98, 1],  # 6-p7
        [23, 0, 1],  # 7-p8
        [23, 64, 1],  # 8-p9
        [20, 76, 1],  # 9-p10
        [20, 80, 1],  # 10-p11
        [40, 31, 1],  # 11-p12
        [40, 47, 1],  # 12-p13
        [50, 35, 1],  # 13-p14
        [50, 46, 1],  # 14-p15
        [50, 50, 1],  # 15-p16
        [71, 0, 1],  # 16-p17
        [85, 0, 1]])  # 17-p18
    v = p @ np.transpose(A)

    punto = concentraciones_relativas.to_numpy().T
    sample_point = np.array([punto[-2, 0], punto[-1, 0], 1]) @ np.transpose(A)

    region_PD = v[[5, 1, 6], :]
    region_T1 = v[[4, 5, 6, 10, 9], :]
    region_T2 = v[[9, 10, 15, 14], :]
    region_T3 = v[[13, 15, 2, 17], :]
    region_D1 = v[[0, 3, 8, 7], :]
    region_D2 = v[[7, 8, 12, 11, 16], :]
    region_DT = v[[3, 4, 14, 13, 17, 16, 11, 12], :]

    fig, ax = plt.subplots(figsize=(6, 6), tight_layout=True)
    ax.fill(region_PD[:, 0], region_PD[:, 1], '#2e962d')
    ax.fill(region_T1[:, 0], region_T1[:, 1], '#bebe12')
    ax.fill(region_T2[:, 0], region_T2[:, 1], '#ff642b')
    ax.fill(region_T3[:, 0], region_T3[:, 1], '#b46414')
    ax.fill(region_D1[:, 0], region_D1[:, 1], '#10b4a7')
    ax.fill(region_D2[:, 0], region_D2[:, 1], '#121eb4')
    ax.fill(region_DT[:, 0], region_DT[:, 1], '#f217d0')
    ax.scatter(sample_point[0], sample_point[1], marker='o', s=50, c='r', zorder=2)
    # ax.grid(linestyle='--', alpha=0.4, axis='both')

    label1 = np.array([45, -5, 1]) @ np.transpose(A)
    ax.text(label1[0], label1[1], '%C2H2')
    label11 = np.array([95, -5, 1]) @ np.transpose(A)
    ax.text(label11[0], label11[1], '0')
    label12 = np.array([5, -5, 1]) @ np.transpose(A)
    ax.text(label12[0], label12[1], '100')
    label2 = np.array([-10, 55, 1]) @ np.transpose(A)
    ax.text(label2[0], label2[1], '%CH4')
    label21 = np.array([-7, 5, 1]) @ np.transpose(A)
    ax.text(label21[0], label21[1], '0')
    label22 = np.array([-7, 95, 1]) @ np.transpose(A)
    ax.text(label22[0], label22[1], '100')
    label3 = np.array([45, 55, 1]) @ np.transpose(A)
    ax.text(label3[0], label3[1], '%C2H4')
    label31 = np.array([5, 95, 1]) @ np.transpose(A)
    ax.text(label31[0], label31[1], '0')
    label22 = np.array([95, 5, 1]) @ np.transpose(A)
    ax.text(label22[0], label22[1], '100')

    ax.set_xlim(0, 600)
    ax.set_ylim(0, 550)
    # plt.grid(False)  # Escondo grilla
    plt.axis('off')  # Escondo ejes

    return fig, ax
