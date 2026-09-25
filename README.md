# Quiz App in Python

A simple command-line quiz application built with Python.

The project presents multiple-choice questions in the terminal, accepts user answers, checks them against the stored correct answers, and provides immediate feedback.

## 🎥 Preview

[▶️ Watch Project Demo](./Preview/Quize%20App%20in%20Python.mp4)

The preview demonstrates the quiz running in VS Code, displaying questions with four options, accepting user input, and showing whether the selected answer is correct or incorrect.

## ✨ Features

- Command-line based quiz interface
- Multiple-choice questions
- Four options for each question
- User input through the terminal
- Automatic answer validation
- Immediate correct/incorrect feedback
- Displays the correct answer when the selected answer is wrong
- Score-based quiz structure
- Questions stored using Python data structures

## 🎯 Project Overview

The Quiz App is a beginner-friendly Python project designed to practice interactive command-line programming.

The application stores quiz questions along with their options and correct answers. During execution, each question is displayed one at a time and the user selects an answer using `A`, `B`, `C`, or `D`.

The selected answer is then compared with the stored correct answer and the application provides feedback in the terminal.

## 🔄 How It Works

    1. The `run_quiz()` function starts the quiz.
    2. A collection of questions is stored inside the function.
    3. Each question contains:
       - The question text
       - Four answer options
       - The correct answer
    4. Questions are displayed sequentially in the terminal.
    5. The user enters an answer using A/B/C/D.
    6. The entered answer is checked against the correct answer.
    7. If the answer is correct, the application provides positive feedback.
    8. If the answer is incorrect, the correct answer is displayed.
    9. The quiz continues with the next question.

## 🧩 Question Structure

Each quiz question is represented using a dictionary containing the question, available options, and correct answer.

Example structure:

    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "C) Paris"
    }

The preview shows questions such as:

- What is the capital of France?
- What is the largest planet in our solar system?
- What is the chemical symbol for water?
- Who wrote "Romeo and Juliet"?
- What is the largest ocean on Earth?

## 📝 Quiz Interaction

The application displays questions in the terminal in the following style:

    Q1: What is the capital of France?
    A) London
    B) Berlin
    C) Paris
    D) Madrid

    Your answer (A/B/C/D):

After the user submits an answer, the application checks the response.

For an incorrect answer, the preview demonstrates feedback such as:

    Wrong! The correct answer is C) Paris

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Lists | Storing the collection of quiz questions |
| Dictionaries | Structuring individual questions |
| Functions | Organizing the quiz logic |
| Terminal Input | Accepting user answers |
| Conditional Logic | Checking submitted answers |

## 📚 Python Concepts Practiced

This project provides practice with:

- Functions
- Lists
- Dictionaries
- Strings
- User input
- Conditional statements
- Iteration
- Data structures
- Function calls
- Command-line interaction

Python's official documentation covers these core areas through its tutorials on control flow, functions, lists, dictionaries, and data structures. :chatgpt-content-reference{index="0"}

## 📁 Project Structure

    Quiz-App-in-Python/
    │
    ├── Preview_video/
    │   └── Quize App in Python.mp4
    │
    ├── main.py
    │
    └── README.md

## ▶️ Run Locally

### 1. Clone the Repository

    git clone https://github.com/dheerajmishra75/Quiz-App-in-Python.git

### 2. Navigate to the Project

    cd Quiz-App-in-Python

### 3. Run the Application

    python main.py

The quiz will start directly in the terminal.

## 🧪 Example Workflow

    Start Application
          ↓
    Display Question
          ↓
    Display Options A/B/C/D
          ↓
    User Enters Answer
          ↓
    Validate Answer
       ↙       ↘
    Correct   Incorrect
       ↓         ↓
    Continue   Show Correct Answer
          ↓
    Next Question

## 🎯 Learning Outcomes

Through this project, I practiced how to:

- Build a basic interactive Python application
- Store structured information using dictionaries
- Organize multiple questions using lists
- Create reusable functions
- Accept and process user input
- Implement answer validation
- Provide immediate feedback
- Work with command-line applications
- Apply basic programming logic to a real mini project

## 🚀 Future Improvements

Possible improvements for future versions include:

- Final score display
- Score percentage calculation
- Question randomization
- Multiple quiz categories
- Difficulty levels
- Timer-based questions
- Input validation for invalid options
- Larger question banks
- Restart quiz option
- High-score tracking

## 🔗 Project Links

- GitHub: https://github.com/dheerajmishra75/Quiz-App-in-Python

## 👨‍💻 Author

**Dheeraj Mishra**

B.Tech CSE Student | Python | Data Science | Machine Learning | Backend Development

## 📌 Disclaimer

This project was created for learning and practice purposes. The quiz questions are stored directly in the Python program and are intended for demonstration of basic programming concepts.
