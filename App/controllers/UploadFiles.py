#from threading import setprofile
#from App import IMAGE_EXTENSIONS, app
import os

IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg'}

######################################################
def validateExtension(file, types):
    return '.' in file and file.rsplit('.', 1)[1].lower() in types

def uploadFile(file):
    if validateExtension(file, IMAGE_EXTENSIONS) :
        file.save(os.path.join('./App/static/upload', file.filename))

x = 'C:\\Users\\Dell-OKMY33\\Documents\\GitHub\\RaynerSystem\\github\\logo.png'
#trint (x)
with open(x, 'rb') as file :
    uploadFile(file)