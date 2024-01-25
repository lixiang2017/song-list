s = "MP3 AAC FLAC WAV OPUS WV DSF DFF APE OGG M4A ALAC"
suffix = s.lower().split()
suffix = ["." + suf for suf in suffix]
print(suffix)
print(set(suffix))
# ['mp3', 'aac', 'flac', 'wav', 'opus', 'wv', 'dsf', 'dff', 'ape', 'ogg', 'm4a', 'alac']
# {'wav', 'ogg', 'flac', 'ape', 'm4a', 'dff', 'mp3', 'dsf', 'alac', 'wv', 'aac', 'opus'}

# ['.mp3', '.aac', '.flac', '.wav', '.opus', '.wv', '.dsf', '.dff', '.ape', '.ogg', '.m4a', '.alac']
# {'.ogg', '.dff', '.alac', '.mp3', '.ape', '.aac', '.dsf', '.wav', '.opus', '.m4a', '.flac', '.wv'}
