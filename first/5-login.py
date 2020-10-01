users={"andyka" : "aku123"}
status=""
def menu():
    status = input("Apakah sudah memiliki akun (y/n)except to exit ? ")
    if status == "y":
        lanjut()
    elif status == "n":
        daftar()
    else:
        print("exit")
def lanjut():
    first=0
    last=3
    while first < last:
        login = input("\nUsername: ")
        password = input("Password: ")
        if login in users and users[login] == password:
            print("Login berhasil")
            break
        else:
            print("Gagal login {} kali".format(first+1))
        first+=1
def daftar():
    nama = input("\nMasukkan username: ")
    if nama in users:
        print ("Nama sudah terdaftar")
    else:
        password =input("Masukkan password: ")
        users[nama] = password
        print("Berhasil membuat akun")
        menu()
menu()