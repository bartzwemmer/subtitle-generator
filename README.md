# Subtitle Generator
A small script to  generate subtitles files for a video.
Input a video file and a subtitle file (SRT) will be generated.

## Requirements

### Local
- Python 3.10+
- ffmpeg on the system path

### Docker
Have Docker installed and running.
`docker run -v C:/Users/bzwem/Docs/code/ogl-code/subtitle-generator/data:/data subs data/video.mp4 nl`
where `data/video.mp4` is the relative path to the video file and `nl` is the spoken language in the vide.