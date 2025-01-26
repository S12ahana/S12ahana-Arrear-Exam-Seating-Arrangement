import pandas as pd

def generate_combined_seating(num_classes, rows, columns, maths_roll_numbers, physics_roll_numbers):
    total_seats_per_class = rows * columns  # Total benches (each bench seats two students)

    # Sort roll numbers to seat students in ascending order
    maths_roll_numbers.sort()
    physics_roll_numbers.sort()
    
    # Initialize seating arrangements for each class
    seating_arrangements = []
    student_index_maths = 0
    student_index_physics = 0

    for class_num in range(1, num_classes + 1):
        seating_arrangement = [["Empty" for _ in range(columns * 2)] for _ in range(rows)]  # 2 seats per row (per bench)
        
        # Fill benches, each row as a bench (Maths and Physics together in one row)
        for row in range(rows):
            for col in range(0, columns * 2, 2):  # Two seats per bench
                if student_index_maths < len(maths_roll_numbers) and student_index_physics < len(physics_roll_numbers):
                    seating_arrangement[row][col] = maths_roll_numbers[student_index_maths]  # Maths student
                    seating_arrangement[row][col + 1] = physics_roll_numbers[student_index_physics]  # Physics student
                    student_index_maths += 1
                    student_index_physics += 1
                else:
                    break
        
        # If there are any remaining students, place them in empty spots
        for row in range(rows):
            for col in range(0, columns * 2, 2):
                if seating_arrangement[row][col] == "Empty":  # Check if the bench is empty
                    if student_index_maths < len(maths_roll_numbers):
                        seating_arrangement[row][col] = maths_roll_numbers[student_index_maths]  # Place Maths student
                        student_index_maths += 1
                    elif student_index_physics < len(physics_roll_numbers):
                        seating_arrangement[row][col + 1] = physics_roll_numbers[student_index_physics]  # Place Physics student
                        student_index_physics += 1
        
        seating_arrangements.append(seating_arrangement)
    
    return seating_arrangements

def print_seating_arrangements(seating_arrangements):
    # Print the seating arrangement for each class
    for class_num, arrangement in enumerate(seating_arrangements, start=1):
        print(f"\nSeating Arrangement for Class {class_num}:")
        for row in arrangement:
            print("\t".join(row))

def save_seating_arrangements_to_csv(seating_arrangements, exam1_name, exam2_name):
    # Save seating arrangements for each class to a CSV file
    for class_num, arrangement in enumerate(seating_arrangements, start=1):
        filename = f"seating_arrangement_{exam1_name}_{exam2_name}_class_{class_num}.csv"
        df = pd.DataFrame(arrangement)
        df.to_csv(filename, index=False, header=False)
        print(f"Seating arrangement for Class {class_num} saved to {filename}")

# User input for Maths and Physics exams
if __name__ == "__main__":
    num_classes = int(input("Enter the number of classrooms: "))
    rows = int(input("Enter the number of rows per classroom: "))
    columns = int(input("Enter the number of columns per classroom: "))  # Each column has 2 seats (1 Maths, 1 Physics)
    
    # Enter student roll numbers from two exams
    maths_roll_numbers = input(f"Enter roll numbers for Maths exam, separated by spaces: ").split()
    physics_roll_numbers = input(f"Enter roll numbers for Physics exam, separated by spaces: ").split()

    # Generate seating arrangement
    seating_arrangements = generate_combined_seating(num_classes, rows, columns, maths_roll_numbers, physics_roll_numbers)
    
    # Print and save seating arrangements
    print_seating_arrangements(seating_arrangements)
    save_seating_arrangements_to_csv(seating_arrangements, "Maths", "Physics")
