import xml.etree.ElementTree as ET

from phone import Phone
from address import Address

class Family:
    '''Representation of information about family members.'''
    def __init__(self, name: str, born: str) -> None:
        '''Constructor for famnily member. Fields phone and address can be set optionally.'''
        self.name = name
        self.born = born
        self.phone = None
        self.address = None

    def set_phone(self, phone: Phone) -> None:
        '''Setter for phone field.'''
        self.phone = phone

    def set_address(self, address: Address) -> None:
        '''Setter for address field.'''
        self.address = address

    def add_to_xmltree(self, parent: ET.SubElement) -> None:
        '''Add a family member to a XML tree structure.'''
        family_tag = ET.SubElement(parent, 'family')
        
        name_tag = ET.SubElement(family_tag, 'name')
        name_tag.text = self.name

        born_tag = ET.SubElement(family_tag, 'born')
        born_tag.text = self.born

        if self.address != None:
            self.address.add_to_xmltree(family_tag)

        if self.phone != None:
            self.phone.add_to_xmltree(family_tag)
