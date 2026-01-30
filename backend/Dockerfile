FROM python:3.14-slim
LABEL authors="Ryan Shores"

WORKDIR /usr/src/app

# Install uvicorn
RUN pip install --upgrade pip && pip install uvicorn[standard]

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]