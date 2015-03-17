import glob
import os
import shutil

os.chdir("/home/szr163/caption_checked_once/")
for files in glob.glob("*.txt"):
    if not 'text' in files:
     imgfilsrc='/home/szr163/images/'+files.split('_')[1].split('.')[0]+'.jpeg'
     imgfildst='/home/szr163/imgcxs/'
     shutil.copy2(imgfilsrc,imgfildst)
     print 'copied '+imgfilsrc+' to '+imgfildst
