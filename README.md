## original Repo 
https://github.com/lucasnewman/f5-tts-mlx  

added :ffmpeg (brew) and yt-dlp (pip) to download videos from youtube in wav format


## Installation

```bash
pip3 install f5-tts-mlx
```

## Usage

```bash
python -m f5_tts_mlx.generate --text "The quick brown fox jumped over the lazy dog."
```

If you want to use your own reference audio sample, make sure it's a mono, 24kHz wav file of around 5-10 seconds:

```bash
python -m f5_tts_mlx.generate \
--text "The quick brown fox jumped over the lazy dog."
--ref-audio /path/to/audio.wav
--ref-text "This is the caption for the reference audio."
```

You can convert an audio file to the correct format with ffmpeg like this:

```bash
ffmpeg -i /path/to/audio.wav -ac 1 -ar 24000 -sample_fmt s16 -t 10 /path/to/output_audio.wav
```

See [examples/generate.py](./examples) for more options.

—

You can load a pretrained model from Python like this:

```python
from f5_tts_mlx import F5TTS

f5tts = F5TTS.from_pretrained("lucasnewman/f5-tts-mlx")

audio = f5tts.sample(...)
```

Pretrained model weights are also available [on Hugging Face](https://huggingface.co/lucasnewman/f5-tts-mlx).  

## python API notes (pap)
- limited length. you'd need to break the input into sentences, loop over sentences. and stitch at the end

- initial repo in pytorch includes an option to have dialogs (multi-voice: https://github.com/SWivid/F5-TTS `python inference-cli.py -c samples/story.toml` ). can probaly be achieved by looping over sentences and stiching.


## yt download
yt-dlp -x --audio-format wav --postprocessor-args "-ac 1 -ar 24000" "youtube-url"
