import sys
import xml.etree.ElementTree as ET
import input_parser as IP
import xml_formatter as XF

def main():
    # Check if number of arguments is correct and inform otherwise
    if len(sys.argv) != 2:
        print('Usage: python main.py \'absolute filepath for file to be converted\'')

    list_of_people = IP.parse_input_to_objects(IP.load_infile())

    people = ET.Element('people')
    for person in list_of_people:
        person.add_to_xmltree(people)

    XF.save_xml_tree(people)    

    outlist = XF.indent_family_tags((XF.load_xml_to_format('output.xml')))
    XF.write_formatted_xml(outlist)

if __name__ == '__main__':
    main()
