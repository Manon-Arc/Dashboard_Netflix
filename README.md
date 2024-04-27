# Netflix Dashboard Project
Project by  __ARCAS__ Manon, __Guillemot__ Killian, __Jacolot__ Marine and __Barboteau__ Mathieu.

Welcome to the Netflix Dashboard project ! 
This project is aimed at providing a web dashboard to display movies and TV shows available on Netflix. 
This README will guide you through setting up your environment, installing the required packages, and starting the project.

## 📌 Table of contents:

I. [Badges](#🎯-badges)

II. [License](#📑-license)

III. [Prerequisites](#🔧-prerequisites)

IV. [Starting the Project](#💻-starting-the-project)

V. [Project Overview](#🌟-project-overview)

## 🎯 Badges

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/)
[![Python logo](https://img.shields.io/badge/Language-Python-green
)](https://www.php.net/)


## 📑 License

[MIT](https://choosealicense.com/licenses/mit/)


## 🔧 Prerequisites
- [Python 3.12](https://www.python.org/downloads/) installed on your system.
- [Pip](https://pip.pypa.io/en/stable/installation/) package manager installed.
- Setup Instructions
### 1. Clone the Repository
```bash
git clone https://github.com/Darkblue5031/projet_data
```
### 2. Navigate to the Project Directory

```bash
cd projet_data
```
### 3. Create a Virtual Environment
```bash
python3 -m venv venv
```
### 4. Activate the Virtual Environment
#### On Windows:
```bash
venv\Scripts\activate
```
#### On macOS and Linux:
```bash
source venv/bin/activate
```
### 5. Install Required Packages
```bash
pip install -r requirement.txt
```
## 💻 Starting the Project

### 1. Navigate to the Dashboard Directory

```bash
cd Dashboard
```
### 2. Run the Django Migrations
```bash
python manage.py migrate
```
### 3. Start the Development Server
```bash
python manage.py runserver
```
### 4. Access the Dashboard
Visit http://localhost:8000 in your web browser to view the Netflix Dashboard.

## 🌟 Project Overview
The Netflix Dashboard project is a web application built using Python Django framework. 
It fetches data about movies and TV shows available on Netflix and presents them in an interactive dashboard format. 
Users can browse through the content and explore details about their favorite movies and shows.








