import f5_tts_mlx.generate

text_to_process= "Even the significant resources allocated by billionaires pursuing immortality seem minuscule - if not misdirected- when faced with the fundamental nature of disorder. Our species remains bound to manage natural death and, naturally, we build machines to do so. "

f5_tts_mlx.generate.generate(
    generation_text= text_to_process,
    ref_audio_path="sample.wav",
    ref_audio_text="Voice of Snoop Dogg",
    output_path="snoop_story.wav",
    speed=0.6,
    )