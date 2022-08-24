import xml.etree.ElementTree as ET

def save_xml_from_tree(tree: ET.Element) -> None:
    '''Create an XML file from a XML tree structure.  Errors terminate the app.'''
    ET.indent(tree)
    bytestring_xml = ET.tostring(tree, encoding='utf-8')
    try:
        with open('output.xml', 'wb') as out:
            out.write(bytestring_xml)
    except IOError:
        print('An error occurred when writing the output file.')
        exit()

def load_xml(filepath: str) -> list:
    '''Parse XML file into a list of strings. Each line is a list element. Errors terminate the app.'''
    try:
        with(open(filepath, 'r', encoding='utf-8')) as infile:
            return infile.readlines()
    except IOError:
        print('An error occurred when reading the file for formatting.')
        exit()

def indent_family_tags(lines: list) -> list:
    '''Indent information about family member one additional level.'''
    formatted_lines = []
    in_family_tag = False
    for idx in range(len(lines)):
        cur = lines[idx]
        if '<family>' in cur:
            in_family_tag = True
        if '</family>' in cur:
            in_family_tag = False
        # Specify conditions when indentation should occur
        indent = ('<born>' in cur) or (in_family_tag and (('<phone>' in cur)
                    or ('<mobile>' in cur) or ('<telephone>' in cur) or
                    ('</phone>' in cur) or ('<address>' in cur) or
                    ('<street>' in cur) or ('<city>' in cur) or
                    ('<postalnumber>' in cur) or ('</address>' in cur)))
        if indent:
            formatted_lines.append('  ' + cur)
            continue
        formatted_lines.append(cur)
    return formatted_lines

def save_xml_from_txt(formatted_lines: list) -> None:
    '''Save a XML file from a list of strings. Errors terminate the app.'''
    try:
        with(open('output.xml', 'w', encoding='utf-8')) as outfile:
            outfile.writelines(formatted_lines)
    except IOError:
        print('An error occurred while writing the formatted output.')
        exit()
