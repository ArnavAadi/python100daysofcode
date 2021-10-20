# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("C:\\Users\Administrator\\Documents\\prog\\Python\\Begginer\\Day 24\\Input\\Letters\\starting_letter.txt") as start:
    letter = start.read()

with open("C:\\Users\Administrator\\Documents\\prog\\Python\\Begginer\\Day 24\\Input\\Names\\invited_names.txt") as names:
    inv_names = names.readlines()

for name in inv_names:
    new_name = name.replace("\n", "")
    with open(f"./Output/ReadyToSend/{new_name}.txt", mode="w") as let:
        new_letter = letter.replace("[name]", f"{new_name}")
        let.write(new_letter)
