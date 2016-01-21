import os
import shutil
import sys

path = sys.argv[1]
padding = 4

# list of files
tmp = os.listdir(path)
files = []
for t in tmp:
    if os.path.isfile( os.path.join(path, t) ):
        files.append(t)

# group sequence
fileNameList = []
for f in files:
    name, ext = os.path.splitext(f)
    fullName = name
    while name[-1].isdigit():
        name = name[:-1]
    fileNameList.append(name)
fileOrigNameList = set(fileNameList)
fileOrigNameList = list(fileOrigNameList)
fileList = []
for f in fileOrigNameList:
    a = fileNameList.index(f)
    b = fileNameList.count(f)
    fileList.append(files[a:(a+b)])

def fixSequence(seq):
    # separate
    frames = []
    for f in seq:
        name, ext = os.path.splitext(f)
        fullName = name
        while name[-1].isdigit():
            name = name[:-1]
        digits = int(fullName.replace(name, ''))
        frames.append (digits)
    offset = min (frames) - 1
    # new name
    correctname = raw_input('Enter correct name for old sequence "'+ seq[0]+ '": ')
    if correctname:
        outFolder = os.path.join(path, correctname)
        if not os.path.exists(outFolder):
            os.mkdir(outFolder)
        for i,f in enumerate(seq):
            old = os.path.join(path,f)
            name, ext = os.path.splitext(f)
            newName = correctname + '_' + str(frames[i]-offset).zfill(padding) + ext
            new = os.path.join(path,correctname,newName)
            if os.path.exists(new):
                os.remove(new)
            shutil.copy2(old,new)

    # search missing frames
    fullrange = range(min(frames),max(frames)+1)
    miss = []
    for i in fullrange:
        if not i in frames:
            miss.append(i)
    # message
    l = len(miss)
    if l == 0:
        print 'Not miss frames'
    else:
        print 'Miss frames: ',miss

    # delete old files
    a = raw_input('Remove old files? [y/n]: ')
    if a == 'y' or a == 'Y':
        for f in seq:
             os.remove(os.path.join(path,f))
    print 'Complete!!! Press Enter for continue...'
    raw_input()

for s in fileList:
    fixSequence(s)
