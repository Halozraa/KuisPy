import random

baik = 100
jahat = 100
rand = random.randint(1, 10)

def quest1():
    global baik, jahat
    while True:
        try:
            print("Bagaimana sikap Anda terhadap orang-orang yang memiliki pandangan atau keyakinan yang berbeda dengan Anda?")
            pilihan = input("Apakah Anda membencinya [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")

def quest2():
    global baik, jahat
    while True:
        try:
            print("Bagaimana Anda merespons kesalahan atau kegagalan, baik yang Anda lakukan sendiri atau yang dilakukan oleh orang lain?")
            pilihan = input("Apakah Anda akan melimpahkannya ke orang lain? [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")
def quest3():
    global baik, jahat
    while True:
        try:
            print("Bagaimana Anda merespons ketidakadilan atau perlakuan yang tidak adil terhadap orang lain?")
            pilihan = input("Apakah akan diam saja [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")
def quest4():
    global baik, jahat
    while True:
        try:
            print("Bagaimana Anda memperlakukan mereka yang berada dalam posisi kekuasaan atau otoritas, terutama jika Anda memiliki kekuatan atau keunggulan atas mereka?")
            pilihan = input("Akan membullynya [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")
def quest5():
    global baik, jahat
    while True:
        try:
            print("Bagaimana Anda memperlakukan mereka yang berada dalam posisi kekuasaan atau otoritas, terutama jika Anda memiliki kekuatan atau keunggulan atas mereka?")
            pilihan = input("tidak membantunya kan? [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")
def quest6():
    global baik, jahat
    while True:
        try:
            print("Apakah Anda cenderung melakukan tindakan yang merugikan atau menyakiti orang lain demi keuntungan pribadi atau kepuasan?")
            pilihan = input("Ya sering sekali? [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")
def quest7():
    global baik, jahat
    while True:
        try:
            print("Apakah Anda sering memaafkan kesalahan atau tindakan buruk orang lain, atau cenderung membalas dendam?")
            pilihan = input("Tidak pernah [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")

def quest8():
    global baik, jahat
    while True:
        try:
            print("Apakah Anda cenderung mengutamakan kepentingan individu atau kepentingan bersama dalam pengambilan keputusan?")
            pilihan = input("Ya, karena hidup itu sendiri-sendiri [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")

def quest9():
    global baik, jahat
    while True:
        try:
            print("Apakah Anda sering menunjukkan empati dan simpati terhadap orang-orang yang sedang menderita atau mengalami kesulitan?")
            pilihan = input("Tidak pernah [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")

def quest10():
    global baik, jahat
    while True:
        try:
            print("Bagaimana Anda berperilaku dalam hubungan interpersonal, terutama dalam hal komunikasi, kerjasama, dan konflik?")
            pilihan = input("lebih sering kerja sendiri ? [y/n]: ")
            if pilihan == 'y':
                baik -= rand
            elif pilihan == 'n':
                jahat -= rand
            else:
                print("Masukkan Jawaban yang benar")
                continue
            break
        except ValueError:
            print("Masukkan jawaban yang benar: ")


def main():
    global baik, jahat
    hasil = f"\nPoin kebaikan {baik}\nPoin Kejahatan {jahat}"
    if baik < jahat:
        print(f"{hasil}\n\nAnda adalah orang yang jahat sekali")
    elif baik > jahat:
        print(f"{hasil}\n\nAnda adalah orang baik dan perjuanganmu akan selalu dikenang")
    elif baik == jahat:
        print("Kamu kadang bisa menjadi orang jahat dan baik, sungguh keseimbangan")
    else:
        print("Error")

if __name__ == "__main__":
    quest1()
    quest2()
    quest3()
    quest4()
    quest5()
    quest6()
    quest7()
    quest8()
    quest9()
    quest10()
    main()
