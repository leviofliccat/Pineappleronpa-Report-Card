
## need to Check use with question marks quotation marks, slashes, etc... still not 100% but pretty solid so far
## trying to do indents

## This program successfully:
    # Removes all extra spaces in the script before formatting
    # Removes extra line spaces
    # Understands dialogue as Speaker: Speech format
    # Understands narration as starting with #
    # Currently formats blue text with the colour and understands it as starting with ?
    # Preserves lines starting with > and @@ for manual review
    # Understands [NAME: EXPRESSION]
    # Understands scene changes as starting with $$

    # Exports the entire script, in order, to a .txt document to be copy pasted directly into Ren'Py.
    # Replaces the colons it removes as part of the separating process.
    # Running this program multiple times will just update the formatted script file if it exists already.

########################################################################################################
## Before executing this program
########################################################################################################

## Ensure the file name and encoder of the script to be formatted is correct:
original_script_file_name = "testing_formats_original.txt"
original_script_encoding = "UTF-8" # whatever it says in the bottom right of the txt file

## Ensure the character names are consistent with the script (case doesn't matter): 
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

scene_transition = []
expression_change = []
blue_text = []
narration = []
review = []
options = []
nested = []

## Ensure the desired character object codes to be used in the game's dialogue code are consistent:
object_codes = {
    "reader_object" : "r",
    "luke_object" : "l",
    "david_object" : "d",
    "sean_object" : "s",
    "julian_object" : "j",
    "riley_object" : "r",
    "mitch_object" : "m",
    "will_object" : "w",

    "johan_object" : "o",
    "mel_object" : "e",

    "felicity_object" : "f"
}

## Colour of blue text

blue = "{color=#2D70D6}"

##############################################################
## Document preparation
##############################################################

def check(line):
    if line.startswith("?") == True:
        blue_text.append(colons_in_dialogue(values)[1])
    elif line.startswith("@@") == True:
        review.append(remove_all_extra_spaces(colons_in_plain_text(values)[0]))
    elif line.startswith("[") == True:
        expression_change.append(remove_all_extra_spaces(colons_in_plain_text(values)[0]))
    elif line.startswith("$$") == True:
        scene_transition.append(remove_all_extra_spaces(colons_in_plain_text(values)[0]))
    elif line.startswith("#"):
        narration.append(remove_all_extra_spaces(colons_in_plain_text(values)[0]))
    


# Import functions.
from exp import colons_in_dialogue
from exp import colons_in_plain_text
from tab_parse import run_parse
from trial import list_from_dict
from trial import b_list_from_dict

# Define a function that removes all extra spaces in a string.
def remove_all_extra_spaces(string):
    return " ".join(string.split())


if original_script_encoding == "UTF-8 with BOM":
    script_encoding = "utf-8-sig"
elif original_script_encoding == "UTF-8":
    script_encoding = "utf-8"


# The open() function opens the text file to be read, 
# then the file is split and turned into a list readable by python.
script_read = open(original_script_file_name, "r", encoding=script_encoding)
chat_script = script_read.read().split("\n")
while("" in chat_script):
    chat_script.remove("")


##############################################################
## Script preparation
##############################################################

# For each line in the script, take the line, turn it into a string, 
# split up speaker and speech, identify type, then sort into lists.
temp = []
scanned = False #scans for all options once, then never again
character_names = ["Reader", "Luke", "David", "Sean", "Julian", "Riley", "Mitch", "Will", "Johan", "Mel", "Felicity"]
list_character_names = [reader, luke, david, sean, julian, riley, mitch, will, johan, mel, felicity]
i = 0
while i < len(chat_script):                                                    
    values = chat_script[i].split(": ")
    
    x = 0
    
    while x < len(character_names):
        person = character_names[x]
        if values[0] == person:
            position = character_names.index(person)
            name = list_character_names[position]
            name.append(remove_all_extra_spaces(colons_in_dialogue(values)[1]))
        x=x+1

    if chat_script[i].startswith('    >') and scanned == False:
        x = i
        while x < len(chat_script):           
            if chat_script[x].startswith('    '):
                temp.append(chat_script[x])
            x = x+1
        scanned = True
        result = run_parse(temp)
        nested = list_from_dict(result)
        options = b_list_from_dict(result)
        check(nested[x]) # help

    check(chat_script[i])
     
    i=i+1



