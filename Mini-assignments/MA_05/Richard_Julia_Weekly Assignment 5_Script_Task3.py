"""
Questionnaire: For what purposes did you use Generative AI / LLMs when completing your assignment?
[] Not at all
[] Which ones did you use? (e.g., ChatGPT, Bard, etc.) Gemini
[x] Explaining programming concepts
[] Practicing coding exercises
[x] Debugging code
[x] Reviewing your Python code
[x] Optimizing code
[] Writing or completing code
[x] Other (please specify): failsafing code for errors

"""  

import Rhino.Geometry as rg
import math

global_xy_plane=rg.Plane.WorldXY

point_a=rg.Point3d.Origin
vector_offset=rg.Vector3d(x,y,z)
point_b=point_a+vector_offset
line_1=rg.Line(point_a,point_b)

mirror_plane=rg.Plane(point_b, rg.Vector3d(1,0,0))
mirror_transform=rg.Transform.Mirror(mirror_plane)

line_2_start=line_1.From
line_2_start.Transform(mirror_transform)
line_2_end=line_1.To
line_2_end.Transform(mirror_transform)
line_2=rg.Line(line_2_start, line_2_end)

all_line_segments=[]

translation_step_x=x*2
total_x_copies=x_copies+1

for i in range(total_x_copies):
    translation_vector=rg.Vector3d(translation_step_x*i,0,0)
    translation_transform=rg.Transform.Translation(translation_vector)

    start_1 = line_1.From
    start_1.Transform(translation_transform)
    end_1 = line_1.To
    end_1.Transform(translation_transform)
    copied_line_1=rg.Line(start_1, end_1)

    start_2 = line_2.From
    start_2.Transform(translation_transform)
    end_2 = line_2.To
    end_2.Transform(translation_transform)
    copied_line_2=rg.Line(start_2, end_2)

    all_line_segments.extend([copied_line_1, copied_line_2])

curve_segments=[]
for line_segment in all_line_segments:
    curve_segments.append(line_segment.ToNurbsCurve())

joined_curves=rg.Curve.JoinCurves(curve_segments)

base_polyline=None
if joined_curves and joined_curves.Length > 0:
    polyine_creation=joined_curves[0]

    success, polyline_1=polyine_creation.TryGetPolyline()
    if success:
        base_polyline=polyline_1
    else:
        base_polyline=polyine_creation

polyline_list=[]

if base_polyline:
    total_y_copies=y_copies+1

    for j in range(total_y_copies):
        z_shift=0.0
        if j % 2 != 0:
            z_shift=z_factor

        translation_vector_final=rg.Vector3d(0, y_spacing*j, z_shift)
        translate_transform_final=rg.Transform.Translation(translation_vector_final)
        
        copied_polyline=base_polyline.Duplicate()
        copied_polyline.Transform(translate_transform_final)
        
        polyline_list.append(copied_polyline)

connecting_points=[]
new_connecting_polyline=None

if polyline_list:
    for current_polyline in polyline_list:
        end_point=current_polyline[current_polyline.Count-1]
        connecting_points.append(end_point)

    if len(connecting_points) >= 2:
        new_connecting_polyline=rg.Polyline(connecting_points)

connecting_polylines=[]

if new_connecting_polyline and base_polyline:
    ref_point=new_connecting_polyline[0]

    for k in reversed(range(base_polyline.Count)):
        target_point=base_polyline[k]
        x_translation_vector=target_point-ref_point
        x_translation_transform=rg.Transform.Translation(x_translation_vector)

        copied_connecting_polylines=new_connecting_polyline.Duplicate()
        copied_connecting_polylines.Transform(x_translation_transform)

        connecting_polylines.append(copied_connecting_polylines)

a=polyline_list
b=new_connecting_polyline
c=connecting_polylines