import glob, os, random
# Current directory

current_dir = 'antdata/'


print(current_dir)


# Percentage of images to be used for the test set
percentage_test = 10

# Create and/or truncate train.txt and test.txt
file_train = open('ant_train.txt', 'a+')  
file_test = open('ant_test.txt', 'a+')

# Populate train.txt and test.txt
counter = 1  
index_test = round(100 / percentage_test)  
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.txt")):  
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
            counter = 1
            file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1




"""
# This may also work
images = glob.glob(os.path.join(current_dir, "*.txt"))

random.seed(4)
random.shuffle(images)

train_image_amount = round((1-percentage_test)*len(glob.glob(os.path.join(current_dir, "*.txt")))/100)
train_images = images[0:train_image_amount]
test_images = images[:train_image_amount]

def image_write(images, file):
    for image in images:
        title, _ = os.path.splitext(os.path.basename(image))
        file.write(current_dir + "/" + title + '.jpg' + "\n")
        
image_write(train_images, file_train)
image_write(test_images, file_test)
    
"""
