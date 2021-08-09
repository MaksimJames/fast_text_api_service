FROM python:3.8
ENV PYTHONUNBUFFERED=1
WORKDIR /predict_category
COPY requirements.txt /predict_category/
RUN pip install -r requirements.txt
COPY . /predict_category/