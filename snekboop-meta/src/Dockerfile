FROM python:3
COPY requirements.txt /
RUN pip install -r requirements.txt
COPY meta.py /

ENTRYPOINT [ "python", "meta.py" ]