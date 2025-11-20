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
[x] Other (please specify): suggesting code for domain for remapping numbers of the original curve

"""  

import Rhino.Geometry as rg
import math

crv = x
N = y

def create_polyline_segments(input_crv, num_segments):
    if not input_crv or num_segments is None or num_segments < 1:
        return []

    original_domain = input_crv.Domain

    num_points = num_segments + 1
    step_size = 1.0 / num_segments

    points = []
    
    for i in range(num_points):
        normalized_t = i * step_size

        if i == num_segments:
            normalized_t = 1.0

        t_actual = input_crv.Domain.ParameterAt(normalized_t)        

        P = input_crv.PointAt(t_actual)
        points.append(P)

    lines = []
    
    for i in range(num_segments):
        start_point = points[i]
        end_point = points[i+1]
        
        line = rg.Line(start_point, end_point)
        lines.append(line)

    if len(points) >= 2:
        for i in range(num_segments):
            if i + 1 < len(points):
                start_point = points[i]
                end_point = points[i+1]
                
                line = rg.Line(start_point, end_point)
                lines.append(line)

    return lines

a = create_polyline_segments(crv, N)