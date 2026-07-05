# 🤖 AI Chatbot with Live Weather & Forecast

An intelligent AI-powered chatbot built using **Python, Flask, HTML, CSS, and JavaScript**. The chatbot leverages the **Google Gemini API** to provide natural and intelligent responses while integrating the **OpenWeatherMap API** to deliver real-time weather updates and weather forecasts for cities around the world.

The project features a clean, modern user interface inspired by contemporary AI assistants, making it both visually appealing and user-friendly. It demonstrates API integration, backend development, frontend design, and real-time data handling.

---

# 📌 Project Overview

The AI Chatbot is designed to simulate conversations with users while also acting as a smart weather assistant. Users can ask general knowledge questions, programming-related queries, educational questions, and weather-related questions through a single interface.

The chatbot intelligently routes user requests:
- General questions are answered using the Google Gemini API.
- Weather-related queries are answered using the OpenWeatherMap API.
- Forecast-related queries retrieve upcoming weather conditions for the requested city.

This project showcases the practical implementation of Generative AI combined with REST APIs to build an interactive web application.

---

# ✨ Features

### 🤖 AI Chat Assistant
- Natural language conversation
- Answers educational and general knowledge questions
- Programming assistance
- Logical reasoning
- Summarization and explanation

### 🌤 Live Weather Information
- Current temperature
- Weather condition
- Feels-like temperature
- Humidity
- Wind information
- City and country details

### 📅 Weather Forecast
- Tomorrow's weather prediction
- Rain detection
- Forecast temperature
- Forecast weather conditions

### 💻 Modern User Interface
- Professional white theme
- Responsive layout
- Sidebar with recent chats
- New Chat functionality
- Elegant chat bubbles
- Animated AI robot illustration
- Smooth scrolling experience

### ⚡ Backend Features
- Flask web server
- REST API integration
- JSON request handling
- Error handling
- Dynamic response generation

---

# 🛠 Technologies Used

## Programming Languages
- Python
- HTML5
- CSS3
- JavaScript

## Backend Framework
- Flask

## APIs
- Google Gemini API
- OpenWeatherMap Current Weather API
- OpenWeatherMap Forecast API

## Libraries
- requests
- google-genai
- python-dotenv

---

# 📂 Project Structure

```
AI-Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env
│
├── static/
│   ├── style.css
│   ├── script.js
│   └── robot.png
│
└── templates/
    └── index.html
```

---

# 🚀 How It Works

1. The user enters a question into the chatbot.
2. Flask receives the request.
3. The application determines whether the query is weather-related or a general AI query.
4. If it is a weather query:
   - The city is identified.
   - OpenWeatherMap API is called.
   - Current weather or forecast data is retrieved.
5. If it is a general question:
   - The request is sent to the Gemini API.
   - Gemini generates an intelligent response.
6. The response is displayed in the chatbot interface.

---

# 💬 Example Questions

## AI Questions

- What is Artificial Intelligence?
- Explain Machine Learning in simple terms.
- What is Deep Learning?
- Write a Python program to reverse a string.
- Explain Object-Oriented Programming.
- Difference between SQL and NoSQL.
- Explain Data Structures.
- Tell me about Cloud Computing.
- How does Blockchain work?

## Weather Questions

- Weather in Vijayawada
- Temperature in Hyderabad
- Current weather in Paris
- Humidity in Tokyo
- Is it raining in Mumbai?
- Forecast for London
- Will it rain tomorrow in Delhi?
- Weather forecast for Bangalore
- Temperature in New York

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/sruthi-kurama/AI-Chatbot.git
```

Move into the project directory

```bash
cd AI-Chatbot
```

Install all required packages

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```text
GEMINI_API_KEY=Your_Gemini_API_Key
WEATHER_API_KEY=Your_OpenWeatherMap_API_Key
```

---

# ▶ Running the Project

Start the Flask server

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

# 🧠 Skills Demonstrated

- Python Programming
- Flask Web Development
- REST API Integration
- Generative AI Integration
- Prompt Engineering
- HTML & CSS UI Design
- JavaScript DOM Manipulation
- JSON Data Processing
- Error Handling
- Responsive Web Design
- Frontend and Backend Integration

---

# 🎯 Future Enhancements

The following features can be added in future versions:

- 🎤 Voice Input
- 🔊 Text-to-Speech Responses
- 🌍 Automatic Location Detection
- 📍 GPS-based Weather
- 🖼 Image Generation using AI
- 📂 File Upload and Analysis
- 👤 User Authentication
- 💾 Database for Chat History
- 🌙 Dark/Light Theme Toggle
- 🌐 Multi-language Support
- 📊 Weather Charts and Graphs
- 📱 Mobile Responsive Optimization

---

# 📸 Project Screenshots

> Add screenshots of your chatbot here after uploading the project.

Example:

- Home Screen
- AI Conversation
- Live Weather Result
- Weather Forecast
- Sidebar with Chat History

---

# 🎓 Learning Outcomes

This project helped strengthen my understanding of:

- Building full-stack web applications using Flask
- Working with Generative AI APIs
- Integrating multiple third-party APIs into a single application
- Designing modern and user-friendly interfaces
- Processing real-time data from external services
- Creating scalable chatbot architectures

---

# 👩‍💻 Author

**Sruthi Kurama**

BBA Student | Aspiring buiness anlytics enthusiast | AI & Technology Enthusiast

I enjoy building AI-powered applications and continuously learning new technologies related to Artificial Intelligence, Data Analytics, and Web Development.

GitHub:
https://github.com/sruthi-kurama

---

# 📄 License

This project is licensed for educational and learning purposes.

![alt text](<Screenshot (67).png>)

![alt text](<Screenshot (70).png>)

![alt text](<Screenshot (69).png>)




