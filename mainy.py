from pathlib import Path

folder = Path(r"C:\Users\52553\Downloads")
for file in folder.rglob('*'):
    if file.is_file():
        suffix = file.suffix.replace('.', '').upper()
        if not Path(folder / suffix).exists():
            new_folder = Path(folder / suffix)
            new_folder.mkdir()
        try:
            file.rename(folder / suffix / file.name)
        except FileExistsError:
            file.unlink()

for x in range(10):
    for file in folder.rglob('**/*'):
        if file.is_dir():
            try:
                file.rmdir()
            except:
                pass

