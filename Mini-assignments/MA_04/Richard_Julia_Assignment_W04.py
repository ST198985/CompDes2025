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
[x] Other (please specify): "import math" - how to import math for volume funtion of cylindrical column("Boom")

"""  


"""In this assignment, you will design a new pavilion inspired by an existing pavilion or project (it does not have to be an ITECH pavilion :D).

You will use object-oriented programming. The components of the pavilion (e.g. columns, beams, roofs, walls) will be modelled as classes and subclasses.
Each component will have parameters (such as dimensions, material type, fabrication methods) that can influence the overall cost and CO2 emissions of the pavilion.
In addition, cost estimates will be updated based on design decisions such as material selection or changes in dimensions.

1. Create the pavilion class. This is the main class that contains the components of the pavilion and provides methods for estimating the total cost, carbon footprint, etc. 
2. Component classes: Each major component (e.g. column, beam, wall) should have its own class that calculates its individual cost, carbon footprint, etc. 
3. Material subclasses: Materials will have different costs and properties that will affect those of the components. 
4. Be creative
5. Upload your assignment to ILIAS and GitHub"""

import math

#Inspo Pavilion: Expo 67 - Ontario Pavilion
class Pavilion:
    def __init__(self, name):
        self.name=name
        self.components=[]

    def add_component(self, component):
        if isinstance(component, Component):
            self.components.append(component)
        else:
            raise TypeError(f"Cannot add item of type {type(component)}. Expected Component.")
    
    def total_volume(self):
        return sum(comp.calculate_volume() for comp in self.components)
    
    def total_weight(self):
        return sum(comp.calculate_weight() for comp in self.components)
    
    def total_cost(self):
        return sum(comp.calculate_cost() for comp in self.components)
    
    def total_co2_footprint(self):
        return sum(comp.calculate_co2_footprint() for comp in self.components)

class Material:
    def __init__(self, name, cost_per_volume, co2_per_volume, density):
        self.name=name
        self.cost_per_volume=cost_per_volume #€/m3
        self.co2_per_volume=co2_per_volume #kg CO2/m3
        self.density=density #kg/m3

    def weight_per_volume(self):
        return self.density

class Component:
    def __init__(self, name, length, width, height, material:Material):
        self.name=name
        self.length=length
        self.width=width
        self.height=height
        self.material=material
    
    def calculate_volume(self):
        return self.length*self.width*self.height
    
    def calculate_weight(self):
        return self.calculate_volume()*self.material.weight_per_volume()
    
    def calculate_cost(self):
        return self.calculate_volume()*self.material.cost_per_volume
    
    def calculate_co2_footprint(self):
        return self.calculate_volume()*self.material.co2_per_volume
    
#Component Types
class Sheet(Component):
    def __init__(self, name, length, width, thickness, material):
        super().__init__(name, length, width, thickness, material)
        self.thickness=thickness

class Boom(Component):
    def __init__(self, name, diameter, height, thickness, material):
        self.diameter=diameter
        self.height=height
        self.thickness=thickness
        self.radius_outer=diameter/2
        self.radius_inner=self.radius_outer-thickness
        super().__init__(name, diameter, diameter, height, material)

    
    def calculate_volume(self):
        volume_outer = math.pi * (self.radius_outer ** 2) * self.height
        volume_inner = math.pi * (self.radius_inner ** 2) * self.height

        return volume_outer-volume_inner
    
class Column(Component):
    def __init__(self, name, diameter, height, thickness, material):
        self.diameter=diameter
        self.height=height
        self.thickness=thickness
        self.radius_outer=diameter/2
        self.radius_inner=self.radius_outer-thickness
        super().__init__(name, diameter, diameter, height, material)

    def calculate_volume(self):
        volume_outer = math.pi * (self.radius_outer ** 2) * self.height
        volume_inner = math.pi * (self.radius_inner ** 2) * self.height

        return volume_outer-volume_inner

class Anchor(Component):
    def __init__(self, name, length, width, height, material):
        super().__init__(name, length, width, height, material)

#Materials
vgfm=Material("Vinyl Glass Fibre Membrane", 53.8, 7.83, 1.4)
aluminum=Material("Aluminum", 7000, 15000, 2700)
steel=Material("Steel", 2595, 800, 7850)
concrete=Material("Concrete", 140, 350, 2300)

#Defining Components
sheet1=Sheet("Sheet 1", 1.38, 2.09, .005, vgfm)
boom1=Boom("Boom 1", .05, 1.38, .003, aluminum)
boom2=Boom("Boom 2", .05, 2.09, .003, aluminum)
column1=Column("Column 1", .1, 2.65, .005, steel)
anchor1=Anchor("Anchor 1", .2, .2, .15, concrete)

#Add Components to Pavilion
my_pavilion=Pavilion("Ontario Pavilion")

all_components=[sheet1, boom1, boom2, column1, anchor1]

for comp in all_components:
    my_pavilion.add_component(comp)

#Final Calculations
total_volume=my_pavilion.total_volume()
total_weight=my_pavilion.total_weight()
total_cost=my_pavilion.total_cost()
total_co2=my_pavilion.total_co2_footprint()

print(f"The '{my_pavilion.name}' is made of {len(my_pavilion.components)} components and {len(set(comp.material.name for comp in my_pavilion.components))} different materials.")
print(f"Total material volume: {total_volume:.3f} m3")
print(f"Total weight: {total_weight:.2f} kg")
print(f"Total cost: €{total_cost:.2f}")
print(f"Total CO2 footprint: {total_co2:.2f}")