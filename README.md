Spotify Data Analysis Project
Overview

This project is an end-to-end data analysis pipeline using Spotify live data.
We fetch data directly from the Spotify Web API using Python, clean it, analyze trends, and create visual dashboards for insights.

##Workflow (Phases)

Data Collection → Fetch live Spotify data (tracks, artists, playlists) using the Spotipy SDK.

Data Cleaning → Handle missing values, duplicates, and standardize columns.

Exploratory Data Analysis (EDA) → Visualize trends, correlations, and music popularity patterns.

Database Integration → Store cleaned data in MySQL/Postgres.

Visualization → Build dashboards (Power BI/Tableau/Metabase) to present insights.

Project Structure
spotify-data-analysis/
├── data/                # raw & cleaned datasets
├── notebooks/           # Jupyter notebooks (data cleaning, EDA)
├── scripts/             # Python scripts (API fetch, cleaning utils)
├── reports/             # EDA plots & dashboard screenshots
├── sql/                 # SQL dump of cleaned data
├── README.md            # Project documentation
└── requirements.txt     # Dependencies


Python (pandas, numpy, matplotlib, seaborn)

Spotify API (Spotipy SDK)

Jupyter Notebook / VS Code

SQL (MySQL / Postgres)

Visualization Tool (Power BI / Tableau / Metabase)

How to Run

Clone the repo:

git clone https://github.com/<your-username>/spotify-data-analysis.git
cd spotify-data-analysis


Create a virtual environment and install dependencies:

pip install -r requirements.txt


Add your Spotify API credentials (Client ID & Secret).

Run the scripts or notebooks to fetch data and begin analysis.

Example Insights (to be added later)

Top 10 artists by popularity

Distribution of track durations

Energy vs. danceability correlation

Yearly trends in Spotify tracks

Status

Phase 1: Repo setup

Phase 2: Spotify API Data Collection (in progress)

Phase 3: Data Cleaning

Phase 4: EDA

Phase 5: Database + Dashboard