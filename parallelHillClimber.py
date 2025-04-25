from solution import SOLUTION
import constants as c
import copy
import os
import time
import csv
class PARALLEL_HILL_CLIMBER:
    
    def __init__(self):
        for i in range(c.populationSize):
            brain_filename = "brain" + str(i) + ".nndf"
            fitness_filename = f"fitness" + str(i) + ".txt"
            if os.path.exists(brain_filename):
                os.remove(brain_filename)               #deleting files
            if os.path.exists(fitness_filename):
                os.remove(fitness_filename)
        self.parents = {}

        self.nextAvailableID = 0

        for i in range(c.populationSize):
            self.parents[i] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
    def Evolve(self):
        self.Evaluate(self.parents)

        for i in self.parents:
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()
        
            
    def Spawn(self):
        self.children = {} 

        for i in self.parents:
            self.children[i] = copy.deepcopy(self.parents[i])  
            self.children[i].Set_ID(self.nextAvailableID)  
            self.nextAvailableID += 1 


    def Mutate(self):
        for i in self.children: 
            self.children[i].Mutate()  

    def Select(self):
        for key in self.parents:
            if self.children[key].fitness < self.parents[key].fitness: 
                self.parents[key] = self.children[key]

    def Print(self):

        print()  
        for key in self.parents:
            print(self.parents[key].fitness, self.children[key].fitness)
        print()  

    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation("DIRECT")  

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()
    def Show_Best(self):

        best_key = None
        best_fitness = 1000

        for key in self.parents:
            if self.parents[key].fitness < best_fitness:
                best_fitness = self.parents[key].fitness
                best_key = key

        self.parents[best_key].Generate_Brain()
        self.parents[best_key].Start_Simulation("DIRECT")
        self.parents[best_key].Wait_For_Simulation_To_End()

        if not os.path.exists("results.csv"):
            with open("results.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Variant", "TrialID", "Distance", "Movement Ratio", "Fitness"])
        with open("results.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([c.fitnessVariants, best_key,
                            self.parents[best_key].distance,
                            self.parents[best_key].movement_ratio,
                            self.parents[best_key].fitness])
