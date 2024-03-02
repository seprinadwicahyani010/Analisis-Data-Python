import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Memasukkan data tabel
day_df = pd.read_csv('data/day.csv')
hour_df = pd.read_csv('data/hour.csv')

# Menggabungkan kedua tabel
bikesharing_df = day_df.merge(hour_df, on='dteday', how='inner', suffixes=('_day', '_hour'))

# Menampilkan data penyewaan sepeda
avg_workday = bikesharing_df.groupby('workingday_day')['cnt_day'].mean()
avg_weekday = bikesharing_df.groupby('weekday_day')['cnt_day'].mean()

labels_workday = ['Hari Kerja', 'Hari Libur']
labels_weekday = ['Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu', 'Minggu']

st.write("## Rata-rata Penyewaan Sepeda")
st.write("### Rata-rata Penyewaan Sepeda pada Hari Kerja")
st.write(avg_workday)
st.write("### Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu")
st.write(avg_weekday)

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

axes[0].pie(avg_workday, labels=labels_workday, autopct='%1.1f%%', colors=('blue', 'lightblue'))
axes[0].set_title('Rata-rata Penyewaan Sepeda pada Hari Kerja')

axes[1].pie(avg_weekday, labels=labels_weekday, autopct='%1.1f%%', colors=('blue', 'white', 'lightblue', 'darkblue'))
axes[1].set_title('Rata-rata Penyewaan Sepeda pada Hari dalam Seminggu')

st.pyplot(fig)


# Menampilkan data penyewaan sepeda berdasarkan kondisi cuaca
weathersit_labels = {
    1: 'Cerah',
    2: 'Mendung',
    3: 'Hujan'
}

bikesharing_df['weathersit_label'] = bikesharing_df['weathersit_day'].map(weathersit_labels)
avg_weather = bikesharing_df.groupby('weathersit_label')['cnt_day'].mean().reset_index()

st.write("## Rata-rata Penyewaan Sepeda berdasarkan Kondisi Cuaca")
st.write(avg_weather)

plt.figure(figsize=(10, 7))
plt.bar(avg_weather['weathersit_label'], avg_weather['cnt_day'], color='skyblue')

plt.title('Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
plt.xlabel('Kondisi Cuaca')
plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')

plt.xticks(rotation=45)

plt.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(plt)


# Menampilkan data penggunaan sepeda (terdaftar dan tidak terdaftar)
st.write("## Penggunaan Sepeda Terdaftar dan Tidak Terdaftar")

total_terdaftar = bikesharing_df['registered_day'].sum()
total_tidak_terdaftar = bikesharing_df['casual_day'].sum()

st.write("Total sewa sepeda (terdaftar):", total_terdaftar)
st.write("Total sewa sepeda (tidak terdaftar):", total_tidak_terdaftar)

cnt_bikesharing = [bikesharing_df['registered_day'].sum(), bikesharing_df['casual_day'].sum()]

labels = ['Terdaftar', 'Tidak Terdaftar']

plt.figure(figsize=(8, 6))
plt.barh(labels, cnt_bikesharing, color=['blue', 'skyblue'])

plt.title('Total Sewa Sepeda (Terdaftar dan Tidak Terdaftar)')
plt.xlabel('Jumlah')
plt.ylabel('Tipe Sewa Sepeda')

st.pyplot(plt)