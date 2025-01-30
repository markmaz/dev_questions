def calculate_average():
    try:
        numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        if not numbers:
            print("No numbers provided.")
            return
        average = sum(numbers) / len(numbers)
        print(f"Average: {average}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")

calculate_average()
