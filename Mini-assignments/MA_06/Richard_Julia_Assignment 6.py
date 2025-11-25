"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) Gemini
[x] Explaining programming concepts
[] Practicing coding exercises
[x] Debugging code
[x] Reviewing your Python code
[] Optimizing code
[] Writing or completing code
[x] Other (please specify): failsafing code for errors; python and grasshopper did not want to read AreaMassPoperties.Compute as a mesh, only a curve, so how to manually calculate area of every mesh face

"""  

import Rhino.Geometry as rg


#Task 1

def mesh_face_centroids(bunny_mesh: rg.Mesh):
    centroids = []
    
    if bunny_mesh is None or not bunny_mesh.IsValid:
        return []
        
    face_list = bunny_mesh.Faces

    for i in range(face_list.Count):
        centroid_point = face_list.GetFaceCenter(i)
        centroids.append(centroid_point)

    return centroids

#Task 2

def find_largest_face_index(bunny_mesh: rg.Mesh) -> int:
    if not isinstance(bunny_mesh, rg.Mesh) or not bunny_mesh.IsValid:
        return -1
    
    max_area=0.0
    largest_face_index= -1
    face_list=bunny_mesh.Faces
    vertices=bunny_mesh.Vertices

    for i in range(face_list.Count):
        face=face_list[i]

        if not face.IsTriangle:
            if not face.IsQuad:
                continue

        vA=vertices[face.A]
        vB=vertices[face.B]
        vC=vertices[face.C]

        u=vB-vA
        v=vC-vA

        cross_product=rg.Vector3d.CrossProduct(u,v)
        current_area=0.5*cross_product.Length

        if current_area>max_area:
            max_area=current_area
            largest_face_index=i

    return largest_face_index

def create_centroid_line(bunny_mesh: rg.Mesh, index: int, line_length: float) -> (rg.Point3d, rg.Line):
    if index== -1:
        return None, None
    
    face_list=bunny_mesh.Faces

    centroid=face_list.GetFaceCenter(index)

    bunny_mesh.FaceNormals.ComputeFaceNormals()
    normal_vector=bunny_mesh.FaceNormals[index]

    normal_vector.Unitize()
    normal_vector*=line_length

    end_point=centroid+normal_vector
    extrusion_line=rg.Line(centroid, end_point)

    return centroid, extrusion_line

#Task 3

# def attract_mesh_vertices(bunny_mesh: rg.Mesh, attractor_point: rg.Point3d, max_distance: float):
#     if not bunny_mesh or not bunny_mesh.IsValid:
#         return bunny_mesh
    
#     vertices = bunny_mesh.Vertices
#     new_vertex_list = [] # Initialize a new list to store modified Point3f objects

#     for i in range(vertices.Count):
#         current_vertex=vertices[i]
#         distance=current_vertex.DistanceTo(attractor_point)

#         modified_position=current_vertex 

#         if distance<=max_distance and distance>0:
#             attraction_vector=attractor_point-current_vertex
            
#             new_position_3d=current_vertex+(attraction_vector*0.5) 
            
#             modified_position=rg.Point3f(new_position_3d.X, new_position_3d.Y, new_position_3d.Z)

#         new_vertex_list.append(modified_position)

#     bunny_mesh.Vertices.Clear()
#     bunny_mesh.Vertices.AddVertices(new_vertex_list)
#     bunny_mesh.Normals.ComputeNormals()
#     bunny_mesh.FaceNormals.ComputeFaceNormals()
#     bunny_mesh.Compact()

#     return bunny_mesh

a = []
b=None
c=None

# ATTRACTION_RADIUS=1

#Outputs

if "bunny_mesh" in globals() and bunny_mesh is not None:
    # modified_mesh=bunny_mesh.DuplicateMesh()
    
    # if "attractor" in globals() and attractor is not None:
    #     modified_mesh=attract_mesh_vertices(modified_mesh, attractor, ATTRACTION_RADIUS)
    
    a=mesh_face_centroids(bunny_mesh)

    if "l" in globals():
        largest_index=find_largest_face_index(bunny_mesh) 

        if largest_index!= -1:
            largest_centroid, line_out=create_centroid_line(bunny_mesh, largest_index, l) 

            b=largest_centroid
            c=line_out