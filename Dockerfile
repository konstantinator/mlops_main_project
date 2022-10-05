FROM python:3.8-slim

RUN mkdir app

WORKDIR /app

COPY requirements.txt $WORKDIR

RUN apt-get update && apt-get clean && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -U pip && \
    pip install jupyter && \
    pip install -r requirements.txt --no-cache-dir

ENV PYTHONPATH "${PYTHONPATH}:/app"

# CMD jupyter notebook --ip 0.0.0.0 --port 9988 --allow-root --NotebookApp.token=""

ENTRYPOINT [ "bash" ]