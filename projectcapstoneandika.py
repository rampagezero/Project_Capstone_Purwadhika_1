id_buku=['A001','A002','A003','A004','A005']
judul_buku=['Akuntansi Pengantar 1','Aplikasi Klinis Induk Ovulasi & Stimulasi Ovarium','Aplikasi Praktis Asuhan Keperawatan Keluarga','A-Z Psikologi : Berbagai kumpulan topik Psikologi','Bangsa gagal ; Mencari identitas kebangsaan']
pengarang=['Supardi','Samsulhadi','Komang Ayu Heni','Zainul Anwar','Nasruddin Anshoriy']
penerbit=['Gava Media','Sagung Seto','Sagung Seto','Andi Offset','LKiS']
tahun=['2009','2013','2012','2012','2008']
def tampilandaftar(x=id_buku,y=judul_buku,z=pengarang,a=penerbit,b=tahun,ind=None):
    print("id_buku\t| Judul_Buku\t\t\t\t\t\t|Pengarang\t\t|Penerbit\t|Tahun")
    if ind!=None:
        k=ind+1
        j=k-1
    else:
        k=len(x)
        j=0
    for i in range(j,k):
        if 43<len(y[i])<45:
            print("%s\t| %s\t\t|%s\t|%s\t|%s"%(x[i],y[i],z[i],a[i],b[i]))          
        elif 40<len(y[i])<44:
            print("%s\t| %s\t\t|%s\t|%s\t\t|%s"%(x[i],y[i],z[i],a[i],b[i]))         
        elif len(y[i])>43:
            print("%s\t| %s\t|%s\t\t|%s\t|%s"%(x[i],y[i],z[i],a[i],b[i]))              
        else:
            print("%s\t| %s\t\t\t\t\t|%s\t\t|%s\t|%s"%(x[i],y[i],z[i],a[i],b[i]))
def daftar_buku():
    while True:
        print('=========================Selamat datang di fitur daftar buku Perpustakaan Purwadhika=========================\n 1. Tampilkan Seluruh Data\n 2. Tampilkan berdasarkan primary \n 3. Kembali ke menu awal')
        j=int(input('Masukan nomor pilihan tampilan:'))
        if len(id_buku)!=0 or len(judul_buku)!=0 or len(penerbit)!=0 or len(pengarang)!=0 or len(tahun)!=0:
                if j==1:
                    tampilandaftar()  
                if j==2:
                        k=input('Masukan primary key:')
                        if k in id_buku:
                            ind=id_buku.index(k)
                            tampilandaftar(ind=ind)
                        else: print('=========================Tidak ada data')
                if j==3:
                    menuawal()
        else: print('=========================Tidak ada data')

def tambah_buku():
    while True:
        print('=========================Selamat datang di fitur daftar buku Perpustakaan Purwadhika=========================\n 1. Menambahkan Data \n 2. Kembali ke menu awal')
        x=int(input('Masukan Nomor Opsi:'))
        if x==1:
            i=input('Masukan id_buku :')
            if i not in id_buku:
                j=input('Masukan judul buku:')
                k=input('Masukan informasi nama pengarang:')
                l=input('Masukan informasi penerbit:')
                m=input('Masukan infromasi tahun penerbitan:')
                print('Apakah ingin menyimpan data? 1. Ya 2. Tidak')
                z=int(input('Masukan opsi :'))
                if z==1:
                    id_buku.append(i)
                    judul_buku.append(j)
                    pengarang.append(k)
                    penerbit.append(l)
                    tahun.append(m)
                    print('=========================Data Tersimpan !')
                    tambah_buku()
            else:
                print('=========================id buku tersedia silahkan coba lagi!')
        else: menuawal()
def update_data():
    while True:    
        print('=========================Selamat datang di fitur Update Data Perpustakaan Purwadhika=========================\n 1. Update Data \n 2. Kembali ke menu awal')
        i=int(input('Masukan Opsi:'))
        if i==1:
            j=input('masukan id buku yang ingin di update :')
            if j in id_buku:
                ind=id_buku.index(j)
                tampilandaftar(ind=ind)
                k=int(input('Lanjut Update ? 1. Ya 2. Tidak:'))
                if k==1:
                    l=input('Masukan judul buku:')
                    m=input('Masukan informasi nama pengarang:')
                    n=input('Masukan informasi penerbit:')
                    o=input('Masukan infromasi tahun penerbitan:')
                    p=int(input('Apakah ingin menupdate data? 1. Ya 2. Tidak'))
                    if p==1:
                        judul_buku[ind]=l
                        pengarang[ind]=m
                        penerbit[ind]=n
                        tahun[ind]=o
                        print('=========================Data Terupdate')
                        update_data()
            else:print("=========================Data yang anda cari tidak ada")
        else: menuawal()
def delete(k):
    id_buku.remove(id_buku[k])
    judul_buku.remove(judul_buku[k])
    pengarang.remove(pengarang[k])
    penerbit.remove(penerbit[k])
    tahun.remove(tahun[k])
