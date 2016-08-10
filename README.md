# image-resizer
Simple python utility to resize photos from high megapixel cameras

I take photos on my phone, they look nice, but are 4000 pixels wide and so take up about 1mb each. 
Really, the detail at more than 50% zoom is kinda shitty, so this resizer just shrinks images down to a max height or width of 1600
(whichever is the longer dimension, height or width). That's about 100kb, 10 times smaller.

There's also a batch file here. As is, this operates on a folder called "img2resize" and then puts the output in a subfolder called "resized"

I use this all the time to destroy shitty information, which Google, Apple, Microsoft etc would rather I keep for no reason. It's 90% of the photo, going to prove to the consumer that their camera is really fancy. 

I started realizing the importance of this process after using a old and very nice 1 megapixel camera, which took badass photos that were about 1600px wide. Still more than enough for almost any application.
