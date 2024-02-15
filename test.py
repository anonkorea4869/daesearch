import os

file_path = "/AA/BB.txt"
directory, extension = os.path.splitext(file_path)

if extension in [".png", ".jpg", ".txt"]:
    index = file_path.rfind("/")
    if index != -1:
        file_path = file_path[:index]

print(file_path)