def delete_data():
    print('=========================Selamat datang di fitur Delete Data Perpustakaan Purwadhika=========================\n 1. Delete Data \n 2. Kembali ke menu awal')
    i=int(input('Masukan opsi:'))
    if i==1:
        tampilandaftar()
        j=input('Masukan id buku yang ingin di hapus :')
        if j in id_buku:
            k=id_buku.index(j)
            l=int(input('Yakin ingin menghapus data? 1.Ya 2.Tidak :'))
            if l==1:
                delete(k)
                tampilandaftar()
                print('=========================data terhapus !')
                delete_data()
    else: menuawal()

import string
import random
def randomticket():
    s=10
    ran=''.join(random.choices(string.ascii_uppercase + string.digits,k=s))
    return ran
lp_id=[]
lp_judul=[]
lp_pengarang=[]
lp_penerbit=[]
lp_tahun=[]
l={}
def borrow():    
    print('=========================Selamat datang di fitur peminjaman Purwadhika Silahkan memilih========================= \n 1. Menambahkan Cart\n 2.  Menu Awal')
    z=int(input('Masukan angka opsi:'))
    if z==1:
        o=int(input('Pengguna baru ? 1.Ya 2. Tidak:'))
        if o==1:
            def borrow_menu():
                global lp_id
                global lp_judul
                global lp_penerbit
                global lp_pengarang
                global lp_tahun
                tampilandaftar()
                j=input('Masukan id buku yang ingin dipinjam:')
                k=id_buku.index(j)
                lp_id.append(id_buku[k])
                lp_judul.append(judul_buku[k])
                lp_pengarang.append(pengarang[k])
                lp_penerbit.append(penerbit[k])
                lp_tahun.append(tahun[k])
                print('Cart Peminjaman:')
                tampilandaftar(lp_id,lp_judul,lp_pengarang,lp_penerbit,lp_tahun)
                delete(k)
                m=int(input('Apakah ada tambahan cart: 1.Ya,2.Tidak :'))
                if m==1:
                    borrow_menu()       
                else:
                    ran=randomticket()
                    l[ran]=[lp_id,lp_judul,lp_pengarang,lp_penerbit,lp_tahun]
                    lp_id=[]
                    lp_judul=[]
                    lp_penerbit=[]
                    lp_pengarang=[]
                    lp_tahun=[]
                    print('=========================Ticket anda adalah %s silahkan dibawa untuk proses pengembalian, Terima Kasih !'%(ran))
                    borrow()
            borrow_menu() 
        else:
            j=input('Masukan nomor tiket anda:')
            if j in l.keys():
                def borrow_lama():
                    tampilandaftar()
                    print('List Pinjaman')
                    tampilandaftar(l[j][0],l[j][1],l[j][2],l[j][3],l[j][4])
                    k=input('Masukan id buku yang ingin dipinjam:')
                    k=id_buku.index(k)
                    l[j][0].append(id_buku[k])
                    l[j][1].append(judul_buku[k])
                    l[j][2].append(pengarang[k])
                    l[j][3].append(penerbit[k])
                    l[j][4].append(tahun[k])
                    tampilandaftar(l[j][0],l[j][1],l[j][2],l[j][3],l[j][4])
                    delete(k) 
                    m=int(input('Apakah ada tambahan cart: 1.Ya,2.Tidak :'))
                    if m==1:
                        borrow_lama()   
                    else:
                        print('=========================Terima kasih, sampai jumpa lagi !')
                        menuawal()
                borrow_lama()
            else:
                print('=========================Maaf ticket tidak tersedia')             
    else:
        menuawal()

def returnbook():
    print('=========================Selamat datang di menu pengembalian buku perpustakaan Purwadhika=========================')
    j=input('Silahkan masukan nomor tiket peminjaman anda:')
    if j in l.keys():
        tampilandaftar(l[j][0],l[j][1],l[j][2],l[j][3],l[j][4])
        m=int(input('Apakah anda yakin ingin mengembalikannya? 1.Ya 2. Tidak'))
        if m==1:
            for i in range(0,len(l[j][0])):
                id_buku.append(l[j][0][i])
                judul_buku.append(l[j][1][i])
                pengarang.append(l[j][2][i])
                penerbit.append(l[j][3][i])
                tahun.append(l[j][4][i])
            print('=========================Buku anda sudah ditambahkan pada sistem, Terima Kasih ')
            menuawal()
    else:print('=========================Maaf nomor tiket anda tidak tersedia, silahakn coba lagi!')


def menuawal():
    print('\t=========================Selamat Datang di Pusat Database Perpustakaan Purwadhika========================= \n\tSilahkan pilih salah satu fitur yang ingin digunakan:\n\t\t 1. Daftar Buku\n\t\t 2. Tambahkan Daftar Buku\n\t\t 3. Koreksi Daftar Buku\n\t\t 4. Hapus Daftar Buku\n\t\t 5. Peminjaman Buku\n\t\t 6. Pengembalian Buku ')
    j=int(input('Masukan angka opsi :'))
    if j==1:
        daftar_buku()
    if j==2:
        tambah_buku()
    if j==3:
        update_data()
    if j==4:
        delete_data()
    if j==5:
        borrow()
    if j==6:
        returnbook()
    else:
        print('Inputan tidak tersedia silahkan coba lagi')


while True:
    menuawal()


            






                
                
                
