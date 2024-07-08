FROM python:latest

RUN git clone https://github.com/rogerpq/Scal.git /root/repthon

WORKDIR /root/repthon

RUN pip3 install --no-cache-dir -r requirements.txt

ENV PATH="/home/repthon/bin:$PATH"

CMD ["python3","-m","repthon"]
