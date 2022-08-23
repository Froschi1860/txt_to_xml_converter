from audioop import add
from re import S
from xml.dom import xmlbuilder
import xml.etree.ElementTree as ET

class Address:

    def __init__(self, street: str, city: str, postal: str) -> None:
        self.street = street
        self.city = city
        self.postal = postal

    def add_to_xmltree(self, xml_parent: ET.SubElement):
        address_tag = ET.SubElement(xml_parent, 'address')

        street_tag = ET.SubElement(address_tag, 'street')
        street_tag.text = self.street

        city_tag = ET.SubElement(address_tag, 'city')
        city_tag.text = self.city

        postalnumber_tag = ET.SubElement(address_tag, 'postalnumber')
        postalnumber_tag.text = self.postal
