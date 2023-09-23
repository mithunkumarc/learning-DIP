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
        
  
    
#### Basic Manipulation, Resize, Crop, rotate

      from PIL import Image
      
      img = Image.open('images/profile.jpg')
      
      #Resize
      smaller_img = img.resize((150,150))
      #smaller_img.show()
      
      #Crop
      box = (100,100,400,400)
      region = img.crop(box)
      
      #region.show()
      #Rotation
      rotated_img = img.rotate(45)
      rotated_img.show()

#### Analyzing image information, shape, type, datatype
    
    import numpy as np
    import matplotlib.pyplot as plt
    
    A = plt.imread('images/profile.jpg')
    #print(A) # numpy array
    print(np.shape(A))
    print(type(A)) # 
    print(A.dtype)
    plt.imshow(A)
    plt.show()
  
#### Plotting Descriptive images

    from PIL import Image
    from pylab import *
    
    im = array(Image.open('images/profile.jpg'))
    imshow(im)
    # draw points on image
    x = [100,150,300,400]
    y = [50,500,200,500]
    
    plot(x,y,'r*') # r* : color
    
    # plot line
    plot(x[:2],y[:2],'r')

    # plot dotted lines
    plot(x[2:],y[2:],'ks:')
    #  add title
    title('Plotting "Profile.jpg"')
    
    show()

#### Adding interactive annotations : eg : mark image
    
    from PIL import Image
    from pylab import *
    
    im = array(Image.open('images/profile.jpg'))
    imshow(im)
    #Select 4 points
    pt = ginput(4)
    
    print('You selected : ',pt)
    
    show() # click on image to show points

#### overview of image processing techniqes

    Three level of processing operations

    Low level : 
    output and input are images : 
    eg : primitive operations :  noise reduction, contrast enhancements
    

    Mid Level
    extraction of attributes
    eg : edges and contours, Region extraction

    High Level
    Analysis and interpretation


#### Examples of some image processing operations

    sharpening : edges and fine details of image are enhanced
    noise removal : reduce amout of noise, depends on type of noise, 
    de-blurring : improper focus, fast moving objects
    Blurring : blurring important parts of image
    Edge extraction : used to separate objects
    Binarization : reduce to only two level image eg : white or black
    contrast enchancement : import for human viewing : to make other process easy like edge detection
    Object Segmentation and labelling : after recognition/classifying and labelling


    
    

    
    
