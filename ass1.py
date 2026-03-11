from CoolProp.CoolProp import PropsSI
import numpy as np
import csv


def generate_dataset(fluid, T_range, P_range, filename):

    data = []

    for T in T_range:
        for P in P_range:
            try:
                rho = PropsSI("D", "T", T, "P", P, fluid)

                data.append([T, P, rho])

            except:

                continue


    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        writer.writerow(["Temperature (K)", "Pressure (Pa)", "Density (kg/m3)"])

        writer.writerows(data)

    print(f"{filename} saved successfully. Total points:", len(data))




# Methane
T_methane = np.linspace(150, 400, 40)
P_methane = np.linspace(1e5, 5e6, 40)

# R134a
T_r134a = np.linspace(250, 400, 40)
P_r134a = np.linspace(1e5, 3e6, 40)



generate_dataset("Methane", T_methane, P_methane, "methane_dataset.csv")

generate_dataset("R134a", T_r134a, P_r134a, "r134a_dataset.csv")
