import sys
import xml.etree.ElementTree as ET
import input_parser as IP
import xml_formatter as XF

def main() -> None:
    # Check if number of arguments is correct and inform otherwise
    if len(sys.argv) != 2:
        print('Usage: python main.py \'absolute filepath for file to be converted\'')
        exit()
    infile = sys.argv[1]

    list_of_people = IP.parse_input_to_persons(IP.load_infile(infile))

    people = ET.Element('people')
    for person in list_of_people:
        person.add_to_xmltree(people)

    XF.save_xml_from_tree(people)
    outlist = XF.indent_family_tags((XF.load_xml('output.xml')))
    XF.save_xml_from_txt(outlist)
    print('Conversion successful. File was saved as output.xml.')

if __name__ == '__main__':
    main()
