FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV MYSQL_HOST=<your-database-host>
ENV MYSQL_USER=root
ENV MYSQL_PASSWORD=Karthick.2002
ENV MYSQL_DB=attendance_db
ENV MAIL_SERVER=smtp.gmail.com
ENV MAIL_PORT=587
ENV MAIL_USERNAME=manokarthick.ks741@gmail.com
ENV MAIL_PASSWORD=zldx bawd gcln jqlw
EXPOSE 5000
CMD ["python", "app.py"]
