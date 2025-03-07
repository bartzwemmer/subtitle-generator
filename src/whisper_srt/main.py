import whisper
from whisper.utils import get_writer
from pathlib import Path


from moviepy import VideoFileClip

import os

ffmpeg_path = "C:/Apps/FFmpeg-Builds-latest/bin"  # Full path to bin folder
os.environ["PATH"] += os.pathsep + ffmpeg_path


def convert_mp4_to_wav(video_file: Path) -> Path:
    """Convert video to WAV audio file"""
    output_path = video_file.with_suffix(".wav")
    print(f"Converting video {video_file} to audio {output_path}...")
    video = VideoFileClip(str(video_file))
    video.audio.write_audiofile(str(output_path))
    video.close()
    return output_path


def transcribe_audio(audio_file: Path) -> None:
    model = whisper.load_model("base")
    print(f"Start transcribing audio {audio_file.name}...")
    result = model.transcribe(audio=audio_file.name)
    print("Finished transcribing audio...")
    # Get a writer and configure it with your preferred subtitle formatting
    writer = get_writer("srt", ".")
    writer(result, str(audio_file.with_suffix(".srt")), {"max_line_width":55, "max_line_count":2, "highlight_words":False} )
    print("Finished saving transcript to SRT file...")
    print("Cleaning up...")
    os.remove(audio_file)
    print("Done!")


def main() -> None:
    transcribe_audio(convert_mp4_to_wav(Path("TrainingWithUliana.mp4")))


if __name__ == "__main__":
    main()
