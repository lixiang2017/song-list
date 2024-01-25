import os

wsl_path = os.path.join(os.path.dirname(__file__), "wsl_list")
dilink_path = os.path.join(os.path.dirname(__file__), "dilink_list")

wsl_pre = "/mnt/d"
dilink_pre = "/storage/D0C4-856E"


for filename in os.listdir(wsl_path):
    print(filename)
    with open(os.path.join(wsl_path, filename)) as wsl_file, open(
        os.path.join(dilink_path, filename), "a+"
    ) as dilink_file:
        for line in wsl_file:
            line = line.replace(wsl_pre, dilink_pre)
            dilink_file.write(line)
