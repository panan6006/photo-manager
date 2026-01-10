import os
import shutil
import glob


class FileManager:
    def __init__(self, input, output):
        self.output_root = output
        self.input = input

    def read_images(self, path):
        '''
        import_images = []

        for file in os.listdir(path):
            import_images.append(f"{path}{file}")

        return import_images

        '''

        files = list(filter(os.path.isfile, glob.glob(path + "*")))
        files.sort(key=lambda x: os.path.getmtime(x))

        files.reverse()

        return files

    def move_image(self, image, index):
        destination = next(os.walk('C:/temp/output'))[1][index]
        shutil.copy(image, f'C:/temp/output/{destination}')

        return self.remove_image(self, image)

    def remove_image(self, image):
        os.remove(image)
        return self.read_images(self, 'C:/temp/input/')
