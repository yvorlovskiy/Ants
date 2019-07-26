import glob, os, random
# Current directory

cwd = os.path.dirname(os.path.abspath(__file__))
current_dir = str(cwd) + '/antdata/'
save_dir = str(cwd) + '/antdata/'
os.chdir(current_dir)
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
            file_test.write(save_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(save_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1

final_dir1 = str(cwd) + '/ant_train.txt'
final_dir2 = str(cwd) + '/ant_test.txt'

os.rename(str(current_dir) + '/ant_train.txt', str(final_dir1))
os.rename(str(current_dir) + '/ant_test.txt', str(final_dir2))
print('moving files from' + str(current_dir) + 'to' + str(cwd))



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
