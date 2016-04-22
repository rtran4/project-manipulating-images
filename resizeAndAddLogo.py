import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'logo.png'

logoIm = Image.open( LOGO_FILENAME )
logoWidth, logoHeight = logoIm.size

os.makedirs("WithLogo", exist_ok = True)

for filename in os.listdir(os.path.join('.','originals')):
    if not (filename.endswith ('.png') or filename.endswith ('.jpg')) or filename == LOGO_FILENAME:
        continue
    
    im = Image.open(os.path.join('originals',filename))
    width, height = im.size
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SQUARE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
           width = int((SQUARE_FIT_SIZE / height) * width)
           height = SQUARE_FIT_SIZE

print('Resizing %s...' % (filename))
im = im.resize((width, height))

print('Adding logo to %s...' % (filename))
im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)
im.save(os.path.join('withLogo', filename))

    

