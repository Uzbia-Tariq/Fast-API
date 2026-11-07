# Fast-API: Diabetes Prediction

A small FastAPI project that loads a saved Logistic Regression model (`Mymdoel.pkl`) and predicts a diabetes class from six input features. It includes a simple HTML page.

## Project files

- `main.py` - FastAPI application and prediction endpoint
- `Mymdoel.pkl` - trained machine-learning model (filename retained to match the supplied model)
- `index.html` - browser interface
- `requirements.txt` - Python dependencies

## Run in VS Code (Windows)

1. Extract the `Fast-API` folder.
2. Open VS Code.
3. Select **File > Open Folder** and choose `Fast-API`.
4. Open **Terminal > New Terminal**.
5. Check Python is installed:

   ```powershell
   python --version
   ```

6. Create a virtual environment:

   ```powershell
   python -m venv .venv
   ```

7. Activate it in PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt terminal and run:

   ```cmd
   .venv\Scripts\activate.bat
   ```

8. Install dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

9. Start the API:

   ```powershell
   python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

10. Open the API documentation in your browser: http://127.0.0.1:8000/docs

Keep this terminal running while testing.

## Test the API

In the Swagger page (`/docs`):

1. Expand **POST /predict**.
2. Click **Try it out**.
3. Paste this sample JSON:

   ```json
   {
     "Glucose": 120,
     "BloodPressure": 70,
     "Insulin": 80,
     "BMI": 28.5,
     "DiabetesPedigreeFunction": 0.5,
     "Age": 35
   }
   ```

4. Click **Execute**. The response includes the predicted class and model probability.

Also test:
- `GET /` - confirms the API is running
- `GET /health` - returns `{"status":"ok"}`

## Open the HTML interface

Keep the API terminal running. In VS Code, right-click `index.html` and choose **Open with Live Server** if the Live Server extension is installed. Otherwise open `index.html` in a browser. The page sends requests to `http://127.0.0.1:8000/predict`.

## Push to GitHub

Create a new empty repository on GitHub named `Fast-API`. Do not add a README, license, or `.gitignore` on GitHub because this folder already contains them.

In the VS Code terminal, run these commands one at a time:

```powershell
git init
git add .
git commit -m "Add FastAPI diabetes prediction project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Fast-API.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git asks you to sign in, complete the browser sign-in prompt. If `origin` already exists, use:

```powershell
git remote set-url origin https://github.com/YOUR-USERNAME/Fast-API.git
```

## Viva explanation

**What did you build?**  
I built a REST API using FastAPI for a diabetes prediction model. The API loads a trained Logistic Regression model from a pickle file and receives six input values.

**How does it work?**  
The user sends six values to `POST /predict` as JSON. Pydantic validates the input, pandas converts it into a DataFrame in the model's expected feature order, and the model predicts the result. The API returns the predicted label, text result, and probability.

**Why FastAPI?**  
FastAPI makes it easy to create APIs, validates request data using Pydantic, and automatically provides interactive Swagger documentation at `/docs`.

**What is `Mymdoel.pkl`?**  
It is the serialized, already-trained machine-learning model. The API loads it instead of training a new model every time it starts.

**What are the endpoints?**
- `GET /` - welcome/status message
- `GET /health` - health check
- `POST /predict` - returns a prediction

**Important:** This is a classroom demonstration, not a clinically validated diagnostic tool. Do not use its output to make medical decisions.
