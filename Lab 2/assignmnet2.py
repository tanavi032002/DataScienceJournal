import matplotlib.pyplot as plt

def read_csv_data(file_path):
  
    gpa_scores, genders = [], []

    with open(file_path, 'r') as file:
        header = file.readline().strip().split(',')

        # Validate presence of 'GPA' and 'Gender' in header
        try:
            gpa_idx = header.index('GPA')
            gender_idx = header.index('Gender')
        except ValueError:
            print("Error: Columns 'GPA' or 'Gender' not found in the CSV header.")
            return gpa_scores, genders

        # Read data line by line
        for line in file:
            fields = line.strip().split(',')
            try:
                gpa = float(fields[gpa_idx])
                gender = fields[gender_idx].strip()

                # Skip invalid entries
                if gender:
                    gpa_scores.append(gpa)
                    genders.append(gender)
            except ValueError:
                continue

    return gpa_scores, genders

def calculate_pass_fail(gpa_scores, threshold):
    """Calculates counts of pass and fail based on a GPA threshold."""
    fail_count = sum(gpa < threshold for gpa in gpa_scores)
    pass_count = len(gpa_scores) - fail_count
    return fail_count, pass_count

def count_genders(genders):
    """Counts the occurrences of each gender."""
    from collections import Counter
    return Counter(genders)

def plot_pie_chart(ax, sizes, labels, colors, title):
    """Plots a pie chart with given parameters."""
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.set_title(title)
    ax.axis('equal')

if __name__ == "__main__":
    # Input parameters
    file_path = r'C:\Users\Tanavi\OneDrive\Desktop\JJJJJJJ\assignmnet2\dataset.csv'
    gpa_threshold = 3.5
    colors_pass_fail = ['#ff9999', '#66b3ff']  # Colors for pass and fail
    colors_gender = ['#99ff99', '#ffcc99']    # Colors for genders

    # Read and process data
    gpa_scores, genders = read_csv_data(file_path)
    fail_count, pass_count = calculate_pass_fail(gpa_scores, gpa_threshold)
    gender_counts = count_genders(genders)

    # Prepare data for pie charts
    pass_fail_sizes = [fail_count, pass_count]
    pass_fail_labels = ['Fail', 'Pass']
    gender_sizes = list(gender_counts.values())
    gender_labels = list(gender_counts.keys())

    # Create pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    plot_pie_chart(ax1, pass_fail_sizes, pass_fail_labels, colors_pass_fail, 'Pass vs Fail Students')
    plot_pie_chart(ax2, gender_sizes, gender_labels, colors_gender, 'Gender Distribution')

    # Display the plots
    plt.tight_layout()
    plt.show()
