# This code will decrypt any phrase without knowing the key

# Option to read from file or input
input_choice = input("Read from file? (y/n): ").lower()

if input_choice == 'y':
    filename = input("Enter filename: ")
    try:
        with open(filename, 'r') as file:
            word = file.read().strip()
        print(f"Read from file: {word}")
    except FileNotFoundError:
        print("File not found! Using manual input instead.")
        word = input("Enter the word you want to decrypt (you dont know the key): ")
else:
    word = input("Enter the word you want to decrypt (you dont know the key): ")

# Option to save results to file
save_choice = input("Save results to file? (y/n): ").lower()
output_file = None
if save_choice == 'y':
    output_file = input("Enter output filename: ")

results = []

# OLD CODE
for i in range(1, 26):
    shift = i
    ans = ""

    for j in range(len(word)):
        char = word[j]

        if char.isupper():
            ans += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            ans += chr((ord(char) - shift - 97) % 26 + 97)

    result_line = f"Using the shift {shift}, the decrypted word is: {ans}"
    print(result_line)
    results.append(result_line)
# OLD CODE

# Save to file if requested
if output_file:
    try:
        with open(output_file, 'w') as file:
            for result in results:
                file.write(result + '\n')
        print(f"Results saved to {output_file}")
    except Exception as e:
        print(f"Error saving to file: {e}")
