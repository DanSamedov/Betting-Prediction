# Betting Prediction

This project involves retrieving betting history data from an e-casino API for CS:GO skins, processing the data, and analyzing whether the outcomes are truly random or if the next bet can be predicted. The goal was to automate the process of fetching historical bet data, process it, and then use machine learning techniques to predict the outcomes of future bets. The project showcases skills in data processing, API integration, machine learning, and automation.

## 🚀 Key Features

- 🌐 **API Integration**: Pulls historical betting data from the CS:GO e-casino API.
- 📊 **Data Processing**: Cleans, processes, and organizes the data into a usable format for analysis.
- 🤖 **Machine Learning**: Uses a decision tree classifier model to predict the outcome of future bets based on past betting data.
- 🔄 **Automation**: Automates the process of retrieving, processing, and storing bet data in an Excel file.
- 🎯 **Prediction Analysis**: Compares predicted outcomes with actual crash data to evaluate model performance.

## 🛠 Libraries Used

- **pandas**: Used for data manipulation and processing, handling structured data efficiently. 📊
- **numpy**: Used for numerical operations, especially in binning the target variable for machine learning. 🔢
- **joblib**: Used to save and load the trained model, allowing for easy reuse without retraining. 💾
- **sklearn**: Used for creating and training the decision tree classifier model, as well as evaluating its performance. 🤖
- **openpyxl**: Used for reading and writing data into an Excel file, storing game data for analysis. 📈
- **requests**: Used for making HTTP requests to the CS:GO e-casino API to retrieve betting history data. 🌐
- **tqdm**: Provides a progress bar for better tracking of the process while fetching data. ⏳

## 📜 Project Workflow

1. **Data Retrieval**: The program fetches historical betting data from the CS:GO e-casino API for each game within a specified range. This is done by making HTTP requests to the API and parsing the returned JSON data. 🔄

2. **Data Processing**: The relevant data, including bet results (`crashedAt`), total bank amount, number of users, and number of items in each game, is extracted and processed. The data is then stored in an Excel file using the `openpyxl` library for future analysis. 📊

3. **Feature Engineering**: The data is preprocessed and prepared for machine learning. This includes converting certain variables into numerical features (e.g., binning the target variable `crashedAt` to classify game outcomes as success or failure). ⚙️

4. **Model Training**: A Decision Tree Classifier from `sklearn` is used to train a model based on the processed data. The model attempts to predict whether the next bet will be a win or loss based on past bet outcomes and features such as total bank, number of users, and number of items. 🤖

5. **Prediction and Evaluation**: The trained model makes predictions on new game data, and the predicted outcomes are compared to the actual results. The accuracy of the model is evaluated to determine if there is any pattern in the data that can be reliably predicted. 📈

6. **Model Persistence**: The trained model is saved using `joblib`, allowing it to be easily loaded and reused in future predictions without retraining. 💾
