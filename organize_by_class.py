from pathlib import Path

excel = ['XLSM', 'XLSX', 'XLS', 'CSV', 'XLAM', 'XLA']
photos = ['JPG', 'JPEG', 'PNG', 'GIF', 'SVG', 'BMP']
music = ['MP3', 'WAV', 'FLAC']
video = ['MP4', 'AVI', 'MOV']
python = ['PY', 'PYTHON', 'IPYNB']
pdf = ['PDF']
zip_files = ['ZIP', 'RAR', '7Z']
powerpoint = ['PPT', 'PPTX', 'ODP']
text = ['TXT']
apps = ['EXE']
html = ['HTML']
word = ['DOC', 'DOCX']
secure = ['CER', 'KEY', 'REN', 'REQ']

# 'all' is a list of all file types
all = excel + photos + music + video + python + pdf + zip_files + powerpoint + text + apps + html + word + secure

folders = [
    r"C:\Users\52553\OneDrive\Documents",
    r"C:\Users\52553\Downloads"
]


def organize(folder_name, file_type_list):
    for folder in folders:  # iterates through all folders to organize
        folder = Path(folder)  # converts string to path
        for file in folder.rglob('*'):  # iterates through all files in the folder
            if file.is_file():  # checks if the file is a file
                suffix = file.suffix.replace('.', '').upper()  # removes the dot from the file type and uppers it
                if any(suffix == ftype for ftype in all):  # checks if the file type is in the list of all file types
                    if any(suffix == ftype for ftype in file_type_list):  # checks for specific file type
                        if not Path(f'{folder}/{folder_name}').exists():  # checks if the folder does not exist yet
                            new_folder = Path(f'{folder}/{folder_name}')  # creates new folder
                            new_folder.mkdir()
                        try:
                            file.rename(f'{folder}/{folder_name}/{file.name}')  # tries to move file to new folder
                        except FileExistsError:
                            file.unlink()  # deletes file if it already exists in new folder
                else:
                    if not Path(folder / suffix).exists():  # checks if the folder does not exist yet
                        new_folder = Path(folder / suffix)
                        new_folder.mkdir()  # creates folder with new name
                    try:
                        file.rename(folder / suffix / file.name)  # tries to move file to new folder
                    except FileExistsError:  # if file already exists in new folder
                        file.unlink()  # deletes file

def delete_empty_folders():
    for folder in folders:
        folder = Path(folder)
        for x in range(10):
            for file in folder.rglob('**/*'):  # iterates through all files in the folder
                if file.is_dir():  # checks if the file is a directory
                    try:
                        file.rmdir()  # tries to delete directory
                    except:
                        pass  # if directory is not empty, it will not be deleted

organize('EXCEL', excel)
organize('PHOTOS', photos)
organize('MUSIC', music)
organize('VIDEO', video)
organize('PYTHON', python)
organize('PDF', pdf)
organize('ZIP', zip_files)
organize('POWERPOINT', powerpoint)
organize('TEXT', text)
organize('APPS', apps)
organize('HTML', html)
organize('WORD', word)
organize('SECURE', secure)
delete_empty_folders()

