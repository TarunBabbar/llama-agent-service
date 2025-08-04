# Use Ollama base image
FROM ollama/ollama

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all app files
COPY . .

# Expose Flask port
EXPOSE 5000

# Add this line at the bottom, before CMD
ENTRYPOINT []

# Run Ollama and Flask app together
CMD ["./start.sh"]
