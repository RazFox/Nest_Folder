import os, pathlib, shutil
from PIL import Image


class Image_File:

    def __init__(self, path_file):
        self.__normal_path = os.path.split(os.path.normpath(path_file))[0]
        self.__name_file = os.path.basename(pathlib.PurePath(os.path.normpath(path_file)).stem)
        self.__extension = pathlib.Path(os.path.normpath(path_file)).suffix
        # self.__width = Image.open(self.__normal_path).size[0]
        # self.__hight = Image.open(self.__normal_path).size[1]
        self.__size = os.stat(os.path.normpath(path_file)).st_size

    def get_path_image(self) -> str:
        return self.__normal_path

    def get_name_file(self) -> str:
        return self.__name_file

    def get_extension(self) -> str:
        return self.__extension

    # def get_width(self) -> int:
    #     return self.__width
    #
    # def get_hight(self) -> int:
    #     return self.__hight

    def get_size(self) -> int:
        return self.__size

    def set_path_image(self, new_path: str) -> None:
        """Метод переноса файла.
        Проверяет существует ли переданный путь, если путь существует, проверяет существует ли указанный файл по данному пути.
        Если файла нет, переносит данный файл из старой директории в новую.
        """
        #  TODO: Привести к адекватному виду метод
        if os.path.exists(new_path):
            name_file_extension = "{name}{extension}".format(name=self.__name_file, extension=self.__extension)
            if not os.path.exists(os.path.join(new_path, name_file_extension)):
                shutil.move(os.path.join(self.__normal_path, name_file_extension),
                            os.path.join(new_path, name_file_extension))
            self.__path_image = os.path.join(new_path, name_file_extension)

    def set_name_file(self, new_name: str) -> None:
        """Изменение наименования файла"""
        name_extension = "{name}{extension}".format(name=new_name, extension=self.__extension)
        os.rename(self.__normal_path, name_extension)
        self.__name_file = new_name
        self.set_path_image(self.__normal_path)

    def set_extension(self, new_extension: str) -> None:
        """Смена расширения файла"""
        new_name = "{name}{extension}".format(name=self.__name_file, extension=new_extension)
        os.rename(self.__normal_path, new_name)
        self.__extension = new_extension
        self.set_path_image(self.__normal_path)

    def set_width(self):
        pass

    def set_hight(self):
        pass

    def set_size(self):
        pass


image = "D:\\Python\\Проекты\\Nest_Folder\\test\\891976.jpg"
image_1 = Image_File(image)
print(image_1.get_path_image())
print(image_1.get_name_file())
print(image_1.get_extension())
# print(image_1.get_width())
# print(image_1.get_hight())
print(image_1.get_size())