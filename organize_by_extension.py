from pathlib import Path

# List of folders to organize into folders by filetype
folders = [
    r"C:\Users\52553\OneDrive\Documents",
    r"C:\Users\52553\Downloads"
]

for folder in folders:
    folder = Path(folder)  # creates a path object from the string
    for file in folder.rglob('*'):  # iterates through all files in the folder
        if file.is_file():  # checks if the file is a file
            suffix = file.suffix.replace('.', '').upper()  # removes the dot from the file extension and makes it upper
            if not Path(folder / suffix).exists():  # checks if the folder does not exist yet
                new_folder = Path(folder / suffix)
                new_folder.mkdir()  # creates folder with new name
            try:
                file.rename(folder / suffix / file.name)  # tries to move file to new folder
            except FileExistsError:  # if file already exists in new folder
                file.unlink()  # deletes file

    for x in range(10):
        for file in folder.rglob('**/*'):  # iterates through all files in the folder
            if file.is_dir():  # checks if the file is a directory
                try:
                    file.rmdir()  # tries to delete directory
                except:
                    pass  # if directory is not empty, it will not be deleted
