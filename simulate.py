from simulation import SIMULATION
import sys
import pybullet as p
import pybullet_data

directOrGUI = sys.argv[1] 
solutionID = sys.argv[2] 


simulation = SIMULATION(directOrGUI, solutionID)
simulation.run()
simulation.Get_Fitness()