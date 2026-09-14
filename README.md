# Commercial Property Price Prediction

A portfolio-style machine learning project that predicts commercial property sale prices using a realistic synthetic dataset. The project demonstrates a complete regression workflow for tabular price estimation while keeping the data public-safe and free from proprietary or confidential information.

## Project Objective

This project aims to build a practical and reproducible price prediction model for commercial real estate using structured listing attributes such as:

- location
- property size
- age and building characteristics
- floor information
- room and layout features
- market context proxies

The main goal is to compare multiple regression approaches and select a model that balances predictive accuracy and stability.

## Dataset

The repository includes a synthetic commercial property dataset designed to reflect realistic listing behavior without exposing any real company data or private records.

- `data/sample_data.csv` — synthetic commercial property listings
- `create_sample_data.py` — script used to generate the dataset

## Repository Structure

```text
.
├── README.md
├── requirements.txt
├── create_sample_data.py
├── data/
│   └── sample_data.csv
├── notebook/
│   └── commercial_property_price_prediction.ipynb
└── .gitignore
```

## Workflow

The notebook follows a full machine learning pipeline based on a synthetic public-safe dataset:

1. Data loading and exploratory analysis
2. Missing value and data quality checks
3. Feature cleaning and type standardization
4. Feature engineering, including a general market-effect proxy derived from local pricing patterns
5. Train/validation split
6. Model comparison and evaluation
7. Hyperparameter tuning
8. Final model selection and error analysis

## Modeling Approach

The project evaluates multiple regression models, including:

- Linear and regularized models
- Tree-based ensemble methods
- XGBoost for stronger predictive performance
- Model diagnostics and performance comparison

## Tech Stack

- Python
- pandas
- NumPy
- scikit-learn
- XGBoost
- matplotlib
- yellowbrick
- Jupyter Notebook

## Local Setup

```bash
git clone <repository-url>
cd Commercial-Property-Price-Prediction
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run the Notebook

Open the notebook from the project root:

```bash
jupyter notebook notebook/commercial_property_price_prediction.ipynb
```

## Notes

This project is intentionally designed for public GitHub sharing and portfolio presentation. It uses synthetic data only and does not rely on external index files or proprietary market datasets. Instead, it derives a general market-effect proxy from the sample data itself to reflect local pricing pressure while remaining privacy-safe and reproducible.

The narrative and modeling workflow in the notebook are intentionally aligned with this public-safe setup, so the project can be shared openly without implying access to confidential or real company data.
