# Initialize variables
positive_sum = 0
negative_sum = 0
positive_count = 0
negative_count = 0

while True:
    # Read the number from the user
    number = int(input("Enter the number: "))
    
    # Check for termination condition
    if number == -1:
        break
    
    # Update sums and counts based on the number's sign
    if number > 0:
        positive_sum += number
        positive_count += 1
    elif number < 0:
        negative_sum += number
        negative_count += 1

# Calculate and print averages
if positive_count > 0:
    positive_average = positive_sum / positive_count
    print(f"The average of positive numbers is: {positive_average:.8f}")
else:
    print("No positive numbers were entered.")

if negative_count > 0:
    negative_average = negative_sum / negative_count
    print(f"The average of negative numbers is: {negative_average:.1f}")
else:
    print("No negative numbers were entered.")
