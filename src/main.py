from frontend import Frontend
from file_manager import FileManager

fm = FileManager("C:/temp/input/", "C:/temp/output/")
import_images = fm.read_images(fm.input)

fe = Frontend(import_images)

fe.create_image_control()

fe.create_output_panels("C:/temp/output/")

fe.run()
