import os

def generate_txt(type)
"""
    this function generates the text file for train and val dataset

    type(str) : folder you want to save to text file
                type = train will generate train.txt
                type = test will generate test.txt
"""
    if type == 'train'
        image_files = []
        os.chdir(os.path.join("Dataset/data/images", "train"))
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                image_files.append("Dataset/data/images/train/" + filename)
        os.chdir("..")
        with open("train.txt", "w") as outfile:
            for image in image_files:
                outfile.write(image)
                outfile.write("\n")
            outfile.close()
        os.chdir("..")
    
    else:
        image_files = []
        os.chdir(os.path.join("Dataset/data/images", "valid"))
        for filename in os.listdir(os.getcwd()):
            if filename.endswith(".jpg"):
                image_files.append("Dataset/data/images/valid/" + filename)
        os.chdir("..")
        with open("train.txt", "w") as outfile:
            for image in image_files:
                outfile.write(image)
                outfile.write("\n")
            outfile.close()
        os.chdir("..")

if __name__ =="__main__":
    generate_txt()