#base image
FROM python:3.9

#workdir 
WORKDIR /app

#copy 
COPY . .

#run
RUN pip install -r requirements2.txt

#port
EXPOSE 5000

# command
CMD ["python", "flaskdemo.py"]

# to run streamlit file CMD ["streamlt", "run", "app.py"]