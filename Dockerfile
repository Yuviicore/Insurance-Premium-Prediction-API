#base image
FROM python:3.11-slim

#workdir
WORKDIR /model_app.py

#copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#Copy rest of application
COPY . .

#port
EXPOSE 8000

#command
CMD ["uvicorn","model_app:app","--host","0.0.0.0","--port","8000"]
