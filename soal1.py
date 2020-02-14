# NOMOR 1 : URAI RAJUT KATA

class uraiRajutKata:
    def urai(self,kata):
        hasil = ""
        for row in range(len(kata)):
            for col in range(row+1):
                hasil += kata[col]
                hasil += ""
        hasil += ""
        return hasil
    def rajut(self,hasilKata):
        himpunan_syarat = [1]
        awal = 1
        for i in range(2, len(hasilKata)): 
            awal += i
            himpunan_syarat.append(awal)
        length_kata = himpunan_syarat.index(len(hasilKata)) + 1 
        length_kata *= -1
        kata = hasilKata[length_kata:len(hasilKata)]
        return kata

x = uraiRajutKata()

print(x.urai("Code"))
print(x.urai('Python'))
print(x.urai('Purwadhika'))
print(x.urai('Andicaca'))

print(x.rajut('CCoCodCode'))
print(x.rajut('PPyPytPythPythoPython'))
print(x.rajut('PPuPurPurwPurwaPurwadPurwadhPurwadhiPurwadhikPurwadhika'))
print(x.rajut("AAnAndAndiAndicAndicaAndicacAndicaca"))