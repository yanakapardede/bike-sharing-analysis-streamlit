import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Load Dataset (Membaca file dari root folder repositori)
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")
    df['dteday'] = pd.to_datetime(df['dteday'])
    return df

day_df = load_data()

# --- SIDEBAR (FILTER / WIDGET) ---
st.sidebar.header("Filter Data Pengguna 🚲")

# Filter berdasarkan Rentang Tanggal
min_date = day_df['dteday'].min()
max_date = day_df['dteday'].max()

date_range = st.sidebar.date_input(
    label="Rentang Waktu",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Validasi jumlah nilai date_range untuk mencegah error unpacking
if len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = date_range[0]
    end_date = date_range[0]

# Filter dataframe berdasarkan tanggal
main_df = day_df[(day_df['dteday'] >= pd.to_datetime(start_date)) & 
                 (day_df['dteday'] <= pd.to_datetime(end_date))]

# --- MAIN CONTENT ---
st.title("🚲 Dashboard Analisis Penyewaan Sepeda")
st.markdown("Proyek Analisis Data Dicoding - **Yanaka Sofia Pardede**")
st.markdown("---")

# Metrics / Summary Cards
total_rentals = main_df['cnt'].sum()
total_casual = main_df['casual'].sum()
total_registered = main_df['registered'].sum()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Keseluruhan Penyewaan", value=f"{total_rentals:,}")
with col2:
    st.metric("Total Pengguna Casual", value=f"{total_casual:,}")
with col3:
    st.metric("Total Pengguna Registered", value=f"{total_registered:,}")

st.markdown("---")

# --- VISUALISASI 1: Berdasarkan Musim & Cuaca ---
st.subheader("📊 Perbandingan Penyewaan Berdasarkan Musim dan Kondisi Cuaca")

col_v1, col_v2 = st.columns(2)

with col_v1:
    fig, ax = plt.subplots(figsize=(8, 5))
    season_user = main_df.groupby('season')[['casual', 'registered']].mean().reset_index()
    season_melted = season_user.melt(id_vars='season', value_vars=['casual', 'registered'],
                                     var_name='user_type', value_name='count')
    sns.barplot(x='season', y='count', hue='user_type', data=season_melted, palette='Set2', ax=ax)
    ax.set_title("Rata-rata Penyewaan Berdasarkan Musim")
    ax.set_xlabel("Musim")
    ax.set_ylabel("Rata-rata Penyewaan")
    ax.legend(title="Tipe Pengguna")
    st.pyplot(fig)

with col_v2:
    fig, ax = plt.subplots(figsize=(8, 5))
    weather_user = main_df.groupby('weathersit')[['casual', 'registered']].mean().reset_index()
    weather_melted = weather_user.melt(id_vars='weathersit', value_vars=['casual', 'registered'],
                                       var_name='user_type', value_name='count')
    sns.barplot(x='weathersit', y='count', hue='user_type', data=weather_melted, palette='Paired', ax=ax)
    ax.set_title("Rata-rata Penyewaan Berdasarkan Kondisi Cuaca")
    ax.set_xlabel("Kondisi Cuaca")
    ax.set_ylabel("Rata-rata Penyewaan")
    plt.xticks(rotation=15)
    ax.legend(title="Tipe Pengguna")
    st.pyplot(fig)

st.markdown("---")

# --- VISUALISASI 2: Tren Bulanan ---
st.subheader("📈 Tren Pertumbuhan Total Penyewaan Sepeda per Bulan")

main_df['year_month'] = main_df['dteday'].dt.to_period('M').astype(str)
monthly_trend = main_df.groupby('year_month')['cnt'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))
sns.lineplot(x='year_month', y='cnt', data=monthly_trend, marker='o', color='b', linewidth=2.5, ax=ax)
ax.set_title("Total Tren Penyewaan Bulanan (2011-2012)")
ax.set_xlabel("Bulan-Tahun")
ax.set_ylabel("Total Penyewaan")
plt.xticks(rotation=45)
ax.grid(True)
st.pyplot(fig)

# Caption Footer
st.markdown("---")
st.caption("Copyright © Yanaka Sofia Pardede 2026 - Dicoding Data Science Submission")