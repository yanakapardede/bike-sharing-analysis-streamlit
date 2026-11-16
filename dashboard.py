import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='darkgrid')

# ---------------------------------------------------------
# Helper functions untuk menyiapkan DataFrame analisis
# ---------------------------------------------------------
def create_daily_orders_df(df):
    daily_orders_df = df.resample(rule='D', on='dteday').agg({
        'cnt': 'sum'
    }).reset_index()
    return daily_orders_df

def create_season_orders_df(df):
    season_orders_df = df.groupby('season')[['casual', 'registered']].mean().reset_index()
    return season_orders_df

def create_weather_orders_df(df):
    weather_orders_df = df.groupby('weathersit')[['casual', 'registered']].mean().reset_index()
    return weather_orders_df

def create_hourly_orders_df(df):
    hourly_orders_df = df.groupby(['hr', 'workingday'])['cnt'].mean().reset_index()
    hourly_orders_df['workingday'] = hourly_orders_df['workingday'].map({0: 'Libur / Akhir Pekan', 1: 'Hari Kerja'})
    return hourly_orders_df

# ---------------------------------------------------------
# Load Dataset
# ---------------------------------------------------------
# Memuat data yang sudah dikondisikan
day_df = pd.read_csv("dashboard/main_data.csv") if pd.io.common.file_exists("dashboard/main_data.csv") else pd.read_csv("data/day.csv")
hour_df = pd.read_csv("data/hour.csv")

# Preprocessing singkat untuk pemetaan di dashboard
day_df['dteday'] = pd.to_datetime(day_df['dteday'])
hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])

season_mapping = {1: 'Springer', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
weather_mapping = {1: 'Clear/Few Clouds', 2: 'Mist/Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice'}

if day_df['season'].dtype != 'object':
    day_df['season'] = day_df['season'].map(season_mapping)
    day_df['weathersit'] = day_df['weathersit'].map(weather_mapping)

# ---------------------------------------------------------
# Sidebar Filter Tanggal
# ---------------------------------------------------------
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=200)
    
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = day_df[(day_df['dteday'] >= pd.Timestamp(start_date)) & 
                 (day_df['dteday'] <= pd.Timestamp(end_date))]

main_hour_df = hour_df[(hour_df['dteday'] >= pd.Timestamp(start_date)) & 
                       (hour_df['dteday'] <= pd.Timestamp(end_date))]

# Memanggil helper functions
daily_orders_df = create_daily_orders_df(main_df)
season_orders_df = create_season_orders_df(main_df)
weather_orders_df = create_weather_orders_df(main_df)
hourly_orders_df = create_hourly_orders_df(main_hour_df)

# ---------------------------------------------------------
# Main Dashboard Layout
# ---------------------------------------------------------
st.header('Bike Sharing Analytics Dashboard 🚲')

# Metric Cards
col1, col2, col3 = st.columns(3)
with col1:
    total_orders = main_df['cnt'].sum()
    st.metric("Total Penyewaan", value=f"{total_orders:,}")
with col2:
    total_registered = main_df['registered'].sum()
    st.metric("Pengguna Registered", value=f"{total_registered:,}")
with col3:
    total_casual = main_df['casual'].sum()
    st.metric("Pengguna Casual", value=f"{total_casual:,}")

st.markdown("---")

# Visualisasi 1: Pertanyaan 1 (Musim & Cuaca)
st.subheader("Penyewaan Berdasarkan Musim & Cuaca")

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(14, 5))

# Subplot Musim
season_melted = season_orders_df.melt(id_vars='season', value_vars=['casual', 'registered'], 
                                     var_name='user_type', value_name='count')
sns.barplot(x='season', y='count', hue='user_type', data=season_melted, palette='Set2', ax=ax[0])
ax[0].set_title('Rata-rata Penyewaan per Musim', fontsize=12)
ax[0].set_xlabel(None)
ax[0].set_ylabel("Rata-rata Penyewaan")

# Subplot Cuaca
weather_melted = weather_orders_df.melt(id_vars='weathersit', value_vars=['casual', 'registered'], 
                                      var_name='user_type', value_name='count')
sns.barplot(x='weathersit', y='count', hue='user_type', data=weather_melted, palette='Paired', ax=ax[1])
ax[1].set_title('Rata-rata Penyewaan per Kondisi Cuaca', fontsize=12)
ax[1].set_xlabel(None)
ax[1].set_ylabel(None)
ax[1].tick_params(axis='x', rotation=15)

st.pyplot(fig)

# Visualisasi 2: Pertanyaan 2 (Pola Jam Kerja vs Libur)
st.subheader("Pola Penyewaan Sepeda per Jam (Hari Kerja vs Libur)")

fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.lineplot(x='hr', y='cnt', hue='workingday', data=hourly_orders_df, marker='o', linewidth=2.5, ax=ax2)
ax2.set_title('Pola Rata-rata Penyewaan Sepeda per Jam', fontsize=14)
ax2.set_xlabel('Jam dalam Sehari (0 - 23)')
ax2.set_ylabel('Rata-rata Jumlah Penyewaan')
ax2.set_xticks(range(0, 24))
ax2.grid(True)

st.pyplot(fig2)

st.caption('Copyright © Yanaka Sofia Pardede')