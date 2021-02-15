FROM python:3.9.1-slim-buster

RUN apt-get update && \
    apt-get install -y ffmpeg

RUN pip install --upgrade youtube-dl
RUN pip install -U discord.py

COPY ./src /src

CMD [ "python", "/src/davd.py" ]