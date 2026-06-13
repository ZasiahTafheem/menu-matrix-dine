# menu-matrix-dine
MenuMatrix-Dine is a streamlined command-line interface (CLI) application designed to simulate a modern restaurant ordering process. Built entirely in Python, the project demonstrates advanced control flow, defensive programming practices through strict runtime input validation, and optimized data tracking using nested dictionary models.

## ✨ Key Features

* **🗂️ Grouped Menu Matrix:** Organizes food items into distinct, logical categories (e.g., Coffee, Burgers, Desserts) utilizing multi-dimensional nested Python dictionaries.
* **🛡️ Defensive Data Validation:** Implements real-time string sanitization (`.lower().strip()`) and numeric verification (`.isdigit()`) to ensure the application never crashes from user typos or illegal character entries.
* **🔢 Dynamic Quantity Adjustments:** Allows users to request specific item quantities, automatically updates the basket dictionary, and handles duplicate additions flawlessly.
* **🧾 Structured Receipt Engine:** Generates a beautifully aligned tabular summary detailing quantities, item names, individual prices, and the final total cost upon checking out.

## 🚀 How to Run the Application

### 📋 Prerequisites
Make sure you have Python installed on your local computer. 

## 🛠️ Development Tools & Methodology
This project was developed utilizing an AI-assisted engineering workflow:
- **Core Logic & Architecture:** Designed manually to implement nested dictionary models and tabular string formatting constraints.
- **AI Collaboration (Google Gemini):** Utilized Gemini as a pairing partner to accelerate workflow, explore robust input validation patterns (`.isdigit()`), and        optimize error-handling strategies.
- **Code Review:** All AI-assisted suggestions were manually reviewed, refactored, and tested to ensure code stability and crash resistance.
