"""
This script takes in a given filepath, and creates an output file based on script formatting.

formatting:
    - SYMBOLS
        - line starts with @@ (Review)
            - skip this symbol - look at next symbol
        - line starts with # (Narration)
            - Enclose in double quotations
        - line starts with $$ (Scene)
            - Change to lower-case as 'scene locationname'
        - line starts with ? (Blue text)
            - Enclose with {color=#2D70D6} and {/color}
            - Then enclose with double quotations
        - line starts with > (Option or Nested)
            - Prepend '(Option)' if 2 tabs, (Nested)' if 4
            - Enclose with double quotations
            - Append ':'
        - line starts with [ and ends with ]
            - replace '[NAME: EMOTION]'
            - with 'show name emotion'
    - AFTER SYMBOLS
        - name ('Reader: ')
            - swap with person_id like 'r'
"""

import re

FILEPATH = r'Pineappleronpa-Report-Card\testing_formats_original.txt'
NEW_FILENAME = r"Pineappleronpa-Report-Card\formatted_script.txt"

HIGHLIGHT_COLOR = "#2D70D6"

def process_file(source_file, dest_file):
    with open(source_file) as source:
        with open(dest_file) as dest:
            for line in source:
                new_line = parse_line(line)
                # dest.write(new_line)

def parse_line(str: str):
    SYMBOLS = ["#","$$","?",">","["]
    indent = str.count("    ")
    str = str.lstrip()
    comment = str.startswith("@@")
    if comment:
        str = str.replace("@@","",1)
    symbol = ""
    for s in SYMBOLS:
        if str.startswith(s):
            symbol = s
    text = str[len(symbol):].lstrip()

    match symbol:
        case "#":
            text = '"' + text + '"'
        case "$$":
            text = "scene " + text.lower()
        case "?":
            text = f'"\{{color={HIGHLIGHT_COLOR}}}' + text + '{/color}"'
        case ">":
            text = "(Option)>" if indent == 1 else "(Nested)>"
            text = '"' + text + '":'
        case "[":
            text.replace("]","")
            text.replace(":","")
            text = text.lower()
    
    return text




if __name__ == "__main__":
    process_file(FILEPATH, NEW_FILENAME)