# Create empty lists for formatted lines and define character objects.                  

renpy_reader = []
renpy_luke = []
renpy_david = []
renpy_sean = []
renpy_julian = []
renpy_riley = []
renpy_mitch = []
renpy_will = []
renpy_johan = []
renpy_mel = []
renpy_felicity = []

renpy_scene_transition = []
renpy_expression_change = []
renpy_blue_text = []
renpy_narration = []
renpy_review = []
renpy_nested = []
renpy_options = []

list_renpy_names = [renpy_reader, renpy_luke, renpy_david, renpy_sean, renpy_julian, renpy_riley, renpy_mitch, renpy_will, renpy_johan, renpy_mel, renpy_felicity]
# Formatting by adding quotation marks to dialogue and adding the 
# character object at front, then inserting into relevant list.



i = 0
while i < len(character_names):
    sent = 0
    person = list_character_names[i]
    while sent < len(person):
        speech = "\"" + person[sent] + "\""
        char = list_renpy_names[i]
        code = str(character_names[i]).lower() + "_object"
        
        char.append(object_codes[code] + " " + speech)
        sent = sent+1  

    i = i+1



# Blue text format removes the quesiton mark, and changes the colour to blue (in-engine). 
x=0
while x<len(blue_text):
    # first_char = ((blue_text[x])[0])[0]
    # cleaned_blue_text = blue_text[x].replace(first_char, "")
    renpy_blue_text.append("\"" + blue + blue_text[x] + "{/color}\"")
    x=x+1

x=0
while x<len(narration):
    
    cleaned_narration = (narration[x])[2:]
    renpy_narration.append("\"" + str(cleaned_narration) + "\"")
    x=x+1



x=0
while x<len(review):
    renpy_review.append(">>>!!!REVIEW FORMATTING!!! \"" + review[x] + "\"")
    x=x+1

x=0
while x<len(nested):
    i = 0
    while i < len(nested[x]):       
        renpy_nested.append("   \"" + nested[x][i] + "\"")
        i=i+1
    x=x+1

x=0
while x<len(options):
    renpy_options.append("\"" + options[x] + "\":")
    x=x+1

x=0
while x<len(scene_transition):
    cleaned_scene = (scene_transition[x])[3:]             ## review syntax
    renpy_scene_transition.append("scene " + str(cleaned_scene).lower())
    x=x+1

x=0
while x<len(expression_change):
    line = str(expression_change[x]).lower()
    line = line.replace("[","")
    line = line.replace("]","")
    values = line.split(": ")
    name = values[0]
    expression = values[1]
    renpy_expression_change.append("show " + name + " " + expression)
    x=x+1



# Create an empty list for the final ordered script.
final_script = []

for line in chat_script:
    
    i = 0
    while i < len(character_names):
        name = character_names[i] + ":"
        renpy_list_name = list_renpy_names[i]
        if line.startswith(name) == True:
            final_script.append(renpy_list_name.pop(0))
        i = i+1

    if line.startswith("?") == True:
        final_script.append(renpy_blue_text.pop(0))
    elif line.startswith("@@") == True:
        final_script.append(renpy_review.pop(0))
    elif line.startswith("    >") == True or line.startswith("        >") == True:
        final_script.append(renpy_options.pop(0))
    elif line.startswith("        ") == True:   
        final_script.append(renpy_nested.pop(0))
    elif line.startswith("[") == True:
        final_script.append(renpy_expression_change.pop(0))
    elif line.startswith("$$") == True:
        final_script.append(renpy_scene_transition.pop(0))
    elif line.startswith("#") == True:
        final_script.append(renpy_narration.pop(0))



## Code to write the formatted script into a text file.

# Open/create file in write mode
fp = open(r"formatted_script.txt", "w")

for item in final_script:
    fp.write("%s\n" % item) # Write each item on a new line

# Notify when complete.
print("Complete")