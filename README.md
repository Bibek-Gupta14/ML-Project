# 🎯 END-TO-END ML PROJECT

A comprehensive machine learning project implementing a complete pipeline for student performance prediction with data ingestion, transformation, model training, and deployment.

---

## 📋 Project Overview

This project demonstrates a production-ready machine learning workflow, including:
- **Data Ingestion** 📥: Loading and processing raw data
- **Data Transformation** 🔄: Feature engineering and preprocessing
- **Model Training** 🤖: Building and training ML models
- **Pipeline Architecture** 🏗️: Modular and scalable design
- **Web Application** 🌐: Flask-based web interface for predictions
- **Deployment Ready** 🚀: Docker and Elastic Beanstalk configuration

---

## 📁 Project Structure

```
ML Project/
├── 📄 app.py                          # Main Flask application
├── 📄 application.py                  # Alternative application entry point
├── 📄 setup.py                        # Package setup configuration
├── 📄 requirements.txt                # Project dependencies
├── 📄 README.md                       # Project documentation
│
├── 📂 src/                            # Source code package
│   ├── 📄 __init__.py
│   ├── 📄 exception.py               # Custom exception handling
│   ├── 📄 logger.py                  # Logging configuration
│   ├── 📄 utils.py                   # Utility functions
│   │
│   ├── 📂 components/                # Core ML components
│   │   ├── 📄 data_ingestion.py      # Data loading and ingestion
│   │   ├── 📄 data_transformation.py # Feature engineering & preprocessing
│   │   └── 📄 model_trainer.py       # Model training logic
│   │
│   └── 📂 pipeline/                  # ML pipelines
│       ├── 📄 train_pipeline.py      # Training pipeline
│       └── 📄 predict_pipeline.py    # Prediction pipeline
│
├── 📂 notebook/                       # Jupyter notebooks
│   ├── 📓 model_training.ipynb       # Model exploration & training
│   ├── 📓 stud_performance.ipynb     # Data analysis & visualization
│   └── 📂 data/
│       └── 📊 stud.csv               # Student dataset
│
├── 📂 templates/                      # Web UI templates
│   ├── 🎨 home.html                  # Home page
│   └── 🎨 index.html                 # Prediction form page
│
├── 📂 artifacts/                      # Saved models and data
│   ├── 🤖 model.pkl                  # Trained model
│   ├── 🔧 preprocessor.pkl           # Data preprocessor
│   ├── 📊 raw_data.csv               # Raw dataset
│   ├── 📊 train.csv                  # Training data
│   └── 📊 test.csv                   # Testing data
│
├── 📂 logs/                           # Application logs
│
├── 📂 .ebextension/                   # AWS Elastic Beanstalk config
│   └── 📄 python.config
│
└── 📂 Ml_Project.egg-info/            # Package metadata
```

---

## 🔧 Key Components

### **Data Ingestion** (`src/components/data_ingestion.py`)
- Loads raw data from CSV files
- Splits data into train and test sets
- Handles data validation and cleaning

### **Data Transformation** (`src/components/data_transformation.py`)
- Feature engineering and selection
- Preprocessing (scaling, encoding, etc.)
- Creates pipelines for reproducibility

### **Model Training** (`src/components/model_trainer.py`)
- Trains multiple ML algorithms
- Hyperparameter tuning
- Model evaluation and selection
- Saves best model artifacts

### **Pipelines** (`src/pipeline/`)
- **train_pipeline.py**: Orchestrates the entire training workflow
- **predict_pipeline.py**: Handles inference on new data

### **Web Application** (`app.py`, `application.py`)
- Flask-based REST API
- Interactive web interface
- Real-time predictions

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip and conda environment

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd ML\ Project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 📊 Data

The project uses student performance data (`stud.csv`):
- **Raw Data**: `artifacts/raw_data.csv`
- **Training Set**: `artifacts/train.csv`
- **Testing Set**: `artifacts/test.csv`

---

## 🏃 Running the Project

### Train the Model
```bash
python -m src.pipeline.train_pipeline
```

### Run the Web Application
```bash
python app.py
```

Then navigate to `http://localhost:5000` in your browser.

---

## 📦 Deployment

### Docker
```bash
docker build -t ml-project .
docker run -p 5000:5000 ml-project
```

### AWS Elastic Beanstalk
Configuration files are provided in `.ebextension/` for easy deployment.

---

## 🛠️ Utility Functions

- **exception.py**: Custom exception handling for better error management
- **logger.py**: Structured logging for debugging and monitoring
- **utils.py**: Helper functions for common tasks

---

## 📈 Project Workflow

```
Raw Data → Ingestion → Transformation → Training → Evaluation → Deployment
   📊        📥          🔄             🤖         📈         🌐
```

---

## ✨ Features

- ✅ Modular and scalable architecture
- ✅ Production-ready code structure
- ✅ Comprehensive error handling
- ✅ Logging and monitoring
- ✅ Web interface for predictions
- ✅ Docker support
- ✅ Cloud deployment ready

---

## 👤 Author

Created an end-to-end ML project lifecycle.

- ✅ Name: Bibek Gupta
- ✅ Email: bibekg1406@gmail.com

---

**Last Updated**: January 2026
