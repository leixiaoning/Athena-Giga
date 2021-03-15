import os
import kaldiio
import pandas

input_dir = 'examples/asr/giga/data/newwavs.scp'

csv_file_path = 'examples/asr/giga/data/newwavs2.scp'

with open(input_dir) as f:
    lines = f.readlines()


files = []
for i in lines:
    name, wavfile, text, speaker = i.strip().split('\t')
    w = kaldiio.load_mat(wavfile)
    len = int(w[1].shape[0] / w[0] * 1000)
    files.append((wavfile, len, text, speaker))

df = pandas.DataFrame(
        data=files, columns=["wav_filename", "wav_length_ms", "transcript", "speaker"]
    )
df.to_csv(csv_file_path, index=False, sep="\t")

print("done")