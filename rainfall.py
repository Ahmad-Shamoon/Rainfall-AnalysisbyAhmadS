import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("rainfall_pak.csv")

df.columns = df.columns.str.strip()
month_mapping = {
  'January': 1, 'February': 2, 'March': 3, 'April': 4,
    'May': 5, 'June': 6, 'July': 7, 'August': 8,
    'September': 9, 'October': 10, 'November': 11, 'December': 12
}
df['Month'] = df['Month'].replace(month_mapping)

st.sidebar.title('Filter Options')

selected_year = st.sidebar.selectbox("Select Year",df['Year'].unique())
selected_month = st.sidebar.selectbox("Select Month",df['Month'].unique())

filtered_data = df[(df['Year'] == selected_year) & (df['Month'] == selected_month)]

st.title("Rainfall Analysis Pakistan")
st.write(f"Data for Year : {selected_year}, Month: {selected_month}")
st.dataframe(filtered_data)

annual_rainfall = df.groupby('Year')['Rainfall - (MM)'].sum()
plt.figure(figsize=(10,6))
sns.lineplot(x=annual_rainfall.index, y=annual_rainfall.values)
plt.title("Total Annual Rainfall in Pakistan")
plt.xlabel("Year")
plt.ylabel("Total Rainfall (MM)")
st.pyplot(plt)

monthly_rainfall = df[df['Year'] == selected_year].groupby('Month')["Rainfall - (MM)"].sum()
plt.figure(figsize=(10,6))
sns.barplot(x=monthly_rainfall.index, y=monthly_rainfall.values)
plt.title(f"Rainfall in {selected_year} by Month")
plt.xlabel("Month")
plt.ylabel("Total Rainfall (MM)")

st.pyplot(plt)

st.subheader("Correlation Matrix")
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
st.pyplot(plt)