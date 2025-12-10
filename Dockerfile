FROM python:3.12-slim
WORKDIR /speed_test
ENV TZ=Europe/Berlin
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /speed_test/logs
RUN mkdir -p /speed_test/data

CMD ["python","main.py"]
