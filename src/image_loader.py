import requests
import os
import shutil
from os.path import splitext, basename
from urllib.parse import urlparse
import time
import logging as log


class ImageLoader:
    def __init__(self, image_directory: str = "images") -> None:
        self.image_directory = image_directory
        self.create_directory(image_directory, True)

    def download_image(self, image_url: str) -> str:
        image_data = requests.get(image_url).content
        disassembled = urlparse(image_url)
        file_name, file_ext = splitext(basename(disassembled.path))
        file_name = "%s%s" % (time.time_ns(), file_ext)
        file_path = "%s/%s" % (self.image_directory, file_name)
        with open(file_path, "wb") as handler:
            handler.write(image_data)
        log.debug("Downloaded image %s and saved to file %s" % (image_url, file_name))
        return file_path

    def create_directory(self, directory_name: str, delete: bool = False) -> None:
        if os.path.exists(directory_name):
            if delete:
                shutil.rmtree(directory_name)
                log.debug("Removed directory %s" % directory_name)
            else:
                log.debug(
                    "Skipped creating directory %s - already exists" % directory_name
                )
                return

        os.makedirs(directory_name)
        log.debug("Created new dirctory %s" % directory_name)
