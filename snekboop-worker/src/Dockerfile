FROM python:3
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY worker.py /

ENTRYPOINT [ "python", "worker.py" ]