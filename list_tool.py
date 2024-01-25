import os


root_path = "/mnt/d/Tianyi_yunpan/"

dirs = os.listdir(root_path)
print(dirs)

[
    "570自听音乐备份 内封歌词 封面",
    "1022首中文精选高格式-24bit-96khz-wav(126GB)",
    "2200首无损音乐大合集",
    "华语----精选推荐 538首经典",
    "歌手录音室专辑合集",
    "周杰伦(2000-2022)CD专辑.正版CD抓轨.[WAV+CUE][约10.37GB]",
]

for item in dirs:
    if os.path.isdir(os.path.join(root_path, item)):
        print(item)

path_to_songlist = {
    "570自听音乐备份 内封歌词 封面": "570自听",
    "1022首中文精选高格式-24bit-96khz-wav(126GB)": "1022首中文精选",
    "2200首无损音乐大合集/1、APE格式合集": "2200首无损-APE",
    "2200首无损音乐大合集/2、FLAC格式合集/FLAC格式无损音乐合集": "2200首无损-FLAC",
    "华语----精选推荐 538首经典": "华语538首经典",
    "歌手录音室专辑合集": "歌手录音室专辑合集",
    "周杰伦(2000-2022)CD专辑.正版CD抓轨.[WAV+CUE][约10.37GB]": "周杰伦(2000-2022)正版CD抓轨",
}


# https://moriafly.xyz/HiMoriafly/docs/salt-player/scan
# 支持的文件拓展名为 MP3 AAC FLAC WAV OPUS WV DSF DFF APE OGG M4A ALAC （仅使用 Android 媒体库方式也被限制在这些格式中，仅允许子集）。
supported_suffix = {
    ".ogg",
    ".dff",
    ".alac",
    ".mp3",
    ".ape",
    ".aac",
    ".dsf",
    ".wav",
    ".opus",
    ".m4a",
    ".flac",
    ".wv",
}


def dump_for_each(each_path, songlist_name):
    with open(
        os.path.join(os.path.dirname(__file__), "wsl_list", f"{songlist_name}.txt"),
        "a+",
    ) as f:
        # each song list path: each_path
        for sub_root, dirs, files in os.walk(each_path):
            print("======dirs===========")
            for name in dirs:
                print(os.path.join(sub_root, name))
            print("======files===========")
            for name in files:
                _, extension = os.path.splitext(name)
                print("extension", extension)
                if extension in supported_suffix:
                    full_path = os.path.join(sub_root, name)
                    print(full_path)
                    f.write(full_path + "\n")


for path, songlist_name in path_to_songlist.items():
    if "歌手录音室专辑合集" == path:
        # do for each singer
        text_to_strip = [
            "录音室专辑合集",
            " 专辑合集 FLAC 分轨",
            "音室专辑+EP合集",
            "合集",
        ]
        for item in os.listdir(os.path.join(root_path, path)):
            print(item)
            stripped_item = item
            for t in text_to_strip:
                stripped_item = stripped_item.replace(t, "")
            stripped_item = stripped_item.replace(" ", "")
            print(item, stripped_item)
            # dump
            each_path = os.path.join(root_path, path, item)
            dump_for_each(each_path, stripped_item)
    # elif path == "周杰伦(2000-2022)CD专辑.正版CD抓轨.[WAV+CUE][约10.37GB]":
    elif path == "not existed path":
        with open(
            os.path.join(os.path.dirname(__file__), "wsl_list", f"{songlist_name}.txt"),
            "a+",
        ) as f:
            print(path)
            # each song list path
            each_path = os.path.join(root_path, path)
            for sub_root, dirs, files in os.walk(each_path):
                print("======dirs===========")
                for name in dirs:
                    print(os.path.join(sub_root, name))
                print("======files===========")
                for name in files:
                    _, extension = os.path.splitext(name)
                    print("extension", extension)
                    if extension in supported_suffix:
                        full_path = os.path.join(sub_root, name)
                        print(full_path)
                        f.write(full_path + "\n")
