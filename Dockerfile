FROM python:3.12

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

COPY entrypoint.sh /

RUN chmod +x entrypoint.sh # Add this line to make the entrypoint.sh script executable

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



