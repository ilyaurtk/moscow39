FROM python:3-slim
WORKDIR /app1
COPY ./app1.py /app1
RUN pip3 install flask requests
EXPOSE 80
ENTRYPOINT ["python3"]
CMD ["app1.py"]
