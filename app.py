from flask import Flask, render_template, request, jsonify
import os
from googletrans import Translator

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method =="POST":
        try:
            txt_to_translated = request.form['text-to-translate']
            selected_language = request.form['select-language']
            translator = Translator()

            translated_txt = translator.translate(
                txt_to_translated,
                dest=selected_language)

            txt = translated_txt.text

            pronunciation_info = translated_txt.pronunciation
            if pronunciation_info == None:
                pronunciation_info = "<No data is available>"

            confidence = f"{translated_txt.extra_data['confidence'] * 100} %"
        except:
            pronunciation_info = "-"
            txt = "<ERROR: We are not able to handle this request right now>"
            confidence = "-"
        return render_template("index.html", translation_result = txt, pronunciation=pronunciation_info, confidence_level=confidence)
    else:
        return render_template("index.html")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)