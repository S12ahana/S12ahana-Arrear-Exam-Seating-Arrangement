import pandas as pd

def generate_combined_seating(num_classes, rows, columns, maths_roll_numbers, physics_roll_numbers):
    total_seats_per_class = rows * columns  

   
    maths_roll_numbers.sort()
    physics_roll_numbers.sort()
    
    
    seating_arrangements = []
    student_index_maths = 0
    student_index_physics = 0

    for class_num in range(1, num_classes + 1):
        seating_arrangement = [["Empty" for _ in range(columns * 2)] for _ in range(rows)] 
        
        
        for row in range(rows):
            for col in range(0, columns * 2, 2):  
                if student_index_maths < len(maths_roll_numbers) and student_index_physics < len(physics_roll_numbers):
                    seating_arrangement[row][col] = maths_roll_numbers[student_index_maths] 
                    seating_arrangement[row][col + 1] = physics_roll_numbers[student_index_physics] 
                    student_index_maths += 1
                    student_index_physics += 1
                else:
                    break
        
        
        for row in range(rows):
            for col in range(0, columns * 2, 2):
                if seating_arrangement[row][col] == "Empty":  
                    if student_index_maths < len(maths_roll_numbers):
                        seating_arrangement[row][col] = maths_roll_numbers[student_index_maths]  
                        student_index_maths += 1
                    elif student_index_physics < len(physics_roll_numbers):
                        seating_arrangement[row][col + 1] = physics_roll_numbers[student_index_physics] 
                        student_index_physics += 1
        
        seating_arrangements.append(seating_arrangement)
    
    return seating_arrangements

def print_seating_arrangements(seating_arrangements):
    
    for class_num, arrangement in enumerate(seating_arrangements, start=1):
        print(f"\nSeating Arrangement for Class {class_num}:")
        for row in arrangement:
            print("\t".join(row))

def save_seating_arrangements_to_csv(seating_arrangements, exam1_name, exam2_name):
    
    for class_num, arrangement in enumerate(seating_arrangements, start=1):
        filename = f"seating_arrangement_{exam1_name}_{exam2_name}_class_{class_num}.csv"
        df = pd.DataFrame(arrangement)
        df.to_csv(filename.xlsx, index=False, header=False)
       


if __name__ == "__main__":
    num_classes = int(input("Enter the number of classrooms: "))
    rows = int(input("Enter the number of rows per classroom: "))
    columns = int(input("Enter the number of columns per classroom: "))  
    
    
    maths_roll_numbers = input(f"Enter roll numbers for Maths exam, separated by spaces: ").split(",")
    physics_roll_numbers = input(f"Enter roll numbers for Physics exam, separated by spaces: ").split(",")

    
    seating_arrangements = generate_combined_seating(num_classes, rows, columns, maths_roll_numbers, physics_roll_numbers)
    
    
    print_seating_arrangements(seating_arrangements)
    save_seating_arrangements_to_csv(seating_arrangements, "Maths", "Physics")
