import xml.etree.ElementTree as ET
import input_parser as IP

from setuptools import PEP420PackageFinder

from person import Person
from family import Family
from phone import Phone
from address import Address

test_person = Person('Fabi', 'Fröschl')
test_address = Address('Morigglstrasse 4a', 'Munich', '80995')
test_phone = Phone('0163-1785794', '089-30779165')
test_family = Family('Sandra', '1993')
test_address_2 = Address('Lothringer Strasse 8', 'Munich', '81667')
test_person_2 = Person('Test', 'Testington')

test_person.set_address(test_address)
test_person.set_phone(test_phone)
test_family.set_address(test_address_2)
test_person.add_family(test_family)
test_person_2.set_address(test_address_2)

people = ET.Element('people')


test_person.add_to_xmltree(people)
test_person_2.add_to_xmltree(people)

ET.indent(people)

bytestring_xml = ET.tostring(people)

ET.dump(people)

with open('output.xml', 'wb') as out:
    out.write(bytestring_xml)


def main():
    # Handle invalid args
    pass

if __name__ == '__main__':
    main()
