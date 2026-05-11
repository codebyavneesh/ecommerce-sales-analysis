# 🎬 Netflix Data Analysis Project using Python

This project is based on Netflix dataset analysis using Python.  
The main goal of this project is to perform data cleaning, data analysis, and data visualization on Netflix movies and TV shows data.

---

# 📌 Project Overview

In this project, I analyzed Netflix content data and created different visualizations to understand:

- Movies vs TV Shows distribution
- Content rating distribution
- Movie duration analysis
- Release year trends
- Top countries producing Netflix content
- Comparison of Movies and TV Shows released over years

---

# 🛠️ Technologies & Libraries Used

- Python
- Pandas
- Matplotlib

---

# 📂 Dataset Used

Dataset: `netflix_titles.csv`

The dataset contains information about:
- Movies
- TV Shows
- Directors
- Cast
- Countries
- Ratings
- Duration
- Release Year

---

# 🧹 Data Cleaning Performed

The following preprocessing steps were performed:

- Filled missing values in:
  - Director
  - Cast
  - Country
  - Rating
- Removed rows with missing:
  - Date Added
  - Duration
- Converted movie duration into integer values for analysis

---

# 📊 Visualizations Created

## 1️⃣ Movies vs TV Shows Bar Chart
Shows the number of Movies and TV Shows available on Netflix.

## 2️⃣ Content Rating Pie Chart
Displays the percentage distribution of content ratings.

## 3️⃣ Movie Duration Histogram
Analyzes the distribution of movie durations.

## 4️⃣ Release Year Scatter Plot
Shows the relationship between release year and number of shows.

## 5️⃣ Top 10 Countries by Content
Displays countries with the highest Netflix content production.

## 6️⃣ Movies vs TV Shows Per Year
Compares yearly release trends for Movies and TV Shows.

---

# 📁 Generated Output Files

The project generates the following visualization images:

- movies_VS_tvshows.png
- content_rating.png
- movies_duration.png
- releaseYear_vs_Scatter.png
- top10_counties.png
- movies_tv_shows_comparison.png

---

# ▶️ How to Run the Project

## Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Step 2: Open Project Folder

```bash
cd netflix-data-analysis
```

## Step 3: Create Virtual Environment

```bash
python -m venv venv
```

## Step 4: Activate Environment

### Windows

```bash
venv\Scripts\activate
```

## Step 5: Install Required Libraries

```bash
pip install pandas matplotlib
```

## Step 6: Run the Project

```bash
python main.py
```

---

# 🚀 Future Improvements

- Add Seaborn visualizations
- Add interactive dashboards
- Perform advanced EDA
- Add genre-based analysis
- Add SQL integration
- Build Streamlit dashboard

---

# 📸 Project Screenshots

(Add your generated graphs/screenshots here)

---

# 👨‍💻 Author

Avneesh Yadav

---

# ⭐ If you like this project, give it a star on GitHub!