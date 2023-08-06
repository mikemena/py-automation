import os
from pathlib import Path

SUBDIRECTORIES = {
    "DOCUMENTS": [".pdf", ".rtf", ".txt"],
    "AUDIO": [".m4a", ".m4b", ".mp3"],
    "VIDEOS": [".mov", ".avi", ".mp4"],
    "IMAGES": [".jpg", ".jpeg", ".png"],
}


def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category


# print(pickDirectory(".mp3"))


def organizeDirectory():
    # get all objects in folder
    for item in os.scandir():
        # get file path for each file
        filePath = Path(item)
        # isolate the suffix to see what directory it needs to go to
        filetype = filePath.suffix.lower()
        # use pickDirectory function and pass in the suffix
        directory = pickDirectory(filetype)
        # cast directory to a path for file movement
        directoryPath = Path(directory)
        # if the directory the file maps to does not exist, then create it
        if directoryPath.is_dir() != True:
            directoryPath.mkdir()
        # moving file happens in both cases [directory exist and directory does not exist]
        # so this is outside of if statement
        filePath.rename(directoryPath.joinpath(filePath))
