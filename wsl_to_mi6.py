import os

wsl_path = os.path.join(os.path.dirname(__file__), "wsl_list")
mi6_path = os.path.join(os.path.dirname(__file__), "mi6_list")

wsl_pre = "/mnt/d"
mi6_pre = "/mnt/media_rw/D0C4-856E"


for filename in os.listdir(wsl_path):
    print(filename)
    with open(os.path.join(wsl_path, filename)) as wsl_file, open(
        os.path.join(mi6_path, filename), "a+"
    ) as mi6_file:
        for line in wsl_file:
            line = line.replace(wsl_pre, mi6_pre)
            mi6_file.write(line)
