# Prompt the user for the file name
filename = input("Enter the file name: ")

try:
    # Open the file
    with open(filename, 'r') as file:
        total = 0  # Total sum of values
        count = 0  # Count of lines

        # Loop through each line in the file
        for line in file:
            # Look for lines starting with the specific string
            if line.startswith("X-DSPAM-Confidence:"):
                # Extract the number after the colon
                value = float(line.strip().split(":")[1])
                total += value  # Add the value to the total
                count += 1      # Increment the count

        # Compute the average
        if count > 0:
            average = total / count
            print("Average spam confidence:", average)
        else:
            print("No valid lines found.")

except FileNotFoundError:
    print("Error: File not found. Please check the file name and try again.")


