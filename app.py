import os
from flask import Flask, request, jsonify, render_template
import ollama

app = Flask(__name__)

# Create a global Ollama client for reuse
ollama_client = ollama.Client()

@app.route('/')
def index():
    return render_template('index.html')

def generate_response(prompt):
    first_token = True
    try:
        # Start generation in streaming mode
        token_generator = ollama_client.generate(
            model="phi4",   # Specify the model
            prompt=prompt,
            stream=True     # Enable streaming
        )
        for token in token_generator:
            # Extract the response text if available; otherwise fallback to str(token)
            token_text = token.response if hasattr(token, "response") and token.response is not None else str(token)
            # Skip if token_text is empty
            if not token_text.strip():
                continue

            if first_token:
                yield token_text.encode('utf-8')
                first_token = False
            else:
                # Split the token text into words and yield each word individually,
                # prepending a space for separation.
                words = token_text.split()
                for word in words:
                    yield (" " + word).encode('utf-8')
    except Exception as e:
        yield f"\nError during streaming: {str(e)}".encode('utf-8')

@app.route('/api/infer', methods=['POST'])
def infer():
    try:
        data = request.get_json(force=True)
        prompt = data.get("prompt", "")
        if not prompt:
            return jsonify({"response": "No prompt provided."}), 400
        
        # Return a streaming plain-text response
        return app.response_class(generate_response(prompt), mimetype='text/plain')
    
    except ollama.OllamaError as e:
        return jsonify({"response": f"Ollama error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"response": f"Unexpected error: {str(e)}"}), 500

# Optional: Verify the model is available
def verify_model():
    try:
        models = ollama_client.list()
        if not any(model['name'] == 'phi4' for model in models['models']):
            print("Warning: phi4 model not found. Please pull the model first.")
    except Exception as e:
        print(f"Error checking models: {e}")

if __name__ == '__main__':
    verify_model()
    app.run(host="0.0.0.0", port=5000)