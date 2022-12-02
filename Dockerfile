FROM python

COPY new.py /opt

RUN pip install flask

EXPOSE 5000:5000
WORKDIR /opt
ENTRYPOINT ["python3", "new.py"]
