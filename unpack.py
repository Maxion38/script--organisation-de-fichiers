# Take all the files out of the forlders
import shutil
import os
import time

start_time = time.time()

files_path = "C:\\Users\\mbong\\OneDrive\\Bureau\\python_photo_sort\\"

dir_list = os.listdir(files_path)
for dir in dir_list:
    file_path_list = os.listdir(files_path + dir)

    for file in file_path_list:
        current_file_path = files_path + dir + "\\" + file
        destination_path = files_path + file
        shutil.move(current_file_path, destination_path)
    print(dir + " unpacked")
print("Directories emptied")

for file_dir in dir_list:
    if os.path.isdir(files_path + "\\" + file_dir):
        os.rmdir(files_path + file_dir)

print("Directories removed")
end_time = time.time()
print(str(round(end_time - start_time, 2)) + "s")