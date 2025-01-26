import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = .5
pyrosim.Start_SDF("boxes.sdf")

for x in range(5):
    for y in range(5):
        length = 1
        width = 1
        height = 1
        for z in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            length *= .90
            width *= .90
            height *= .90
            z += 1
        y += 1
    x += 1
pyrosim.End()