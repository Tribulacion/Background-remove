import os
from datetime import datetime
from rembg import remove


class BackgroundRemove:
    def __init__(self, input_folder, output_folder):
        """
        Clase para remover el fondo de las imágenes de un directorio
        :param input_folder:
        :param output_folder:
        """
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        """
        Procesar las imágenes de un directorio
        :return:
        """
        today = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        proccessed_folder = os.path.join(self.output_folder, f"proccessed_{today}")
        os.makedirs(proccessed_folder, exist_ok=True)

        for file_name in os.listdir(self.input_folder):
            if file_name.endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(self.input_folder, file_name)
                output_path = os.path.join(proccessed_folder, file_name)

                self._remove_background(input_path, output_path)
                self._move_originals(input_path, proccessed_folder)

    def _remove_background(self, input_p, output_p):
        """
        Remover el fondo de una imagen
        :param input_p:
        :param output_p:
        :return:
        """
        with open(input_p, 'rb') as inp, open(output_p, 'wb') as outp:
            background_remove = remove(inp.read())
            outp.write(background_remove)

    def _move_originals(self, input_p, dest_p):
        """
        Mover las imágenes originales a una carpeta de respaldo
        :return:
        """
        original_folder = os.path.join(dest_p, "originals")
        os.makedirs(original_folder, exist_ok=True)

        filename = os.path.basename(input_p)
        new_path = os.path.join(original_folder, filename)
        os.rename(input_p, new_path)


if __name__ == '__main__':
    input_folder = "input"
    output_folder = "output"

    background_remove = BackgroundRemove(input_folder, output_folder)
    background_remove.process_images()
