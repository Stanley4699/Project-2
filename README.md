#  Nutrition Paradox: A Global View on Obesity and Malnutrition

This project explores the global trends and disparities in **obesity** and **malnutrition** using public health data from the [World Health Organization (WHO) API](https://ghoapi.azureedge.net/). Through interactive visualizations, we highlight the coexistence of overnutrition and undernutrition across countries, genders, age groups, and regions.

---

## Project Objectives

- Analyze WHO data on obesity and malnutrition among adults and children.
- Understand trends by **country**, **region**, **gender**, **age group**, and **year**.
- Create an interactive **Streamlit dashboard** to visualize and compare global patterns.
- Support public health insights through data-driven visual storytelling.

---

##  Data Sources

We use the following WHO API endpoints:

| Indicator | Description | API |
|----------|-------------|-----|
| Obesity (Adults) | BMI ≥ 30 | [`/NCD_BMI_30C`](https://ghoapi.azureedge.net/api/NCD_BMI_30C) |
| Obesity (Children) | BMI-for-age > +2 SD | [`/NCD_BMI_PLUS2C`](https://ghoapi.azureedge.net/api/NCD_BMI_PLUS2C) |
| Malnutrition (Adults) | BMI < 18 | [`/NCD_BMI_18C`](https://ghoapi.azureedge.net/api/NCD_BMI_18C) |
| Malnutrition (Children) | BMI-for-age < -2 SD | [`/NCD_BMI_MINUS2C`](https://ghoapi.azureedge.net/api/NCD_BMI_MINUS2C) |

---

## 🛠️ Tech Stack

- **Python** (Data processing & API interaction)
- **Pandas** (Data cleaning & manipulation)
- **PyCountry** (Country name standardization)
- **SQLite / MySQL** (Database storage)
- **Streamlit** (Interactive dashboard)
- **Matplotlib / Plotly** (Visualizations)


 Fetch and clean data from WHO API
 Normalize country codes and merge datasets
 Build interactive dashboard
 Add geospatial visualizations (choropleth maps)
 Deploy app via Streamlit Cloud or Heroku
