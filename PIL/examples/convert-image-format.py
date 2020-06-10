from PIL import Image
import os
# if image is in same directory , full path not required , or else use full path c\\path\\image.bmp
filelist = ['lena_gray.bmp']

for infile in filelist:
	outfile = os.path.splitext(infile)[0]+'.png'
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("cannot convert"), infile
      
  
  '''
  bmp vs png

            BMP is both uncompressed and lossless. (takes more memory than png, quality is same)
            PNG is compressed but lossless. 

            Thus, with a lossless format the only visible difference is the file size. 
            I'd recommend using PNG over BMP unless you can't for compatibility reasons.

            There's no quality difference between BMP & PNG format (except PNG is compressed using deflate algorithm).

            BMP8 can be compressed using RLE (run-length-encoding) algorithm, but BMP16/24/32/64 doesn't support compression yet.

            BMP32 support alpha channel just like PNG32 support transparency.
'''
