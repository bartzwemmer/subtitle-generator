import whisper
from whisper.utils import get_writer
from pathlib import Path

from moviepy import VideoFileClip

import os, sys


def convert_mp4_to_wav(video_file: Path) -> Path:
    """Convert video to WAV audio file"""
    output_path = video_file.with_suffix(".wav")
    print(f"Converting video {video_file} to audio {output_path}...")
    video = VideoFileClip(str(video_file))
    video.audio.write_audiofile(str(output_path))
    video.close()
    return output_path


def transcribe_audio(audio_file: Path, language_code: str = "nl") -> None:
    model = whisper.load_model("large")
    print(f"Start transcribing audio {audio_file.name}...")
    result = model.transcribe(audio=audio_file.as_posix(), language=language_code)
    print("Finished transcribing audio...")
    # Get a writer and configure it with your preferred subtitle formatting
    writer = get_writer("srt", audio_file.parent.as_posix())
    writer(result, str(audio_file.with_suffix(".srt")), {"max_line_width":55, "max_line_count":2, "highlight_words":False} )
    print("write hard coded srt...")
    writer(result, "data/output.srts", {"max_line_width":55, "max_line_count":2, "highlight_words":False} )
    print("Finished saving transcript to SRT file...")
    print("Cleaning up...")
    os.remove(audio_file)
    print("Done!")


def main(file_name: str, language_code: str) -> None:
    transcribe_audio(convert_mp4_to_wav(Path(file_name)), language_code)


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python main.py <video_file.mp4> <language_code>")
        sys.exit(1)
    main(args[0], args[1])

