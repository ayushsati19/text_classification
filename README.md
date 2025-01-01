# Text Classification Project

This project is part of the ML Ops course at Jio Institute. The goal of this project is to build and deploy a robust text classification model using modern machine learning techniques.

## Project Structure

```
text_classification/
├── app/
│   ├── main.py         # FastAPI app
│   ├── routes.py       # API routes
├── model/
│   ├── train.py        # Model training
│   ├── predict.py      # Prediction logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## Features

- **Model Training**: Scripts for training text classification models.
- **API Deployment**: A FastAPI-based application for serving predictions.
- **Scalable Design**: Modular code structure for easy updates and maintenance.

## Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/text_classification.git
   cd text_classification
   ```

2. Create and activate a virtual environment (optional):

   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Training the Model

Run the training script to build the classification model:

```bash
python model/train.py
```

### Starting the API Server

Use `uvicorn` to start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Deployment

The application can be deployed using the following command:

```bash
uvicorn app.main:app --reload
```

Refer to the [documentation](link/doc) for detailed deployment instructions.

## Contributing

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed explanation of your changes.

For major changes, please open an issue first to discuss your ideas.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Jio Institute** for providing the course and resources.
- **Open-Source Community** for their invaluable tools and libraries.

