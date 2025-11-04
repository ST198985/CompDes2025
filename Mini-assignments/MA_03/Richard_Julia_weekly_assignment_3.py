
building_elements={}

calculate_area=lambda l, h:l*h
calculate_volume=lambda l, h, t :l*h*t

def add_element(key, element):
    building_elements[key]=element

def get_elements_by_type(library,element_type):
    filtered_elements={
        key: details for key, details in library.items()
        if details["Type"].lower() == element_type.lower()
    }
    return filtered_elements

print("Hello! Welcome to your new BIM tool - Building Elements Library.") 

while True:
    print("\nPlease choose from the following options:")
    print("A - Add an element to the Building Elements Library")
    print("B - Display the full Building Elements Library")
    print("C - List elements by type")
    print("D - Summarize all data of Building Elements Library")
    print("E - Exit program")

    choice=input("Enter your choice (A, B, C, D, or E): ").upper()

    #OPTION E - EXIT
    if choice=='E':
        print("K byyyeeee!")
        break

    #OPTION A - ADD ELEMENT TO LIBRARY
    elif choice=='A':
        while True:
            key=input("Enter a unique key for the building element (e.g. InW.01.23): ")
            if key in building_elements:
                replace=input(f"Key '{key}' already exists. Would you like to replace it with a new key? Y/N ")
                if replace.lower() in ('y', 'yes'):
                    print(f"Replacing element with key '{key}'.")
                    break
                else:
                    print("Please enter a different unique key.")
            else:
                break
        
        type=input("Enter the type of the building element (e.g., 'wall,' 'window,' 'door,' etc.): ")
        room=input("Enter the name of the room assigned to the element (e.g., 'living room,' 'staircase,' etc.): ")
        
        while True:
            try:
                length=float(input("Enter the length of the element in meters: "))
                if length <0:
                    print("Length cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Length must be a number (eg. 1.2). Please try again.")

        while True:
            try:
                height=float(input("Enter the height of the element in meters: "))
                if height <0:
                    print("Height cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Height must be a number (eg. 1.2). Please try again.")
            
        while True:
            try:
                thickness=float(input("Enter the thickness of the element in meters: "))
                if thickness <0:
                    print("Thickness cannot be negative. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Thickness must be a number (eg. 1.2). Please try again.")
        
        area_dec=calculate_area(length, height)
        area=round(area_dec,2)
        volume_dec=calculate_volume(length, height, thickness)
        volume=round(volume_dec,3)

        element={
            "Type":type,
            "Room":room,
            "Length":length,
            "Height":height,
            "Thickness":thickness,
            "Area":area,
            "Volume":volume
        }

        add_element(key, element)
        print("Element", key, "was added to the Building Elements library with the following information:",element)

    #OPTION B - DISPLAY BUILDING ELEMENTS LIBRARY
    elif choice=='B':
        if building_elements:
            print("\nFull Building Elements Library")
            for key, details in building_elements.items():
                print(f"Key: {key}, Details: {details}")
        else:
                print("The Building Elements Library is currently empty. Please add an element.")

#OPTION C - LIST ELEMENTS BY TYPE
    elif choice=='C':
        if not building_elements:
            print("The Building Elements Library is currently empty. Please add an element.")
            continue

        while True:
            search_type=input("Enter the element type (e.g., 'wall,' 'window,' 'door,' etc.): ")
            results=get_elements_by_type(building_elements,search_type)
            if results:
                for key, details in results.items():
                    print(f"\nElements List for Type: {search_type.upper()}")
                    print(f"Key: {key}")
            else:
                print(f"No elements of type '{search_type} could be found.")
            prompt=input("Would you like to search for another element type? Y/N")
            if prompt.lower() in ('n', 'no'):
                break

#OPTION D - SUMMARIZE ALL DATA
    elif choice=='D':
        if not building_elements:
            print("The Building Elements Library is currently empty. Please add an element.")
            continue

        print("\nDATA SUMMARY")

        type_counts={}
        all_element_types=[info["Type"] for info in building_elements.values()]
        unique_element_types=set(all_element_types)
        
        for info in building_elements.values():
            current_type=info["Type"]
            if current_type in type_counts:
                type_counts[current_type]+= 1
            else:
                type_counts[current_type]=1

        print("\nElement Types Report")
        print("There are", len(unique_element_types), "unique element types:")
        print("Numer of elements by Type:")
        for element_type, count in type_counts.items():
            print(f"{element_type.title()}: {count}")

        all_room_names=[info["Room"] for info in building_elements.values()]
        unique_room_names=set(all_room_names)

        print("\nRoom Types Report")
        print("There are", len(unique_room_names), "unique room types:")
        print(unique_room_names)

        areas_by_type={}
        volumes_by_type={}

        for info in building_elements.values():
            element_type_key=info["Type"]
            element_area=info["Area"]
            element_volume=info["Volume"]

            if element_type_key not in areas_by_type:
                areas_by_type[element_type_key] = []
            areas_by_type[element_type_key].append(element_area)

            if element_type_key not in volumes_by_type:
                volumes_by_type[element_type_key] = []
            volumes_by_type[element_type_key].append(element_volume)

        for type_name, area_list in areas_by_type.items():
            min_area=min(area_list)
            max_area=max(area_list)

            print("\nAreas Report (Min/Max per type)")
            print(f"Type: {type_name.title()}")
            print(f"    Min Area: {min_area:.2f} m2")
            print(f"    Max Area: {max_area:.2f} m2")

        for type_name, volume_list in volumes_by_type.items():
            min_volume=min(volume_list)
            max_volume=max(volume_list)
            
            print("\nVolumes Report (Min/Max per type)")
            print(f"Type: {type_name.title()}")
            print(f"    Min Volume: {min_volume:.3f} m3")
            print(f"    Max Volume: {max_volume:.3f} m3")

        total_dimensions_by_type={}

        for info in building_elements.values():
            current_type=info["Type"]
            dimensions=[info["Length"], info["Area"], info["Volume"]]

            if current_type not in total_dimensions_by_type:
                total_dimensions_by_type[current_type]=[]
            total_dimensions_by_type[current_type].append(dimensions)

        for type_name, list_of_dimensions in total_dimensions_by_type.items():
            total_lengths=sum([dimensions[0] for dimensions in list_of_dimensions])
            total_areas=sum([dimensions[1] for dimensions in list_of_dimensions])
            total_volumes=sum([dimensions[2] for dimensions in list_of_dimensions])

            print("\nTotal Dimensions Report by Element Type")
            print(f"Type: {type_name.title()}")
            print(f"    Total Length: {total_lengths:.2f} m")
            print(f"    Total Surface Area: {total_areas:.2f} m2")
            print(f"    Total Volume: {total_volumes:.3f} m3")

    else:
        print("Invalid input. Please enter A, B, C, D, of E.")



#total/added length of all "Type" using sum (eg. total length of all walls is 12.4m)
#total/added surface area of all "Type" using sum (eg. total surface area of all walls is 40.8m2)
#total/added volume of all "Type" using sum (eg. total volume of all walls is 60.3m3)

#total/added length of "Type" per room name using sum
#total/added surface area of "Type" per room name using sum
#total/added volume of "Type" per room name using sum