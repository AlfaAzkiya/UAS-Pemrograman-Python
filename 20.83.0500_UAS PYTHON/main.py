import requests
import json
import pymysql


con = pymysql.connect(
    host = 'localhost', user = 'root',
    passwd = '', db = 'db_akademik_0500')

cursor = con.cursor()

if(cursor):
    print("Koneksi", "Koneksi Berhasil")
else:
    print("Koneksi", "Koneksi Gagal")
                
def write_api():
    t1={}
    r = requests.get('https://api.abcfdab.cfd/students')
    package_json = r.json()
    
    for i in package_json['data']:
        val = (i['id'],i['nim'],i['nama'],i['jk'],i['jurusan'],i['alamat'])
        cursor.execute("""INSERT INTO tbl_students_0500
            (id,nim,nama,jk,jurusan,alamat)
            VALUES (%s, %s, %s, %s, %s, %s)""", val)
        con.commit()
        


def show_data():
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tbl_students_0500')
    myresult = cursor.fetchall()
    for x in myresult:
        print(x)

def show_data_limit():
    limit = int(input('masukan limit>'))
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tbl_students_0500')
    myresult = cursor.fetchmany(limit)
    for x in myresult:
        print(x)

def show_data_nim():
    x = "'"
    nim = input('masukan nim>')
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tbl_students_0500 WHERE nim = ' + x + nim + x)
    myresult = cursor.fetchone()
    print(myresult)

#hapus pagar pada write_api untuk membuat database
#tambah pagar pada write api untuk melhat database
#write_api()
    
while True:
    print("1. Tampilkan semua data")
    print("2. Tampilkan data berdasarkan limit")
    print("3. Cari data berdasarkan NIM")
    print("0. keluar")

    value = int(input("Pilih menu> "))

    if value == 1:
        show_data()


    elif value == 2:
        show_data_limit()


    elif value == 3:
        show_data_nim()

    elif value == 0:
        break

    else:
        print("invalid")


