from simulation import SIMULATION
import sys
import pybullet as p
import pybullet_data
import os

directOrGUI = sys.argv[1] 
solutionID = sys.argv[2] 


simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()
simulation.Get_Fitness()


os.remove(f"body{solutionID}.urdf")
os.remove(f"world{solutionID}.sdf")
