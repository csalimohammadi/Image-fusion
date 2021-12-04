# Image-fusion
CLHAE based image enhancement

In this project, we combine two different formats of an X-Ray image to enrich the features of an image.

Our algorithm loads all of the JPG images (X-Ray) from a folder and transforms them into two different formats (HSV and LAB format). Then, decompose the LAB image into L and A, and B and then apply CLHAE denoising to the L channel. 
Finally, our algorithm fuses all the channels and combine them with HSV image and build enhanced images (less noise and richer features). 
