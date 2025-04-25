import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c
import time


#if os.path.exists("results.csv"):  #resetting results file
#    os.remove("results.csv")

for variant in [0, 1, 4]:
    c.fitnessVariants = variant
    print(f"\n>>> Running trials for FITNESS VARIANT {variant}\n")
    for trial in range(5):
        
        print(f"trial: {trial} for variant: {c.fitnessVariants}")
        #deleting files at beginning
        for i in range(c.populationSize * c.numberOfGenerations * 2):  
            brain_filename = f"brain{i}.nndf"
            fitness_filename = f"fitness{i}.txt"
            if os.path.exists(brain_filename):
                os.remove(brain_filename)
            if os.path.exists(fitness_filename):
                os.remove(fitness_filename)

        phc = PARALLEL_HILL_CLIMBER()
        phc.Evolve()
        phc.Show_Best()


        time.sleep(5)

            
        for i in range(c.populationSize * c.numberOfGenerations * 2):
            brain_filename = f"brain{i}.nndf"
            fitness_filename = f"fitness{i}.txt"
            if os.path.exists(brain_filename):
                os.remove(brain_filename)
            if os.path.exists(fitness_filename):
                os.remove(fitness_filename)

        print("program done")   
    print(f"all trials for variant {variant} done")
print("\n\n------\n\n------------\n\n---------------FINISHED\n\n-----------\n\n-----------\n\n\n")