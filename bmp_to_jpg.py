import os
from PIL import Image

# bmp 转换为jpg
def bmpToJpg(file_path):
    for fileName in os.listdir(file_path):
        # print(fileName)
        newFileName = fileName[0:-4]+".jpg"
        print(newFileName)
        im = Image.open(file_path+"\\"+fileName)
        im.save(file_path+"\\"+newFileName)


# 删除原来的位图
def deleteImages(file_path, imageFormat):
    command = "del "+file_path+"\\*."+imageFormat
    os.system(command)


def main():
    file_path = "C:\\Users\\admin\\Downloads\\拼接堇青石图像采集\\拼接堇青石图像采集"
    bmpToJpg(file_path)
    deleteImages(file_path, "bmp")


if __name__ == '__main__':
    main()