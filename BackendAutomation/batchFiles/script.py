import csv
import random

def update_csv_randomly(input_file, output_file):
    """
    Update the second column of a CSV file starting from the second row
    with randomly assigned values: "approved" or "rejected".

    Parameters:
        input_file (str): Path to the input CSV file.
        output_file (str): Path to save the updated CSV file.
    """
    try:
        with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            rows = list(reader)

        # Check if the file has at least one row and a second column
        if len(rows) < 2 or len(rows[0]) < 2:
            print("The input file does not have sufficient rows or columns.")
            return

        # Update the second column starting from the second row
        for row in rows[1:]:
            row[1] = random.choice(["approved", "rejected"])

        # Write the updated rows to the output file
        with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            writer.writerows(rows)

        print(f"Updated CSV saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_csv = 'loanasa.csv'  # Replace with your input CSV file path
output_csv = 'loanasa.csv'  # Replace with your desired output CSV file path
update_csv_randomly(input_csv, output_csv)