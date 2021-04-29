import math, sys
import json

from goprocam import GoProCamera, constants

folder = "100GOPRO"

def transform_timestamp(timestamp):
    minutes = timestamp / 60000.0
    seconds = int((math.modf(minutes)[0]) * 60)
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)

    return str(int(minutes)) + ":" + str(seconds)

class VideoFileModel:

    def __init__(self, filename):
        self.__filename = filename

    @property
    def video_encoding(self):
        return self.__filename[0:2]

    @property
    def chapter(self):
        return self.__filename[2:4]

    @property
    def clip(self):
        return self.__filename[4:8]

    @property
    def file_extension(self):
        return self.__filename[9:]
    
    @property
    def sane_format(self):
        return self.clip + "-" + self.chapter + "." + self.file_extension

    @property
    def video_length(self):
        return self.__length
    
    @video_length.setter
    def video_length(self, length):
        self.__length = length


# Build array of video clip files
video_files = []
# for file in gpCam.listMedia(True, True):
    v = VideoFileModel("GH011234.mp4")
    v.video_length = file.length
    video_files.append(v)



for n in video_files:
    print(n.sane_format)