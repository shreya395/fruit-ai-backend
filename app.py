from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)  # Corrected __name__ to initialize the Flask app
CORS(app)

# Dummy data for FAQs
faqs = [
    {
        'id': 1,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://imgs.search.brave.com/DygaCUZLKX4VoJnPz4Ra8QPiJnM-5ONwEUCsGUDd3fA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/emluZXIuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzEy/L2hvdy10by1idXkt/dGhlLXN3ZWV0ZXN0/LXRhbmdlcmluZXMu/anBnLndlYnA'
    },
    {
        'id': 2,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://imgs.search.brave.com/DygaCUZLKX4VoJnPz4Ra8QPiJnM-5ONwEUCsGUDd3fA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/emluZXIuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzEy/L2hvdy10by1idXkt/dGhlLXN3ZWV0ZXN0/LXRhbmdlcmluZXMu/anBnLndlYnA'
    },
    {
        'id': 3,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://imgs.search.brave.com/DygaCUZLKX4VoJnPz4Ra8QPiJnM-5ONwEUCsGUDd3fA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/emluZXIuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzEy/L2hvdy10by1idXkt/dGhlLXN3ZWV0ZXN0/LXRhbmdlcmluZXMu/anBnLndlYnA'
    },
    {
        'id': 4,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://imgs.search.brave.com/DygaCUZLKX4VoJnPz4Ra8QPiJnM-5ONwEUCsGUDd3fA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/emluZXIuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzEy/L2hvdy10by1idXkt/dGhlLXN3ZWV0ZXN0/LXRhbmdlcmluZXMu/anBnLndlYnA'
    },
    {
        'id': 5,
        'title': 'How is Tangerine healthy?',
        'description': 'Tangerines are a great health booster due to their high vitamin C content, which supports the immune system and skin health.',
        'image': 'https://imgs.search.brave.com/DygaCUZLKX4VoJnPz4Ra8QPiJnM-5ONwEUCsGUDd3fA/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9hcmNo/emluZXIuY29tL3dw/LWNvbnRlbnQvdXBs/b2Fkcy8yMDIyLzEy/L2hvdy10by1idXkt/dGhlLXN3ZWV0ZXN0/LXRhbmdlcmluZXMu/anBnLndlYnA'
    },
    # Add more FAQs as needed
]

@app.route('/faqs', methods=['GET'])
def get_faqs():
    return jsonify(faqs)

@app.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({'error': 'FAQ not found'}), 404
    return jsonify(faq)

@app.route('/faqs', methods=['POST'])
def create_faq():
    new_faq = request.get_json()
    new_faq['id'] = len(faqs) + 1
    faqs.append(new_faq)
    return jsonify(new_faq), 201

@app.route('/faqs/<int:faq_id>', methods=['PUT'])
def update_faq(faq_id):
    faq = next((faq for faq in faqs if faq['id'] == faq_id), None)
    if faq is None:
        return jsonify({'error': 'FAQ not found'}), 404
    updated_data = request.get_json()
    faq.update(updated_data)
    return jsonify(faq)

@app.route('/faqs/<int:faq_id>', methods=['DELETE'])
def delete_faq(faq_id):
    global faqs
    faqs = [faq for faq in faqs if faq['id'] != faq_id]
    return jsonify({'message': 'FAQ deleted'})

if __name__ == '__main__':  # Corrected __name__ and __main__
    app.run(debug=True)
