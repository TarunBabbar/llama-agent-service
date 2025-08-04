# Use base image with Ollama installed
FROM ollama/ollama

# Install Python
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set workdir
WORKDIR /app

# Copy app files
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

# Run on port 8000
EXPOSE 8000

CMD ["./start.sh"]
