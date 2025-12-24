#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    # Create root element
    root = ET.Element("data")

    # Add dictionary items as child elements
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    # Write XML tree to file
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    # Parse XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Reconstruct dictionary
    result = {}
    for child in root:
        result[child.tag] = child.text

    return result
