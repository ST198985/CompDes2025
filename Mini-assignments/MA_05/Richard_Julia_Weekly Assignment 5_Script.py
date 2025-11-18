import Rhino.Geometry as rg

def approximate_curve_to_polyline(crv, N):
   
    if crv is None or N is None or N <= 0:
        return []

    curve_copy = crv.DuplicateCurve()
    
    if curve_copy is None:
        return []

    curve_copy.Domain = rg.Interval(0.0, 1.0)
    
    success, points, t_values = curve_copy.DivideByCount(N, True)

    lines = []
    if success:
        for i in range(len(points) - 1):
            start_point = points[i]
            end_point = points[i + 1]
            
            line = rg.Line(start_point, end_point)
            lines.append(line)

    return lines

all_lines = []

input_list = crv if isinstance(crv, list) else [crv]

for single_crv in input_list:
    if single_crv is not None and isinstance(single_crv, rg.Curve):
        try:
            lines_for_crv = approximate_curve_to_polyline(single_crv, N)
            all_lines.extend(lines_for_crv)
        except Exception as e:
            pass

a = all_lines