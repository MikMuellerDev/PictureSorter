import os
import time
from PIL import Image
from PIL.ExifTags import TAGS

folder_dict = {"SM-G950F": "mik", "SM-A520F": "ron", "SM-M115F": "sandra"}

directory = os.fsencode("dataset")

for key in folder_dict:
    try:
        os.mkdir(folder_dict[key])
    except Exception as e:
        pass

for file in os.listdir(directory):
    try:
        filename = os.fsdecode(file)
        image = Image.open("dataset/" + filename)
        exifdata = image.getexif()
        print("filename: " + filename)
        print("Camera-Model: " + str(exifdata[272]))
        print("This picture was taken by: " + str(folder_dict[exifdata[272]]))
        print("Moving Picture: " + filename + " to folder: " + folder_dict[exifdata[272]])
        os.rename("dataset/" + filename, folder_dict[exifdata[272]] + "/" + filename)
        print("Finished job: " + filename + "\n")
    except Exception as e:
        print(f"{'#'*50} Skipped: {filename}")


