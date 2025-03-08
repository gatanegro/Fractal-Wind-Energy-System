import numpy as np
import trimesh

# Step 2: Generating STL Files for Boomerang and Spiral Geometries

# 1. Boomerang Geometry
def create_boomerang_stl(file_path):
    # Define boomerang curve parameters
    x = np.linspace(-1, 1, 200)
    y = -np.abs(x) + 1  # Boomerang shape
    z = np.zeros_like(x)

    # Thickness and extrusion
    thickness = 0.2  # Adjust thickness of the boomerang
    extrusion_depth = 0.5  # Extrusion along the Z-axis

    # Generate vertices for top and bottom surfaces
    vertices_top = np.array([x, y, z]).T
    vertices_bottom = np.array([x, y, z - thickness]).T

    # Combine top and bottom vertices
    vertices = np.vstack([vertices_top, vertices_bottom])

    # Create faces to connect the top and bottom surfaces
    num_points = len(x)
    faces = []
    for i in range(num_points - 1):
        # Top surface triangle
        faces.append([i, i + 1, num_points + i])
        # Bottom surface triangle
        faces.append([i + 1, num_points + i + 1, num_points + i])
        # Side faces to close the extrusion
        faces.append([i, num_points + i, num_points + i + 1])
        faces.append([i, num_points + i + 1, i + 1])

    # Create the 3D mesh
    boomerang_mesh = trimesh.Trimesh(vertices=vertices, faces=np.array(faces))
    boomerang_mesh.export(file_path)


# 2. Spiral Geometry
def create_spiral_stl(file_path):
    # Spiral parameters
    num_turns = 4
    num_points = 500
    radius = np.linspace(0.1, 1.0, num_points)
    theta = np.linspace(0, num_turns * 2 * np.pi, num_points)
    z = np.linspace(0, 0.5, num_points)  # Height for 3D effect

    # Generate spiral vertices
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Create vertices for the spiral
    vertices = np.array([x, y, z]).T

    # Create faces by connecting consecutive points
    faces = []
    for i in range(len(vertices) - 1):
        faces.append([i, i + 1, i + 2])

    # Create the 3D mesh
    spiral_mesh = trimesh.Trimesh(vertices=vertices, faces=np.array(faces))
    spiral_mesh.export(file_path)


# File paths for the STL files
boomerang_stl_path = "/mnt/data/Boomerang_Geometry.stl"
spiral_stl_path = "/mnt/data/Spiral_Geometry.stl"

# Generate STL files
create_boomerang_stl(boomerang_stl_path)
create_spiral_stl(spiral_stl_path)

boomerang_stl_path, spiral_stl_path

def create_spiral_stl_fixed(file_path):
    # Spiral parameters
    num_turns = 4
    num_points = 500
    radius = np.linspace(0.1, 1.0, num_points)
    theta = np.linspace(0, num_turns * 2 * np.pi, num_points)
    z = np.linspace(0, 0.5, num_points)  # Height for 3D effect

    # Generate spiral vertices
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # Create vertices for the spiral
    vertices = np.array([x, y, z]).T

    # Create faces by connecting consecutive points into triangles (for a fan-like effect)
    faces = []
    for i in range(len(vertices) - 2):
        faces.append([i, i + 1, i + 2])

    # Create the 3D mesh
    spiral_mesh = trimesh.Trimesh(vertices=vertices, faces=np.array(faces))
    spiral_mesh.export(file_path)


# Regenerate spiral STL file with corrected logic
create_spiral_stl_fixed(spiral_stl_path)

boomerang_stl_path, spiral_stl_path