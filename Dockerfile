FROM python:3.10-slim

WORKDIR /app

# Copy requirements first (caching optimization)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install -e .

# Expose same port as Flask
EXPOSE 5000

CMD ["martian-compiler"]
