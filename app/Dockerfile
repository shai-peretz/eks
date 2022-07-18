FROM python:3.7-alpine
ARG PORT
ENV PORT=$PORT
EXPOSE $PORT
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]