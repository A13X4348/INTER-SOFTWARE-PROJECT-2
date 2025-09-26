FROM python:3.11

WORKDIR /app
COPY origin.py ./
COPY audio_files ./

RUN pip install flask requests os

CMD ["python", "origin.py"]