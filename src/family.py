import xml.etree.ElementTree as ET
from phone import Phone
from address import Address

class Family:

    def __init__(self, name: str, born: str) -> None:
        self.name = name
        self.born = born
        self.phone = None
        self.address = None

    def set_phone(self, phone: Phone):
        self.phone = phone

    def set_address(self, address: Address):
        self.address = address

    def add_to_xmltree(self, xml_parent: ET.SubElement):
        family_tag = ET.SubElement(xml_parent, 'family')
        
        name_tag = ET.SubElement(family_tag, 'name')
        name_tag.text = self.name

        # Must be indented!
        born_tag = ET.SubElement(family_tag, 'born')
        born_tag.text = self.born

        # Must be indented!
        if self.address != None:
            self.address.add_to_xmltree(family_tag)

        # Must be indented!
        if self.phone != None:
            self.phone.add_to_xmltree(family_tag)