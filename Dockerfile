# --- 1. Base Image ---
FROM python:3.10-slim

# --- 2. Set Working Dir ---
WORKDIR /app

# --- 3. Install Dependencies ---
COPY requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# --- 4. Copy Project Files ---
COPY . .

# --- 5. Expose Jupyter Port ---
EXPOSE 8888

# --- 6. Default Command: start JupyterLab ---
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''" ]
