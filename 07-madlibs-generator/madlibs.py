"""
Prepare your story template: Write a short story containing specific words you want the user to replace. 
Mark these words in a way the program can identify (e.g., using curly braces like {adjective} or {noun}).
Identify target words: Create a list or a mechanism to scan the story for these placeholders to determine 
exactly which words the user needs to provide.
Handle user input: Create a loop that iterates through the identified placeholders, prompting the user via 
input() to provide a replacement for each one.
Inject inputs into the story: Use string manipulation to replace the placeholders in your original template 
with the specific words provided by the user.
Display the result: Print the final, modified story back to the user.
"""
import re
with open("story.txt") as file:
    story=file.read()
placeholders=list(dict.fromkeys(re.findall(r"<([^>]+)>", story)))
print("Write words for these placeholders:")
for placeholder in placeholders:
    rep=input(f"{placeholder}: ")
    story=story.replace(f"<{placeholder}>", rep)

print(story)