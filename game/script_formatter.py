
## Check use with quotation marks, slashes, etc
## blue text needs to be changed

## This program successfully:
    # Removes all extra spaces in the script before formatting
    # Removes extra line spaces
    # Understands dialogue as Speaker: Speech format
            # Understands narration as anything that is not dialogue or blue text format
            # Currently formats blue text with the colour #2D70D6 and removes the asterisks

    # Exports the entire script, in order, to a .txt document to be copy pasted directly into Ren'Py.
    # Replaces the colons it removes as part of the separating process.
    # Running this program multiple times will just update the formatted script file if it exists already.

########################################################################################################
## Before executing this program
########################################################################################################

## Ensure the file name of the script to be formatted is correct:
original_script_file_name = "testing_formats_original.txt"
original_script_encoding = "UTF-8" #with BOM"

## Ensure the character names are consistent with the script (coloured text within dialogue like important yellow text needs to be done manually): 

list_of_character_names = ["reader", "luke", "david", "sean", "julian", "riley", "mitch", "will", "johan", "mel", "felicity", "blue_text", "narration"]


# Create empty lists to be filled with character dialogue. Each line of dialogue will be a seperate element.
reader = []
luke = []
david = []
sean = []
julian = []
riley = []
mitch = []
will = []
johan = []
mel = []
felicity = []

blue_text = []
narration = []

## Ensure that the Ren'Py character codes in the game's code are correct here:
sean_object = "s"
reader_object = "r"


#########################################################################################################


# Import functions that replace colons.
from exp import colons_in_dialogue
from exp import colons_in_plain_text

# Define a function that removes all extra spaces in a string.
def remove_all_extra_spaces(string):
    return " ".join(string.split())

if original_script_encoding == "UTF-8 with BOM":
    script_encoding = "utf-8-sig"
elif original_script_encoding == "UTF-8":
    script_encoding = "utf-8"


# The open() function opens the text file to be read, 
# then the file is split and turned into a list readable by python.
script_read = open(original_script_file_name, "r", encoding=script_encoding)            # need to add encoding="utf-8-sig" in the open() command if it's utf-8 with bom
chat_script = script_read.read().split("\n")
while("" in chat_script):
    chat_script.remove("")


# For each line in the script, take the line, turn it into a string, 
# split up speaker and speech, identify type, then sort into lists.
i = 0
while i < len(chat_script):                                                                 ## This needs to be made more efficient; nested loops
    values = chat_script[i].split(": ")

    if values[0] == "Sean": 
        # calling the function to put colons back in if they were removed.
        sean.append(remove_all_extra_spaces(colons_in_dialogue(values)[1]))

    elif values[0] == "Reader":
        reader.append(remove_all_extra_spaces(colons_in_dialogue(values)[1]))

    else:
        if chat_script[i].startswith("?") == True:
            blue_text.append(colons_in_plain_text(values)[0])

        else:
            narration.append(remove_all_extra_spaces(colons_in_plain_text(values)[0]))
    i=i+1


# Create empty lists for formatted lines and define character objects.                  Again, make this a loop
renpy_sean = []

renpy_reader = []

renpy_blue_text = []

renpy_narration = []




# Formatting by adding quotation marks to dialogue and adding the 
# character object at front, then inserting into relevant list.
x = 0
while x < len(sean):
    speech = "\"" + sean[x] + "\""
    renpy_sean.append(sean_object + " " + speech)
    x = x+1        

x=0
while x<len(reader):
    speech = "\"" + reader[x] + "\""
    renpy_reader.append(reader_object + " " + speech)
    x=x+1

# Blue text format removes the asterisks, and changes the colour to blue (in-engine).
x=0
while x<len(blue_text):
    cleaned_blue_text = blue_text[x].replace("*", "")
    renpy_blue_text.append("\"{color=#2D70D6}" + remove_all_extra_spaces(cleaned_blue_text) + "{/color}\"")
    x=x+1

x=0
while x<len(narration):
    renpy_narration.append("\"" + narration[x] + "\"")
    x=x+1


# Create an empty list for the final ordered script.
final_script = []

for line in chat_script:
    if line.startswith("Sean:") == True:
        final_script.append(renpy_sean.pop(0)) 
        # Removes the first item from the dialogue list and adds it to the final_script list.
    elif line.startswith("Reader:") == True:
        final_script.append(renpy_reader.pop(0)) 
    elif line.startswith("*") == True and line.endswith("*") == True:
        final_script.append(renpy_blue_text.pop(0))
    else:
        final_script.append(renpy_narration.pop(0)) 
    


## Code to write the formatted script into a text file.

# Open/create file in write mode
fp = open(r"formatted_script.txt", "w")

for item in final_script:
    fp.write("%s\n" % item) # Write each item on a new line

# Notify when complete.
print("Complete")