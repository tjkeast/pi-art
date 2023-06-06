import logging as log
from os import listdir
from os.path import isfile, join
from image_loader import ImageLoader
from image_display import ImageDisplay


def main() -> None:
    images_folder = "images"
    image_loader = ImageLoader(images_folder)
    image_loader.download_image(
        "https://vulcan.condenastdigital.com/demo/photos/6430305a43557ca5c77bec32/master/pass/WIR_LIFT_Sale_Growler_Paywall_Bar_400x400-update-white-bg_1x%20(1).png?format=original"
    )
    image_loader.download_image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/Raspberry_Pi_4_Model_B_-_Side.jpg/1200px-Raspberry_Pi_4_Model_B_-_Side.jpg"
    )

    image_files = [f for f in listdir(images_folder) if isfile(join(images_folder, f))]
    image_display = ImageDisplay()
    for file in image_files:
        image_display.add_image("%s/%s" % (images_folder, file))

    image_display.start()


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)
    log.info("App started")
    main()
