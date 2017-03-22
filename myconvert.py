#!/usr/bin/env python3.5
""" convert photo or image files using ImageMagick to thumbnail sizes
"""
import sys
import subprocess

def process_image():
    """ Process an image file.
    """
    max_xdim = 260
    outputdir = "./.resampled/"

    photo = sys.argv[1]
    photo_info = subprocess.Popen(["/usr/bin/identify", photo], stdout=subprocess.PIPE)
    (myout, myerr) = photo_info.communicate()
    if myerr:
        print("error from the ImageMagick identify routine: %s" % (myerr.decode('ascii')))
    myidentify = myout.decode('ascii').split(' ')
    dims = myidentify[2]
    xdim, ydim = dims.split('x')
    xdim = int(xdim)
    ydim = int(ydim)

    while xdim > max_xdim:
        xdim /= 2
        ydim /= 2

    mygeom = str(xdim)+'x'+str(ydim)
    myoutputfile = outputdir+photo
    myconvert = subprocess.run(["/usr/bin/convert", "-geometry", mygeom, photo, myoutputfile])
    print("%s" % (myconvert))

# end def process_image

process_image()
