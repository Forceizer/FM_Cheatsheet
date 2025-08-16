import pathlib
import shutil

import cv2

notes_path = pathlib.Path(".").absolute().parent
inverted_path = notes_path.parent / "Inverted_Notes"
if inverted_path.exists():
    shutil.rmtree(inverted_path)

filters = ["Further Mathematics/Induction Resources"]
filters_paths = list()
for filter in filters:
    filters_paths.append(notes_path / filter)

def image_in_filtered_folder(file):
    filtered = False
    for filter in filters_paths:
        if file.is_relative_to(filter):
            filtered = True
            break
    return filtered


copiable_extensions = {".png", ".jpg"}
if __name__ == "__main__":
    for file in notes_path.glob("**/*"):
        if not file.is_file():
            continue
        new_dir = inverted_path / file.relative_to(notes_path).parent
        if not new_dir.exists():
            new_dir.mkdir(parents=True)

        if file.suffix in copiable_extensions and not image_in_filtered_folder(file):
            image = cv2.imread(str(file))
            inverted_image = cv2.bitwise_not(image)

            new_path = new_dir / file.name
            cv2.imwrite(str(new_path), inverted_image)
        else:
            shutil.copy(file, new_dir / file.name)
