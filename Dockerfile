FROM python:3.10.6-slim

COPY package_folder /package_folder
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# When testing locally, uncomment this line:
CMD uvicorn package_folder.api.escaladata_api:app --reload --host 0.0.0.0

# # When ready for cloud, uncomment this line:
# CMD uvicorn app.simple:app --host 0.0.0.0 --port $PORT
