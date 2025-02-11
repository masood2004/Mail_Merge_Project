# Define the placeholder text that will be replaced in the letter.
PLACEHOLDER = "[name]"

# Open and read the file containing the list of names.
# Each name is expected to be on a separate line in the "invited_names.txt" file.
with open("./Input/Names/invited_names.txt") as names_file:
    # Read all lines from the file into a list called 'names'
    names = names_file.readlines()

# Open and read the template letter from the "starting_letter.txt" file.
with open("./Input/Letters/starting_letter.txt") as letter_file:
    # Read the entire content of the letter template into the variable 'letter'
    letter = letter_file.read()

    # Loop through each name in the list of names.
    for name in names:
        # Remove any leading or trailing spaces from the name (using .strip())
        # and replace the placeholder with the actual name in the letter template.
        new_letter = letter.replace(PLACEHOLDER, name.strip())

        # Open a new file for writing the personalized letter for the current name.
        # The file is named dynamically based on the person's name, using the pattern 'letter_for_<name>.txt'.
        with open("./Output/ReadyToSend/letter_for_" + name.strip() + ".txt", mode="w") as completed_letter:
            # Write the modified letter into the new file
            completed_letter.write(new_letter)
