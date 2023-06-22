#!/usr/bin/env python
# coding: utf-8

# In[6]:


import requests #Untuk mengirim permintaan HTTP ke halaman web.
from bs4 import BeautifulSoup # Untuk mem-parsing dokumen HTML. 
import csv #Untuk membaca dan menulis data dalam format CSV


web_url = 'https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D=redmi&search_source=omnisearch_keyword&source=navbar' #Menyimpan link web bukalapak yang akan discraping ke variabel.

data = []  #List kosong untuk menyimpan data produk.

for page in range(1, 6): #Melakukan perulangan untuk scraping pada halaman 1 hingga 5.
    url = web_url + str(page)  #Untuk menggabungkan URL dasar dengan nomor halaman yang sedang diproses.
    req = requests.get(url)  #Untuk mengirim permintaan HTTP GET ke URL bukalapak.
    soup = BeautifulSoup(req.text, 'html.parser')  #Untuk membuat objek dari konten HTML yang diperoleh dari respons HTTP menggunakan parser HTML bawaan.
    product_items = soup.find_all('div', {'class': 'bl-product-card'})  #Untuk mencari semua elemen dalam halaman web yang memiliki tag <div> dan class 'bl-product-card'.
    
    for item in product_items: #Untuk melakukan perulangan untuk mengambil masing-masing item yang telah dicari di variabel product_items.
        
        #Mengambil nama, alamat, harga, dan rating produk dari elemen-elemen yang ditemukan.
        name = item.find('a', {'class': 'bl-link'}).text.strip() #Digunakan untuk mengekstrak teks dari elemen <a> yang memiliki class 'bl-link'.
        address = item.find('span', {'class': 'mr-4 bl-product-card__location bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1'}).text.strip() #Untuk mengekstrak teks dari elemen <span> yang memiliki class yang spesifik dalam suatu elemen item.
        price = item.find('p', {'class': 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1'}).text.strip() #Untuk mengekstrak teks dari elemen <p> yang memiliki class yang spesifik dalam suatu elemen item.
        data.append([name, address, price])  #Menyimpan data dalam list data.
        
csv_file = 'data_hpredmi.csv'  #Deklarasikan nama CSV untuk menyimpan data.

with open(csv_file, 'w', newline='', encoding='utf-8') as file: #Membuka file csv_file dengan mode write ('w') untuk menulis data.
    writer = csv.writer(file) #Untuk membuat objek penulis (writer) dari modul CSV yang akan digunakan untuk menulis data ke dalam file CSV.
    writer.writerow(['Name', 'Address', 'Price'])  #Untuk menulis baris header ke dalam file CSV.
    writer.writerows(data)  #Untuk menulis multiple baris data ke dalam file CSV yang sedang dibuka.

    
    
import pandas as pd #Untuk mengimpor modul Pandas ke dalam script.
import matplotlib.pyplot as plt #Untuk mengimpor modul Matplotlib ke dalam script.

#Untuk membaca file CSV dengan nama "data_hpredmi.csv".
data = pd.read_csv("data_hpredmi.csv")

#Untuk membuat sebuah figur baru dalam visualisasi dengan ukuran 12x7 inci.
plt.figure(figsize=(12, 7))

#Untuk menghitung jumlah kemunculan tiap nilai dalam kolom 'Address'.
plt.hist(data['Address'])

#Menambahkan judul.
plt.title("Histogram HP Redmi Berdasarkan Alamat")

#Menyimpan Histogram dalam format JPG dengan nama file 'Histogram_hpredmi.jpg'.
plt.savefig('Histogram_hpredmi.jpg', dpi=300, bbox_inches='tight')

#Menampilkan hasil Histogram.
plt.show()



import pandas as pd #Untuk mengimpor modul Pandas ke dalam script.
import matplotlib.pyplot as plt #Untuk mengimpor modul Matplotlib ke dalam script.

#Untuk membaca file CSV dengan nama "data_hpredmi.csv".
data = pd.read_csv("data_hpredmi.csv")

#Untuk membuat sebuah figur baru dalam visualisasi dengan ukuran 12x7 inci.
plt.figure(figsize=(12, 7))

data['Address'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)  #Membuat pie chart dengan persen.
plt.ylabel('') #Menghapus label sumbu Y.

#Menambahkan judul.
plt.title("Pie Chart HP Redmi Berdasarkan Alamat")

#Menyimpan Pie Chart dalam format JPG dengan nama file 'PieChart_hpredmi.jpg'.
plt.savefig('PieChart_hpredmi.jpg', dpi=300, bbox_inches='tight')

#Menampilkan hasil Pie Chart.
plt.show()



# In[ ]:




