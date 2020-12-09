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

class GoProFileModel:

    def __init__(self, filename):

        self.filename = filename
        # self.gp = GoProCamera.GoPro(constants.gpcontrol)

    @property
    def prefix(self):
        return self.filename[0:2]

    @property
    def chapter(self):
        return self.filename[2:4]

    @property
    def clip(self):
        return self.filename[4:8]

    @property
    def extension(self):
        return self.filename[9:]
    
    @property
    def sane_format(self):
        return self.clip + "-" + self.chapter + "." + self.extension
    
    @property
    def duration(self):
        return 0
        return self.gp.getVideoInfo("dur",folder,self.filename)

    @property
    def tags(self):
        return 0
        return self.gp.getVideoInfo("tags",folder,self.filename)


class GoProFileGroup:

    def __init__(self):
        self.clip_id
        self.chapters = []


files = ["GH010041.mp4","GH020041.mp4","GH030041.mp4","GH010042.mp4","GH010043.mp4"]
file_groups = []
file_group = {}
chapters = []

# First load up the file_groups
for f in files:
    j = GoProFileModel(f)

    if j.clip not in file_group:
        file_group = {}
        file_group[j.clip] = None
        file_groups.append(file_group)

# Now load the chapters
for f in files:

    j = GoProFileModel(f)

    chapter = {}
    chapter = {
        j.chapter: {
            "duration": j.duration,
            "tags": j.tags
        }
    }

    chapters.append(chapter)

print(chapters)

"""
for f in files:
    j = GoProFileModel(f)

    chapter = {
        j.chapter: {
            "duration": j.duration,
            "tags": j.tags
        }
    }

    if (file_group[j.clip] == None):
        file_group = {j.clip: {}}
    
    file_group[j.clip].append(chapter)

file_groups.append(file_group)

media = gpCam.listMedia(True, True)
for i in media:
        folder = i[0]
        filename = i[1]
        if filename.endswith('MP4'):
"""