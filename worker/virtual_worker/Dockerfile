FROM python:3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY virtual_worker.py .
ENTRYPOINT [ "python3","virtual_worker.py" ]