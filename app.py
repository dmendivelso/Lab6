from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "¡Hola desde la versión 2.0! 🎉 "
# Health check endpoint for Kubernetes probes
@app.route("/health")
def health():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    app.run(
        host='0.0.0.0', # Required for containers
        port=5000
    )