import xml.etree.ElementTree as ET

from address import Address
from family import Family
from phone import Phone

class Person:
    '''Representation of of a person'''

    def __init__(self, firstname: str, lastname: str) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.phone = None
        self.address = None
        self.family = []

    def set_address(self, address: Address):
        self.address = address

    def set_phone(self, phone: Phone):
        self.phone = phone

    def add_family(self, family_member: Family):
        self.family.append(family_member)

    def add_to_xmltree(self, xml_parent: ET.Element):
        person_tag = ET.SubElement(xml_parent, 'person')

        firstname_tag = ET.SubElement(person_tag, 'firstname')
        firstname_tag.text = self.firstname

        lastname_tag = ET.SubElement(person_tag, 'lastname')
        lastname_tag.text = self.lastname

        if self.address != None:
            self.address.add_to_xmltree(person_tag)

        if self.phone != None:
            self.phone.add_to_xmltree(person_tag)

        if len(self.family) > 0:
            for i in self.family:
                i.add_to_xmltree(person_tag)
