# MTCNN CROP

An MTCNN pytorch implementation to detect and crop face region on an image as described by   
[Joint Face Detection and Alignment using Multi-task Cascaded Convolutional Networks](https://arxiv.org/abs/1604.02878).

## Instructions
Download the repository and then
```linux
crop.py --root-dir path_to_images -output-dir output_path
```
The system will create an output with the same format as the original path to the images

For examples see `test_on_images.ipynb`.

## Dir Format
The root directory format containing the images of interest need to be held in a similar fashion to:

![](https://github.com/Erick7451/mtcnn-pytorch-crop/blob/master/images/sample.png)

## Requirements
* pytorch 0.2
* Pillow, numpy

## Credit
This implementation and algorithm is completely taken by:
* [TropComplique/mtcnn-pytorch](https://github.com/TropComplique/mtcnn-pytorch)  
