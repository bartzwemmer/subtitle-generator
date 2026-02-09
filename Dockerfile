FROM jrottenberg/ffmpeg:8-ubuntu-edge

RUN apt update && apt upgrade -y && apt install python3 python3-pip python3-virtualenv -y 

COPY . .

# Set up virtual environment
RUN virtualenv -p 3.12 env
ENV VIRTUAL_ENV=/env
ENV PATH=/env/bin:$PATH 

RUN pip install ffmpeg>=1.4 ffmpeg-python>=0.2.0 moviepy>=2.1.2 openai-whisper>=20240930 . 

ENTRYPOINT ["python3", "./src/whisper_srt/main.py"]