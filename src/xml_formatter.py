import xml.etree.ElementTree as ET

def save_xml_tree(tree: ET.Element):
    ET.indent(tree)
    bytestring_xml = ET.tostring(tree, encoding='utf-8')
    try:
        with open('output.xml', 'wb') as out:
            out.write(bytestring_xml)
    except IOError:
        print('An error occurred when writing the output file.')
        exit()

def indent_family_tags(lines_as_list: list):

    in_family_tag = False
    for idx in range(len(lines_as_list)):
        cur = lines_as_list[idx]

        if '<family>' in cur:
            in_family_tag = True
        if '</family>' in cur:
            in_family_tag = False

        shift = ('<born>' in cur) or ((('<phone>' in cur) or ('<mobile>' in cur)
                    or ('<telephone>' in cur) or ('</phone>' in cur) or
                    ('<address>' in cur) or ('<street>' in cur) or
                    ('<city>' in cur) or ('<postalnumber>' in cur) or
                    ('</address>' in cur)) and in_family_tag)
        
        if shift:
            lines_as_list[idx] = '  ' + cur

    return lines_as_list

def write_formatted_xml(formatted_lines: list):
    try:
        with(open('output.xml', 'w', encoding='utf-8')) as outfile:
            outfile.writelines(formatted_lines)
    except IOError:
        print('An error occurred while writing the formatted output.')
        exit()


def load_xml_to_format(filepath: str):
    try:
        with(open(filepath, 'r', encoding='utf-8')) as infile:
            return infile.readlines()
    except IOError:
        print('An error occurred when reading the File for formatting.')
        exit()
