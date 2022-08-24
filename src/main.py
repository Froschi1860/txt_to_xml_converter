import sys
import xml.etree.ElementTree as ET
import input_parser as IP

def main():
    # Check if number of arguments is correct and inform otherwise
    if len(sys.argv) != 2:
        print('Usage: python main.py \'absolute filepath for file to be converted\'')

    list_of_people = IP.parse_input(IP.load_infile())

    people = ET.Element('people')
    for person in list_of_people:
        person.add_to_xmltree(people)
    ET.indent(people)

    bytestring_xml = ET.tostring(people)
    try:
        with open('output.xml', 'wb') as out:
            out.write(bytestring_xml)
    except IOError:
        print('An error occurred when writing the output file.')
        exit()

    ET.dump(people)

if __name__ == '__main__':
    main()
