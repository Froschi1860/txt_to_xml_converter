import xml.etree.ElementTree as ET

from address import Address
from phone import Phone

class Person:
    '''Representaion of information about a person.'''
    def __init__(self, firstname: str, lastname: str) -> None:
        '''Constructor for person. Fields phone, address and family can be set optionally.'''
        self.firstname = firstname
        self.lastname = lastname
        self.phone = None
        self.address = None
        self.family = []

    def set_address(self, address: Address) -> None:
        '''Setter for address field.'''
        self.address = address

    def set_phone(self, phone: Phone) -> None:
        '''Setter for phone field.'''
        self.phone = phone

    def add_family(self, family_members: list) -> None:
        '''Setter for family field.'''
        self.family += family_members

    def add_to_xmltree(self, parent: ET.Element) -> None:
        '''Add a person to a XML tree structure.'''
        person_tag = ET.SubElement(parent, 'person')

        firstname_tag = ET.SubElement(person_tag, 'firstname')
        firstname_tag.text = self.firstname

        lastname_tag = ET.SubElement(person_tag, 'lastname')
        lastname_tag.text = self.lastname

        if self.address != None:
            self.address.add_to_xmltree(person_tag)

        if self.phone != None:
            self.phone.add_to_xmltree(person_tag)

        if len(self.family) > 0:
            for member in self.family:
                member.add_to_xmltree(person_tag)
