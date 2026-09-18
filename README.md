# 🎬 IMDB Sentiment Analysis

A Natural Language Processing (NLP) project that uses a deep learning model to classify text reviews as **Positive** or **Negative**.

The model was trained using the **IMDB Dataset - Sentiment Analysis** from Kaggle and deployed through a simple Flask web application.

## 🚀 Features

- NLP-based sentiment classification
- Trained on the IMDB movie review dataset
- Text tokenization and sequence preprocessing
- Deep learning model built with TensorFlow/Keras
- Saved trained `.keras` model
- Saved tokenizer using Pickle
- Flask web interface
- Real-time sentiment prediction

## 📂 Project Structure


IMDB-Sentiment-Analysis/
│
├── app.py
├── Sentiment-Analysis.keras
├── tokenizer.pkl
├── requirements.txt
│
└── templates/
    └── index.html
🧠 Model

The model was trained to classify movie reviews into two sentiment classes:

Positive
Negative

The text is first converted into numerical sequences using the trained tokenizer. The sequences are then padded and passed to the trained Keras model for prediction.

Prediction Pipeline
User Input
    ↓
Text Preprocessing
    ↓
Tokenization
    ↓
Sequence Padding
    ↓
Keras Model
    ↓
Sentiment Prediction
    ↓
Positive / Negative
📊 Dataset

The model was trained using the IMDB Dataset - Sentiment Analysis available on Kaggle.

Dataset:
IMDB Dataset - Sentiment Analysis

The dataset contains movie reviews labeled according to their sentiment.

🌐 Flask Application

The project includes a simple Flask web application.

Users can enter a movie review into the web interface, and the application sends the text through the trained NLP model.

Example:

Input:
This movie was absolutely amazing. I loved every minute of it!

Output:
Positive

Another example:

Input:
The movie was boring and the story was terrible.

Output:
Negative
🛠️ Technologies Used
Python
TensorFlow
Keras
Flask
NumPy
Pickle
NLP
HTML
CSS
📦 Installation

Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Move into the project directory:

cd IMDB-Sentiment-Analysis

Install the required dependencies:

pip install -r requirements.txt
▶️ Running the Application

Run:

python app.py

Then open:

http://127.0.0.1:5000

in your browser.

📁 Model Files

The repository contains:

Sentiment-Analysis.keras

The trained TensorFlow/Keras sentiment analysis model.

tokenizer.pkl

The tokenizer used during training to convert text into numerical sequences.

It is important to use the same tokenizer during prediction that was used during model training.

🔮 Future Improvements
Deploy the application online
Add confidence scores
Improve the UI
Add sentiment probability visualization
Add batch prediction for multiple reviews
Add support for larger text inputs
👨‍💻 Author

Asad Ajaz

GitHub: asad673-creator

📄 Dataset Credit

Dataset provided by Bhavik Jikadara on Kaggle.

https://www.kaggle.com/datasets/bhavikjikadara/imdb-dataset-sentiment-analysis
