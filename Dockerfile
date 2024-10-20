# Author(s): Russell Johnston <rujohns2@cisco.com>
#

FROM python:alpine

LABEL com.cisco.author="Russell Johnston <rujohns2@cisco.com>"

WORKDIR /usr/src/app

COPY src/ /usr/src/app/
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD python ./main.py --count $COUNT --key $API_KEY --url $API_URL