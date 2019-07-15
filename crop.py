import os
from PIL import Image
import time
from src import detect_faces
import argparse
import glob



parser = argparse.ArgumentParser(description = "Face Crop using MTCNN")

parser.add_argument("--root-dir", default = '/work2/VGGFACE2_DATASET/FaceNet/lwf/Images',type = str,help = "root dir path containing images")

parser.add_argument("--output-dir",default = '/work2/VGGFACE2_DATASET/FaceNet/lfw/Aligned', type = str, help = "output dir path containing aligned images")

args = parser.parse_args()

#Images
files = glob.glob(args.root_dir + '/*/*')



def aligned(files, alg_path): #args.output_dir is dir where all IMAGE DIRS are contained
    start = time.time()
    
    for i,image in enumerate(files):
        
        dirs = os.path.basename(os.path.dirname(image)) # image identity DIR.
        name = os.path.basename(image) # image ID
        if dirs not in os.listdir(alg_path): #if dir DOES NOT exist on NEW Path for NEW image
            os.mkdir(os.path.join(alg_path,dirs))
            
        img = Image.open(image)
        try:
            bboxes,_ = detect_faces(img)
        except ValueError:
            continue
        
            
        try:
            pt1 = tuple(bboxes[0][:2])
            pt2 = tuple(bboxes[0][2:4])
        except IndexError:
            continue
            
        
        cropped = img.crop(pt1 + pt2)
        cropped.save(os.path.join(alg_path,dirs,name))
        
    end = time.time() - start

    print(alg_path, 'Time: ', end)











if __name == '__main__':

	aligned(files,args.output_dir)





























