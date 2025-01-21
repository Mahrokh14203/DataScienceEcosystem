# Prompt for the file name
file_name = input("Enter file name: ")

try:
    # Open the file
    with open(file_name, 'r') as file:
        # Initialize variables
        count = 0
        total = 0.0

        # Process each line
        for line in file:
            # Look for lines starting with the target string
            if line.startswith("X-DSPAM-Confidence:"):
                count += 1
                # Extract the numerical value
                confidence = float(line.split(":")[1].strip())
                total += confidence

        # Compute the average
        if count > 0:
            average = total / count
            print("Average spam confidence:", average)
        else:
            print("No matching lines found.")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")

