import xml.etree.ElementTree as ET

# Load and parse the XML file
XML_FILE_PATH = "../data/raw/Library.xml"

tree = ET.parse(XML_FILE_PATH)
root = tree.getroot()

# Helper to parse nested dictionaries from XML <dict> tags
def parse_dict(element):
    result = {}
    key = None
    for child in element:
        if child.tag == 'key':
            key = child.text
        else:
            result[key] = child.text if child.text else child
    return result

# Navigate to the top-level <dict> in the plist
top_dict = root.find('dict')

# Find the 'Tracks' and 'Playlists' entries
items = list(top_dict)
tracks = {}
playlists = []

for i, elem in enumerate(items):
    if elem.tag == 'key' and elem.text == 'Tracks':
        track_dict = items[i + 1]
        for j in range(0, len(track_dict), 2):
            track_id = track_dict[j].text
            track_info = parse_dict(track_dict[j + 1])
            tracks[track_id] = track_info
    if elem.tag == 'key' and elem.text == 'Playlists':
        playlist_array = items[i + 1]
        for playlist_dict in playlist_array:
            playlist = parse_dict(playlist_dict)
            playlists.append(playlist)

# Extract info for playlists
extracted_data = []

for playlist in playlists:
    playlist_name = playlist.get('Name', '')
    if playlist_name.startswith('Replay '):
        for item in playlist.get('Playlist Items', []):
            if isinstance(item, ET.Element):
                item_dict = parse_dict(item)
                track_id = str(item_dict.get('Track ID'))
                track = tracks.get(track_id)
                if track:
                    extracted_data.append({
                        'Playlist': playlist_name,
                        'Track Name': track.get('Name') or track.get('Sort Name'),
                        'Artist': track.get('Artist') or track.get('Sort Artist'),
                        'Album': track.get('Album') or track.get('Sort Album'),
                    })

# Display or export the result
for row in extracted_data:
    print(row)