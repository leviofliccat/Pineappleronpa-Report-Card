import re

def parse_tree(lines):
    """
    Parse an indented outline into (level, name, parent) tuples.  Each level
    of indentation is 4 spaces.
    """
    regex = re.compile(r'^(?P<indent>(?: {4})*)(?P<name>\S.*)')
    stack = []
    for line in lines:
        line = line[4:]
        match = regex.match(line)
        if not match:
            raise ValueError(
                'Indentation not a multiple of 4 spaces: "{0}"'.format(line)
            )
        level = len(match.group('indent')) // 4
        if level > len(stack):
            raise ValueError('Indentation too deep: "{0}"'.format(line))
        stack[level:] = [match.group('name')]
        yield level, match.group('name'), (stack[level - 1] if level else None)
        

myDict = {

}

def run_parse(raw):

    for level, name, parent in parse_tree(raw):
        # print('{0}{1} ( {2} )'.format(' ' * (4 * level), name, parent or 'root'))
        if level == 0:
            choice_name = name
            dialogue = []
        if level == 1:            
            if name.startswith('>'):
                nested_choice = '(Nested)' + name
                dialogue_nested = []
                myDict[nested_choice] = dialogue_nested
            else:
                dialogue.append(name)
            myDict[choice_name] = dialogue
    
        if level == 2: 
            dialogue_nested.append(name)
    return myDict
        


            
            
        



        
# script = """    hi
#         ohdear"""

# run_parse(script)