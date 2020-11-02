FROM python:3.8

COPY pip.conf /root/.pip/pip.conf

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD exec uvicorn test:app --reload --host '0.0.0.0' --port 8000
