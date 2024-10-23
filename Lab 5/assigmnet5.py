def read_data_file(file_path):
    records = []
    with open(file_path, 'r') as file:
        next(file)  # Skip the header row
        for line in file:
            fields = line.strip().split(',')
            records.append(fields)
    return records

def parse_date(date_string):
    year, month, day = map(int, date_string.strip().split('-'))  # Parse date
    return (year, month, day)

def filter_by_date_range(records, start_date, end_date):
    filtered_records = []
    start_date_tuple = parse_date(start_date)
    end_date_tuple = parse_date(end_date)

    for entry in records:
        date_string = entry[0].strip()  # Strip whitespace
        entry_date_tuple = parse_date(date_string)

        if start_date_tuple <= entry_date_tuple <= end_date_tuple:
            filtered_records.append(entry)

    return filtered_records

def calculate_daily_average(filtered_records):
    daily_avg = {}
    for entry in filtered_records:
        date_string = entry[0].strip()
        calories = int(entry[2].strip())  # Changed index to 2 for calories
        
        if date_string in daily_avg:
            daily_avg[date_string].append(calories)
        else:
            daily_avg[date_string] = [calories]

    # Calculate average calories per day
    avg_per_day = {date: sum(calories) / len(calories) for date, calories in daily_avg.items()}
    return avg_per_day

def find_maximum_calories_per_meal(filtered_records):
    daily_max = {}
    for entry in filtered_records:
        date_string = entry[0].strip()
        calories = int(entry[2].strip())  # Changed index to 2 for calories

        if date_string in daily_max:
            daily_max[date_string] = max(daily_max[date_string], calories)
        else:
            daily_max[date_string] = calories
            
    return daily_max

def compute_standard_deviation(filtered_records):
    calorie_values = [int(entry[2].strip()) for entry in filtered_records]  # Changed index to 2 for calories
    if len(calorie_values) <= 1:
        return None
    mean = sum(calorie_values) / len(calorie_values)
    variance = sum((x - mean) ** 2 for x in calorie_values) / len(calorie_values)
    return variance ** 0.5

def find_maximum_calories_in_range(filtered_records):
    return max(int(entry[2].strip()) for entry in filtered_records) if filtered_records else 0  # Changed index to 2 for calories

def calculate_average_calories_in_range(filtered_records):
    total_calories = sum(int(entry[2].strip()) for entry in filtered_records)  # Changed index to 2 for calories
    return total_calories / len(filtered_records) if filtered_records else None

def get_valid_date(prompt):
    while True:
        date_string = input(f"{prompt} (YYYY-MM-DD): ")
        # Validate the input date format
        if len(date_string) == 10 and date_string[4] == '-' and date_string[7] == '-':
            return date_string
        else:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")

def main():
    file_path = r'C:\Users\Tanavi\OneDrive\Desktop\JJJJJJJ\assignmnet2\calorie_data.csv'  # Updated file path
    records = read_data_file(file_path)

    start_date = get_valid_date("From Date")
    end_date = get_valid_date("To Date")

    filtered_records = filter_by_date_range(records, start_date, end_date)

    average_calories_per_day = calculate_daily_average(filtered_records)
    max_calories_per_meal = find_maximum_calories_per_meal(filtered_records)
    std_deviation = compute_standard_deviation(filtered_records)
    overall_max_calories = find_maximum_calories_in_range(filtered_records)
    overall_average_calories = calculate_average_calories_in_range(filtered_records)

    print(f"Data from {start_date} to {end_date}:")
    for date, avg_calories in average_calories_per_day.items():
        print(f"Date: {date}, Average Calories: {avg_calories:.2f}")

    for date, max_calories in max_calories_per_meal.items():
        print(f"Date: {date}, Highest Calories in Meal: {max_calories}")

    if std_deviation is not None:
        print(f'Standard deviation of calories from {start_date} to {end_date}: {std_deviation:.2f}')

    if overall_max_calories is not None:
        print(f'Highest Calories consumed between {start_date} to {end_date}: {overall_max_calories}')

    if overall_average_calories is not None:
        print(f'Average Calories consumed between {start_date} to {end_date}: {overall_average_calories:.2f}')
    else:
        print("No data available")

if __name__ == "__main__":
    main()
