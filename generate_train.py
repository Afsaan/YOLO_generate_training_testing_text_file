import os

def generate_txt(folder_type):
    """
        this function generates the text file for train and val dataset

        folder_type(str) : folder you want to save to text file
                    folder_type = train will generate train.txt
                    folder_type = test will generate test.txt
    """
    if folder_type == 'train':
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
        with open("test.txt", "w") as outfile:
            for image in image_files:
                outfile.write(image)
                outfile.write("\n")
            outfile.close()
        os.chdir("..")

if __name__ =="__main__":
    # generate_txt('train')
    generate_txt('val')
