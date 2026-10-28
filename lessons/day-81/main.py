rooms = {
    "start": {"description": "A sunny garden.", "east": "path"},
    "path": {"description": "A quiet path.", "west": "start", "north": "lake"},
    "lake": {"description": "A peaceful lake.", "south": "path"},
}
location = "start"
for direction in ["east", "north"]:
    print(rooms[location]["description"])
    location = rooms[location][direction]
print(rooms[location]["description"])
