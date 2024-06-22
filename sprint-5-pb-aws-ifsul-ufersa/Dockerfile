FROM python:3.9
COPY . /app
WORKDIR /app
RUN rm -rf __pycache__
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["python", "main.py"]