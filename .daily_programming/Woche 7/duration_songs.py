new_playlist = {
    "title": "wanderlust",
    "artist": "summer breeze",
    "song": [
        {"title": "track1", "artist": ["green"], "duration": 25},
        {"title": "track2", "artist": ["paws", "djwhiskers"], "duration": 5.25},
        {"title": "purrbeat", "artist": ["whiskers"], "duration": 2.0},
    ]
}

total_duration = 0
for song in new_playlist["song"]:
    total_duration += song["duration"]

print("Total duration:" , total_duration) 
# Ouput: Total duration: 32.25
