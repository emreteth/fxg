ort = float(input("Ortalamınızı Giriniz : "))
print("ortalamanız ",ort)

if ort >= 85:
       print("Takdir Aldınız")
else:
       if ort >= 70:
           print("Teşekkür Aldınız")
       else:
           if ort >= 50:
               print("Okulu Geçtiniz")
           else:
               print("Okulda Kaldınız")
