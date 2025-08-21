import pathlib
import shutil

notes_path = pathlib.Path(".").absolute().parent
webpage_obsidian_path = notes_path.parent / "Webpage_Notes"
if webpage_obsidian_path.exists():
    shutil.rmtree(webpage_obsidian_path)

filters = ["Further Mathematics/Printable", "Further Mathematics/Pure Math 1/Printable", "README",
           "Further Mathematics/Further Mathematics Cheat Sheet.md", "Untitled.md", "Untitled 1.md", "README.md", "LICENSE.md",
           "Further Mathematics/Pure Math 1/Further Mathematics Cheat Sheet.md", "Further Mathematics/Statistics/Further Mathematics Cheat Sheet.md"]
filters_paths = list()
for filter in filters:
    filters_paths.append(notes_path / filter)

def file_in_filtered_folder(file):
    filtered = False
    for filter in filters_paths:
        if file.is_relative_to(filter):
            filtered = True
            break
    return filtered

core_folder = notes_path / ".obsidian"
def file_in_core_folder(file):
    return file.is_relative_to(core_folder)

copiable_extensions = {".png", ".jpg", ".md", ".gif"}
def file_is_copiable(file):
    return file.suffix in copiable_extensions or file_in_core_folder(file)


if __name__ == "__main__":
    for file in notes_path.glob("**/*"):
        if not file.is_file():
            continue

        if file_is_copiable(file) and not file_in_filtered_folder(file):
            new_dir = webpage_obsidian_path / file.relative_to(notes_path).parent
            if not new_dir.exists():
                new_dir.mkdir(parents=True)
            shutil.copy(file, new_dir / file.name)

    ## Special Instructions
    shutil.copy(notes_path / "Further Mathematics/Pure Math 1/Printable/Proof By Induction.md", webpage_obsidian_path / "Further Mathematics/Pure Math 1/Proof By Induction.md")
    shutil.copy(notes_path / "webpage/workspace.json", webpage_obsidian_path / ".obsidian/workspace.json")
