import numpy as np
import matplotlib.pyplot as plt

materials = ["Tabletop", "Plastic", "Wooden"]

SHOW_ORIGINAL_GRAPHS = False
SHOW_UPDATED_GRAPHS = True

original_matrix = [[np.loadtxt(f"./s/s{mat_num+1}_{tst_num+1}.txt",delimiter=",") for tst_num in range(5)] for mat_num in range(3)]
updated_matrix = [[np.loadtxt(f"./u/u{mat_num+1}_{tst_num+1}.txt",delimiter=",") for tst_num in range(5)] for mat_num in range(3)]

def display_graphs(mx):
    for mat_num in range(3):
        for tst_num in range(5):
            time_arr = mx[mat_num][tst_num][:,0]
            pos_arr = mx[mat_num][tst_num][:,1]
            plt.scatter(time_arr,pos_arr)
            plt.title(f"Position vs Time — Material {mat_num+1} ({materials[mat_num]}), Test {tst_num+1}")
            plt.xlabel(f"Time")
            plt.ylabel(f"Position")
            plt.show()

if SHOW_ORIGINAL_GRAPHS: display_graphs(original_matrix)
if SHOW_UPDATED_GRAPHS: display_graphs(updated_matrix)


