# Function to convert decimal to binary
def decimal_to_binary(decimal):
    binary = ""
    
    if decimal == 0:
        return "0"
    
    while decimal > 0:
        remainder = decimal % 2  # Get remainder when dividing by 2
        binary = str(remainder) + binary  # Add remainder to the binary string
        decimal = decimal // 2  # Update decimal by dividing it by 2

    return binary

# Input decimal number from user
decimal_number = int(input("Enter a decimal number: "))

# Convert to binary and display the result
binary_number = decimal_to_binary(decimal_number)
print(f"The binary equivalent of {decimal_number} is {binary_number}")
