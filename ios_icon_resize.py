#!/usr/bin/python

import sys
import os.path
import Image
import string

###USAGE: python ios_icon_resize.py

### Script by Firecracker Software
### http://www.firecrackersw.com
### Use freely; no attribution required.

### This script relies on PIL, the Python Image Library.
### It will not work with the newer "Pillow" image library.

### Place this script in a directory containing your iTunesArtwork@2x
### asset (1024x1024 px) and run from command line.

EXPORT_QUALITY=100

def main():

	#Import the image into an image object.
	im = Image.open("iTunesArtwork@2x.png")
	width = im.size[0]
	height = im.size[1]

	#Resize for all known icon sizes.
	resize(im, "Icon-Notification-20", 20, 20)
	resize(im, "Icon-Notification-20@2x", 40, 40)
	resize(im, "Icon-Notification-20@3x", 60, 60)
	
	resize(im, "Icon-29", 29, 29)
	resize(im, "Icon-29@2x", 58, 58)
	resize(im, "Icon-29@3x", 87, 87)
	
	resize(im, "Icon-40", 40, 40)
	resize(im, "Icon-40@2x", 80, 80)
	resize(im, "Icon-40@3x", 120, 120)
	
	resize(im, "Icon-57", 57, 57)
	resize(im, "Icon-57@2x", 114, 114)
	
	resize(im, "Icon-60@2x", 120, 120)
	resize(im, "Icon-60@3x", 180, 180)
	
	resize(im, "Icon-50", 50, 50)
	resize(im, "Icon-50@2x", 100, 100)
	
	resize(im, "Icon-72", 72, 72)
	resize(im, "Icon-72@2x", 144, 144)
	
	resize(im, "Icon-76", 76, 76)
	resize(im, "Icon-76@2x", 152, 152)
	
	resize(im, "Icon-83.5@2x", 167, 167)
	
	resize(im, "iTunesArtwork", 512, 512)
	#With iTunesArtwork@2x taken as granted.

def resize(im, name, width, height):
	#Resize the image object to the target size.
	im = im.resize((height, height), Image.ANTIALIAS)
	
	#Perform cropping pass.  Really only useful for iOS 6 and below.
	left = (height - width)/2		#Crops from center of icon.
	top = 0
	right = (height + width)/2
	bottom = height
	finalcrop = im.crop((left, top, right, bottom))
	
	#Save the final result.
	finalcrop.save(str(name) + ".png", quality=EXPORT_QUALITY)
	
if __name__ == "__main__":
    main()