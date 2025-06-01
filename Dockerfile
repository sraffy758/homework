# Use PyTorch base image that supports both CUDA and MPS
FROM pytorch/pytorch:latest

# Set working directory
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone ComfyUI repository
RUN git clone https://github.com/comfyanonymous/ComfyUI.git .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose the default ComfyUI port
EXPOSE 8188

# Set the default command to run ComfyUI
CMD ["python", "main.py"]
