# Use Ollama base image
FROM ollama/ollama

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

RUN python3 --version
RUN pip3 --version
RUN ls -la /app
RUN cat requirements.txt

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run Ollama and Flask app together
CMD ["./start.sh"]
