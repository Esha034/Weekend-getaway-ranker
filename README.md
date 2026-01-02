# Weekend Getaway Ranker 

A data-driven recommendation engine that ranks the best weekend travel destinations in India based on **distance, user ratings, and popularity**. This project demonstrates practical **data engineering, feature engineering, and ranking logic**, and is deployable as an interactive web app using Streamlit.

---
## 🔗 Live Demo
 **Click here:** [Weekend Getaway Ranker ](https://weekend-getaway-ranker-web.streamlit.app/)

##  Features

- Takes a **source city** as input
- Ranks top weekend destinations using:
  - Google review ratings
  - Popularity 
  - Engineered distance proximity 
- Interactive Streamlit web app
- Easily deployable on cloud platforms

---

##  Tech Stack

- Python
- Pandas
- Streamlit

---

##  Project Structure

weekend-getaway-ranker/

│

├── app.py # Streamlit application

├── src/

│ └── ranker.py # Core recommendation logic

├── data/

│ └── Top Indian Places to Visit.csv

├── output/

│ └── sample_output.txt

├── requirements.txt

└── README.md

## Installation

### 1️ Clone the repository


git clone https://github.com/your-username/weekend-getaway-ranker.git

cd weekend-getaway-ranker

### 2️. Create virtual environment

python -m venv venv

### 3️. Activate environment
Windows

venv\Scripts\activate
Linux / Mac

source venv/bin/activate

### 4️. Install dependencies

pip install -r requirements.txt

## Execution (CLI Mode)
Run the ranking algorithm using:

python src/ranker.py
The output will be saved to:

output/sample_output.txt

## Run Streamlit App Locally

streamlit run app.py
Open browser at:

http://localhost:8501

## Recommendation Logic

Since the dataset does not provide geographical distance, a distance proxy is engineered:

| Condition      | Distance Score |
| -------------- | -------------- |
| Same City      | 0.0            |
| Same State     | 1.0            |
| Same Zone      | 0.5            |
| Different Zone | 0.05           |

## Final Ranking Score

Final Score =

+ 0.30 × Popularity Score
  
+ 0.40 × Distance Score

+ 0.30 × Rating Score
  
Weights were tuned empirically to improve weekend travel feasibility.


## Future Improvements
-Add geographical distance using latitude/longitude

-Include travel time and cost

-Add map-based visualization

-User preference-based filtering

👤 Author

Eshani Banik

B.Tech (CSE)





