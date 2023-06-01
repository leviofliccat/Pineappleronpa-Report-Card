"""
This script takes in a given filepath, and creates an output file based on script formatting.
"""

FILEPATH = r'Pineappleronpa-Report-Card\testing_formats.txt'
NEW_FILENAME = r"Pineappleronpa-Report-Card\formatted_script.txt"

HIGHLIGHT_COLOR = "#2D70D6"

def process_file(source_file, dest_file):
    with open(source_file, encoding="UTF-8") as source:
        with open(dest_file, "w", encoding="UTF-8") as dest:
            for line in source:
                new_line = parse_line(line)
                dest.write(new_line)

def parse_line(str: str):
    SYMBOLS = ["#","$$","?",">","["]
    NAME_DICT = {
        "Reader": "r",
        "Luke" : "l",
        "David" : "d",
        "Sean" : "s",
        "Julian" : "j",
        "Riley" : "i",
        "Mitch" : "m",
        "Will" : "w",
        "Johan" : "o",
        "Mel" : "e",
        "Felicity" : "f"
    }
    indent = str.count("    ")
    str = str.strip()

    comment = str.startswith("@@")
    if comment:
        str = str.replace("@@","",1)
    comment = "@@" if comment else "" #Ternary operator

    symbol = ""
    for s in SYMBOLS:
        if str.startswith(s):
            symbol = s
    text = str[len(symbol):].lstrip()
    text = text.replace('"', "'") # Replace " with '

    if text == "": return ""

    match symbol:
        case "#":
            text = f"\"{comment}{text}\""
        case "$$":
            text = "scene " + text
        case "?":
            # See READER_SAYS_HIGHLIGHTS at top of file to change blue
            text = f"\"{{color={HIGHLIGHT_COLOR}}}{comment}{text.split(':')[1].strip()}{{/color}}\""
        case ">":
            text = f"(Option)>{text}" if indent == 1 else f"(Nested)>{text}"
            text = '"' + text + '":'
            indent = 0
        case "[":
            text = text.replace("]","")
            text = text.replace(":","")
            text = "show " + text.lower()
        case _:
            text = text.split(":")
            text = f"{NAME_DICT[text[0]]} \"{comment}{text[1].lstrip()}\""

    indent = "    " if indent else ""
    return indent + text + '\n'

if __name__ == "__main__":
    process_file(FILEPATH, NEW_FILENAME)
    print("Done")