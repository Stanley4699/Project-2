import streamlit as st
import pandas as pd
import mysql.connector

st.set_page_config(layout="wide")
st.title("Nutrition Paradox: Obesity & Malnutrition Dashboard")


try:
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='12345',
        database='nutrition'
    )
except Exception as e:
    st.error(f"Could not connect to MySQL: {e}")
    st.stop()


st.header("Overview")
st.markdown("""
This dashboard explores the **double burden of obesity and malnutrition** using WHO data.

Use the filters and tables below to explore and compare different countries, years, and gender groups.
""")


st.header("Explore Data")

years = pd.read_sql("SELECT DISTINCT Year FROM nutrition_data ORDER BY Year DESC", conn)['Year']
regions = pd.read_sql("SELECT DISTINCT Region FROM nutrition_data", conn)['Region']
genders = pd.read_sql("SELECT DISTINCT Gender FROM nutrition_data", conn)['Gender']

year = st.selectbox("Select Year", years, key="explore_year")
region = st.selectbox("Select Region", regions, key="explore_region")
gender = st.selectbox("Select Gender", genders, key="explore_gender")

query = f"""
SELECT CountryCode, Mean_Estimate
FROM nutrition_data
WHERE Year = {year}
AND Region = '{region}'
AND Gender = '{gender}'
ORDER BY Mean_Estimate DESC
LIMIT 10
"""

try:
    df = pd.read_sql(query, conn)
    st.write(f"Query ran: {query}")

    if df.empty:
        st.warning("⚠️ No data found.")
    else:
        st.dataframe(df)
except Exception as e:
    st.error(f"SQL Error: {e}")


st.header("🧠 Explore Analytical Insights")

questions = [
    "1. Obesity by gender in selected year & region",
    "2. Malnutrition by gender in selected country",
    "3. Gender-wise obesity trend in a region",
    "4. Gender with steepest obesity rise over time",
    "5. Lowest malnutrition by gender in latest year",
    "6. Top 10 countries by obesity (year)",
    "7. Average obesity across all regions by year",
    "8. Top 5 countries with highest obesity growth (2000–2022)",
    "9. Top 5 countries with highest malnutrition rate in 2022",
    "10. Obesity trend in a selected country",
    "11. Malnutrition trend in a selected country",
    "12. Compare obesity vs malnutrition in a selected region",
    "13. Year with highest global obesity average",
    "14. Region with highest average obesity in 2022",
    "15. Region with lowest average malnutrition in 2022",
    "16. Top 10 countries with obesity above 30% in 2022",
    "17. Top 10 countries with malnutrition below 5% in 2022",
    "18. Average obesity by gender across all years",
    "19. Country with the steepest decline in malnutrition",
    "20. Region where male obesity increased most since 2000",
    "21. Year-wise gender comparison for malnutrition in a region",
    "22. Correlation between obesity and malnutrition in a region",
    "23. Country with consistent obesity rates over years",
    "24. Top 5 countries where female obesity exceeds male",
    "25. Total number of countries reporting obesity and malnutrition data each year"
    
]

selected_q = st.selectbox("Select a Question", questions, key="insights_question")

year_filter = st.slider("Select Year", 2000, 2022, 2022, key="insights_year")
region_filter = st.selectbox("Select Region", regions)
gender_filter = st.selectbox("Select Gender", ["Male", "Female", "Both"], key="insights_gender")

try:
    if selected_q.startswith("1"):
        query = f"""
        SELECT Gender, AVG(Mean_Estimate) AS AvgObesity
        FROM nutrition_data
        WHERE Year = {year_filter}
        AND Region = '{region_filter}'
        AND IndicatorCode = 'NCD_BMI_30C'
        GROUP BY Gender
        """
    elif selected_q.startswith("2"):
        query = f"""
        SELECT Gender, AVG(Mean_Estimate) AS AvgMalnutrition
        FROM nutrition_data
        WHERE CountryCode = '{country_filter}'
        AND IndicatorCode = 'NUT_MALN'
        GROUP BY Gender
        """
    elif selected_q.startswith("6"):
        query = f"""
        SELECT CountryCode, AVG(Mean_Estimate) AS AvgObesity
        FROM nutrition_data
        WHERE Year = {year_filter}
        AND IndicatorCode = 'NCD_BMI_30C'
        GROUP BY CountryCode
        ORDER BY AvgObesity DESC
        LIMIT 10
        """
    else:
        st.info("Query for this selection is not implemented yet.")
        query = None

    if query:
        df_insights = pd.read_sql(query, conn)
        if df_insights.empty:
            st.warning("⚠️ No data found for selected filters.")
        else:
            st.dataframe(df_insights)

except Exception as e:
    st.error(f"Error running insights query: {e}")

conn.close()
