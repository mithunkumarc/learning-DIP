Image Resolution and quantization

Size of 2-D grid and data size stored for each individual image pixel.


#### Spatial Resolution
  C*R eg 640*480


#### Temporal Resolution: video

    eg : 25fps : frame per second

    
#### Bit Resolution

    eg : color intensity : quantization
    eg : 24 bit : color 8 + 8 + 8 ??

#### Image Formats 

    JPEG 
    GIF 8bit
    BMP basic format
    PNG 
    TIFF 
    
#### Image Datatype

    Binary Image
    Intensity or greyscale Image
    RGB or true color Image
    Floating point image : TIFF : medical field

#### Importing image

    From PIL import Image
    img = Image.open('images/profile.jpg')
    img.show()


#### convert to grey scale image

    new_img = Image.open('images/profile.jpg').convert('L')
    new_img.show()

#### convert image format 

    from PIL import Image
    import os
    
    filelist=['images/profile.jpg','images/moon.jpg']
    
    
    for infile  in filelist:
        outfile = os.path.splitext(infile)[0]+".png"
        if infile !=outfile:
            try:
                Image.open(infile).save(outfile)
            except IOError:
                    print("Cannot convert"), infile
        
  
    
  ####
    
