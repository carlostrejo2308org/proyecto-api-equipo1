FROM python:3.10.4

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements2.txt

COPY . .

CMD [ "python", "book.py" ]