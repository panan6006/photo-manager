import os
import shutil
from pathlib import Path
import yaml


class FileManager:
    @staticmethod
    def load_config(path="config.yml"):
        with open(path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)

    def __init__(self):
        config = self.load_config()

        self.output_root = config["paths"]["output"]
        self.input = config["paths"]["input"]

    def read_images(self, path):

        #files = list(filter(os.path.isfile, glob.glob(path + "*")))
        #files.sort(key=lambda x: os.path.getmtime(x))

        #files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        #files.sort(key=lambda f: os.path.getmtime(os.path.join(path, f)), reverse=True)

        input_folder = Path(path)

        files = sorted([f for f in input_folder.glob("*") if f.is_file()],
                       key=lambda f: f.stat().st_mtime,
                       reverse=True)

        print(files)

        return files

    def move_image(self, image, index):
        destination = next(os.walk(self.output_root))[1][index]
        shutil.copy(image, Path(self.output_root) / destination)

        return self.remove_image(image)

    def remove_image(self, image):
        os.remove(image)
        return self.read_images(self.input)
