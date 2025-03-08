// Секундомер
let timeLeft = 60;
const timerElement = document.getElementById('timer');
let timerInterval;

function updateTimer() {
    timerElement.textContent = `Осталось времени: ${timeLeft} секунд`;
    if (timeLeft <= 0) {
        clearInterval(timerInterval);
        alert("Время вышло!");
        document.getElementById('quiz-form').submit(); // Автоматически отправить форму
    }
    timeLeft--;
}

// Запуск таймера
timerInterval = setInterval(updateTimer, 1000);

// Обработка формы
document.getElementById('quiz-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем стандартное поведение формы

    // Останавливаем таймер
    clearInterval(timerInterval);

    const formData = new FormData(this);
    const answers = [];
    const questionsLength = parseInt(this.getAttribute('data-questions-length')); // Получаем длину массива

    // Собираем ответы
    for (let i = 0; i < questionsLength; i++) {
        const selectedAnswers = formData.getAll(`question${i}`); // Получаем все выбранные ответы для вопроса
        answers.push({
            question_index: i,
            selected_answers: selectedAnswers
        });
    }

    // Отправляем ответы на сервер
    fetch('/check_answer', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(answers)
    })
    .then(response => response.json())
    .then(data => {
        // Обрабатываем ответ от сервера
        const resultDiv = document.getElementById('result');
        let resultText = "";
        data.forEach((result, index) => {
            resultText += `Вопрос ${index + 1}: ${result.is_correct ? "Правильно!" : "Неправильно!"}<br>`;
        });
        resultDiv.innerHTML = resultText;
    })
    .catch(error => {
        console.error('Ошибка:', error);
    });
});