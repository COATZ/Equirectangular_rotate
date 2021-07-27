import os 
import numpy as np
import argparse
import random

PARSER = argparse.ArgumentParser()
PARSER.add_argument('-d', '--datadir',
                    nargs='?',
                    type=str,
                    default='/media/cartizzu/DATA/DATASETS/UNREAL/FOREST/FOREST_2/',
                    help='Dir containing the Equi images to rotate')
PARSER.add_argument('-e', '--ext',
                    nargs='?',
                    type=str,
                    default='png',
                    help='Image format')
PARSER.add_argument('-v', '--VERBOSE',
                    nargs='*',
                    action='store',
                    help='If true, prints out additional info.')

def main():
    list_img = sorted([file for file in os.listdir(DATADIR) if (file.endswith(EXT) and not file.startswith("rotate"))], key=lambda f: int(f.rsplit("/", 1)[-1].rsplit("_",1)[0]))
    
#    print(list_img)
    
    for idx, image in enumerate(list_img):
        if idx%3==0 or idx==0: 
            angle90 = [-1,1][random.randrange(2)] * 90
#        print("../Equirectangular_rotate.out {} {} {} {} ".format(image,angle90,0,0))
#        os.system("../Equirectangular_rotate_noname.out {} {} {} {} ".format(image,0,angle90,0))
        
    os.makedirs("ROTATED", exist_ok=True)
    os.system("mv rotate_* ROTATED/.")
    os.system("cd ROTATED; rename 's/.{7}(.*)/$1/' *")

if __name__ == '__main__':
    args = PARSER.parse_args()
    DATADIR = args.datadir
    EXT = args.ext
    VERBOSE = args.VERBOSE is not None
    main()
    