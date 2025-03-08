from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Пример вопросов и ответов
questions = [
    {
        "question": "Какой язык программирования используется для создания веб-приложений?",
        "options": ["Python", "Java", "C++", "JavaScript"],
        "answer": ["JavaScript"]  # Ответ теперь может быть списком
    },
    {
        "question": "Какой фреймворк используется для создания веб-приложений на Python?",
        "options": ["Django", "Flask", "Pyramid", "All of the above"],
        "answer": ["All of the above"]  # Ответ теперь может быть списком
    }
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/check_answer', methods=['POST'])
def check_answer():
    data = request.json
    results = []

    for answer in data:
        question_index = answer['question_index']
        selected_answers = answer['selected_answers']
        correct_answers = questions[question_index]['answer']
        
        # Проверяем, что выбраны только правильные ответы (без лишних)
        is_correct = (
            set(selected_answers) == set(correct_answers))  # Сравниваем множества
        results.append({"question_index": question_index, "is_correct": is_correct})

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)