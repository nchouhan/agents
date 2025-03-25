# Web Application for Homework Assistance

This web application is designed to assist users with their homework questions by leveraging a set of specialized agents. The application takes user input and processes it to provide relevant assistance.

## Project Structure

```
web-app
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── static
│   └── style.css
├── requirements.txt
├── .env
└── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd web-app
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file in the root directory and add any necessary environment variables.

5. **Run the Application**
   ```bash
   python -m app.main
   ```

## Usage

- Open your web browser and navigate to `http://localhost:5000`.
- Enter your homework question in the provided form and submit it.
- The application will process your input and return relevant assistance based on the question type.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.