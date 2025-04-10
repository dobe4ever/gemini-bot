# FROM python:3.9.18-slim-bullseye
FROM python:3.11-slim-bookworm
WORKDIR /app
COPY ./ /app/
RUN pip install --no-cache-dir -r requirements.txt
ENV BOT_TOKEN=""
ENV GEMINI_API_KEYS=""
CMD ["sh", "-c", "python main.py ${BOT_TOKEN} ${GEMINI_API_KEYS}"]
