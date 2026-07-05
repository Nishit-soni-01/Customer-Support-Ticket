FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    NLTK_DATA=/usr/local/share/nltk_data

WORKDIR /app

RUN addgroup --system appgroup && adduser --system --group appuser

# COPY EVERYTHING FIRST so pip can find setup.py
COPY . .

# Now run the pip install
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Download NLTK data
RUN python -m nltk.downloader -d ${NLTK_DATA} stopwords

# Set permissions and switch user
RUN chown -R appuser:appgroup /app
USER appuser

EXPOSE 8080

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "2", "--threads", "4", "application:application"]