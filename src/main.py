from frontend import Frontend
from file_manager import FileManager

fm = FileManager()

fe = Frontend(fm.read_images(fm.input), fm)

fe.create_image_control()

fe.create_output_panels(fm.output_root)

fe.run()
