import open3d as o3d
import numpy as np

# Step 1: Generate a synthetic cylinder point cloud
cylinder_mesh = o3d.geometry.TriangleMesh.create_cylinder(radius=0.2, height=2.0)
cylinder_mesh.compute_vertex_normals()
pcd = cylinder_mesh.sample_points_poisson_disk(number_of_points=1000)

# Add noise
noise = np.random.uniform(-1.0, 1.0, size=(300, 3))
noise_cloud = o3d.geometry.PointCloud()
noise_cloud.points = o3d.utility.Vector3dVector(noise)

# Combine
pcd_combined = pcd + noise_cloud
pcd_combined.paint_uniform_color([0.5, 0.5, 0.5])  # gray base

# Save the point cloud
o3d.io.write_point_cloud("synthetic_cylinder_cloud.ply", pcd_combined)

# Step 2: Visualize
o3d.visualization.draw_geometries([pcd_combined])
