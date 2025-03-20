import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c
import time

# for _ in range(5):
#     os.system("python generate.py")
#     os.system("python simulate.py")

phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()


time.sleep(2)

    
for i in range(c.populationSize):
     brain_filename = f"brain{i}.nndf"
     fitness_filename = f"fitness{i}.txt"
     if os.path.exists(brain_filename):
         os.remove(brain_filename)
         print(f"Deleted {brain_filename}")
     if os.path.exists(fitness_filename):
         os.remove(fitness_filename)
         print(f"Deleted {fitness_filename}")

print("program done")   