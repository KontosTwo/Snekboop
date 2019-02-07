FROM python:3
COPY . /

RUN pip install -r requirements.txt
ENV SNEKBOOP_API_PORT 10001
CMD [ "python", "api.py" ]