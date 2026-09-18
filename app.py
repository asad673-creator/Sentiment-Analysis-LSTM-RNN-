from flask import Flask, render_template, request
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = tf.keras.models.load_model("Sentiment-Analysis.keras")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)


@app.route("/", methods=["GET", "POST"])
def home():
    sentiment = None
    text = ""

    if request.method == "POST":
        text = request.form["text"]

        sequence = tokenizer.texts_to_sequences([text])

        max_length = model.input_shape[1]

        if max_length is None:
            max_length = 100

        padded = pad_sequences(
            sequence,
            maxlen=max_length,
            padding="post"
        )

        prediction = model.predict(padded, verbose=0)

        if prediction.shape[-1] == 1:
            sentiment = "Positive" if prediction[0][0] >= 0.5 else "Negative"
        else:
            classes = ["Negative", "Neutral", "Positive"]
            sentiment = classes[prediction.argmax()]

    return render_template(
        "index.html",
        sentiment=sentiment,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)