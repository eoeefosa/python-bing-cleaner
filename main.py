import re
# Open a file named bingmessage.txt with read mode
with open("bingmessage.txt", "r") as file:
  # Read the text from the file and store it in a variable
  text = file.read()
# Define the characters or substrings to remove
# Define a sample chatbot text
# text = "Hello, this is Bing. How can I help? [1]"
# to_remove = ["[1]", "[2]", "[3]"]
to_remove = [f"[{x}]" for x in range(1, 50)] # ['[1]', '[2]', '[3]']
in_remove = [f"[^{x}^]" for x in range(1, 50)]
# Define a function that takes a text as input and returns the modified text
def remove_spaces(text):
  # Split the text into paragraphs by newline characters
  paragraphs = text.split("\n")
#   paragraphs = text.split("")

  # Initialize an empty list to store the modified paragraphs
  modified_paragraphs = []
  # Loop through each paragraph
  for paragraph in paragraphs:
    # Replace any occurrence of more than two spaces with one space
    modified_paragraph = re.sub(" {2,}", " ", paragraph)
    # Append the modified paragraph to the list
    modified_paragraphs.append(modified_paragraph)
  # Join the modified paragraphs with newline characters and return the result
  return "\n".join(modified_paragraphs)

# Define a function that takes a text as input and returns a text with no spaces greater than 2
def removes_spaces(text):
  # Initialize an empty string to store the output
  output = ""
  # Initialize a counter to keep track of consecutive spaces
  space_count = 0
  # Loop through each character in the text
  for char in text:
    # If the character is not a space, append it to the output and reset the space count
    if char != " ":
      output += char
      space_count = 0
    # If the character is a space and the space count is less than 2, append it to the output and increment the space count
    elif space_count < 2:
      output += char
      space_count += 1
    # If the character is a space and the space count is equal to or greater than 2, ignore it and do nothing
    else:
      pass
  # Return the output string
  return output


to_remove = [f"[{x}]" for x in range(1, 50)] # ['[1]', '[2]', '[3]']
in_remove = [f"[^{x}^]" for x in range(1, 50)]
newline=["\n"]
# Loop through each item in to_remove and replace it with an empty string
for item in to_remove:
  text = text.replace(item, "")
for item in in_remove:
  text = text.replace(item, "")
for item in newline:
  text =text.replace(item," ")
new_contents = text.replace("age", "\nage")


# Open a new file with write mode
with open("output.txt", "w") as file:
  # Write the modified text to the file
  file.write(text)

remove_spaces(text)
removes_spaces(text)
# Print a confirmation message

print("The output.txt file has been created.")


# # Example usage
# text = "This is   a sample   text with   extra spaces.\n\nThis is another   paragraph."
# print(remove_spaces(text))