import xml.etree.ElementTree as ET

# XML file path
XML_FILE_PATH = "../data/raw/Library.xml"
OUTPUT_PATH = "../models/apple_music_xml_structure.md"

tree = ET.parse(XML_FILE_PATH)
root = tree.getroot()

lines = []


def write_xml_key_tree(elem, level=0):
    if elem.tag == "key":
        lines.append(f"{'    ' * level}- {elem.text}")
    for child in elem:
        write_xml_key_tree(child, level + 1)


# Run tree walk and save to file
lines.append("# 🎼 Apple Music XML Structure\n")
write_xml_key_tree(root)

with open(OUTPUT_PATH, "w") as f:
    f.write("\n".join(lines))

print(f"✅ XML structure written to {OUTPUT_PATH}")
