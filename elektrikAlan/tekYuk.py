import numpy as np
import matplotlib.pyplot as plt

# Elektrik alanin buyuklugunu ve yonunu donduren bir fonksiyon olustur
def elektrikAlan_NoktaKaynak_N_C(xKaynak_m, yKaynak_m, kaynakYukunIsareti, x_m, y_m):
    # Yukun isareti -1 veya +1 olmali
    if kaynakYukunIsareti != -1 and kaynakYukunIsareti != 1:
        exit("\nProgram sonlandirildi... \n\n !! yukunIsareti -1 veya +1 olmali !!")

    # Nokta yukun uzerindeki elektrik alan hesaplanamaz
    if xKaynak_m == x_m and yKaynak_m == y_m:
        exit("\nProgram sonlandirildi... \n\n !! Nokta yukun uzerindeki elektrik alan hesaplanamaz. !!")

    # Coulomb sabiti (k katsayisi)
    k_Nm2_C2  = 8.99e+9
    # Yuk birimi, Bitim Yuk 1*coulomb [C]
    coulomb = 1.6e-19

    # Fonksiyon elektrik alanin buyuklugunu dondurecek.
    elektrikAlanBuyuklugu_N_C = k_Nm2_C2 * coulomb / (((x_m- xKaynak_m) + (y_m- yKaynak_m))**2)
    
    #! Yonu 
    # Tek yuk oldugu icin her zaman merkeze dogru yani r sapka yonunde olacak
    # \vec{r} = x cos(theta) i + y sin(theta) j
    # \hat{r} = cos(theta) i + sin(theta) j
    # theta = arctan(y/x)
    aci_rad = np.arctan2(y_m- yKaynak_m, x_m- xKaynak_m)
    # Kartezyen Birim Vektorler
    x_sapka = 1 
    y_sapka = 1
    # \hat{r} = cos(theta) i + sin(theta) j
    # Elektrik alanin yonu yukun isaretine bagli
    r_sapka = kaynakYukunIsareti* (np.cos(aci_rad) * x_sapka + np.sin(aci_rad) * y_sapka)

    # Elektrik alanin x ve y koordinatlaridaki buyuklugunu ve yonunu veren
    # bir array olusturalim.
    elektrikAlanVec_N_C = np.array([elektrikAlanBuyuklugu_N_C, r_sapka])

    # return np.array([elektrikAlanBuyuklugu_N_C2, r_sapka])
    return elektrikAlanVec_N_C

xKaynak_m = 0; yKaynak_m = 0
kaynakYukunIsareti= 2

print("Kaynak Noktasi [m]: ( x , y ) = (", xKaynak_m, ",", yKaynak_m, ")")
print("Yukun isareti     : ", kaynakYukunIsareti)
print('-----------------------------------------------------')
print("Elektrik Alanin Olculdugu Nokta (x,y) [m]: || Elektrik Alanin Buyuklugu [N/C] || Yonu [\hat{r}]:")

for it_x in range(1, 5): # range(1, 10)
    for it_y in range(0, 5):
        temp = elektrikAlan_NoktaKaynak_N_C(xKaynak_m, yKaynak_m, kaynakYukunIsareti, it_x, it_y)
        print('(%.2f, %.2f) ' %(it_x, it_y),'|| %1.2E ' % temp[0], '|| %1.2E ' % temp[1] )