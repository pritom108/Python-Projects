<h1 align="center">🧮 Smart Calculator – Streamlit App</h1>

<p align="center">
  <b>A multi-mode, modern, professional scientific calculator built using Python, OOP, and Streamlit.</b><br>
  Supports Normal Math, Complex Numbers, Base-N Conversions, and Matrix Operations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## ✨ Features

### 🔹 **1. Normal Math Mode**
- Addition, subtraction, multiplication, division  
- Scientific functions:  
  ✔ Trigonometry  
  ✔ Logarithms  
  ✔ Exponentials  

---

### 🔹 **2. Complex Number Mode**
- Supports **Rectangular (x + jy)** and **Polar (r ∠ θ)** forms  
- Convert both ways  
- Perform operations:  
  ✔ Addition  
  ✔ Subtraction  
  ✔ Multiplication  
  ✔ Division  

---

### 🔹 **3. Base-N Mode**
- Convert between **Binary, Octal, Decimal, Hexadecimal**  
- View representations in all bases  
- Compute:  
  ✔ 1’s Complement  
  ✔ 2’s Complement  

---

### 🔹 **4. Matrix Mode**
- Create matrices of any size  
- Operations supported:  
  ✔ Addition  
  ✔ Multiplication  
  ✔ Transpose  
  ✔ Determinant  
  ✔ Inverse  
- Clean UI for inputting matrix elements  

---

## 📁 Project Structure
<pre>
  smart-calculator/
│
├── app.py # Streamlit UI
├── requirements.txt
├── .gitignore
│
├── smart_calc/
│ ├── init.py
│ ├── core.py # Shared utilities
│ ├── normal_ops.py # Normal math operations
│ ├── complex_ops.py # Complex number engine
│ ├── base_ops.py # Base-N conversion engine
│ └── matrix_ops.py # Matrix operations
│
└── tests/
└── test_basic.py
</pre>
