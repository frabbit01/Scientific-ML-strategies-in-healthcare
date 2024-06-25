
#simple code for opening images, I want to use this as base for a method "open segmented image" in one of the derived classes
import numpy as np
import vtk
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Read the VTK file
filename = 'Mesh_10954794.vtk'

reader = vtk.vtkGenericDataObjectReader()
reader.SetFileName(filename)
reader.Update()

# Step 2: Extract points
vtk_points = reader.GetOutput().GetPoints().GetData()

# Convert the vtkArray to a NumPy array
points = np.zeros((vtk_points.GetNumberOfTuples(), 3))
for i in range(vtk_points.GetNumberOfTuples()):
    points[i] = vtk_points.GetTuple(i)

# Step 3: Plot the points using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(points[:, 0], points[:, 1], points[:, 2], marker='o')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()


#I need to keep the information about color!
