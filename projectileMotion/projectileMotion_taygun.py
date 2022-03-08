import numpy as np

import matplotlib.pyplot as plt

# Kendi fonksiyonumu tanimliyorum
def projectileMotion_2D_taygun(v0_m_s, r0_m, tFinal_s):
    g_m_s2 = np.array([0, -9.8])    

    # Firlatma acisini baslangic hizindan bulabilirim. theta= arctan(v0_y/v0_x)
    #! Hep radyan ile calis. Numpy trigonometrik fonksiyonlari radyan icin calisir
    theta_rad = np.arctan2(v0_m_s[0], v0_m_s[1])

    # Baslangic Zamani
    t0_s= 0
    # 0.001 yazmaktansa asagidaki gibi yazabilirsin
    dt_s= 1e-3

    # Kac adim hesaplayacaksin?
    tSteps = int(tFinal_s/ dt_s)

    # Bos bir 2 boyutlu r matrisi olusturalim:
    r_m = np.zeros((tSteps, 2))
    # Bos bir 1 boyutlu zaman matrisi olusturalim
    time_s = np.zeros(tSteps)

    # Baslangic konumunu koyalim
    r_m[0,:] = r0_m
    
    # Baslangic zamani koyalim
    time_s[0] = t0_s

    # for loop'u ile daha kolay olur.
    for it1 in range(1, tSteps): # Baslangic degerlerini 0. idekse koyduk. O yuzden 1. iterasyondan baslasin
        
        time_s[it1] = time_s[it1-1] + dt_s

        # Hizin x bilesenini hesaplamama gerek yok
        #v_x= v0_m_s[0]*np.cos(theta_rad)
        
        # Hizin y bileseni
        v_y= v0_m_s[1]* np.sin(theta_rad)+ g_m_s2[1]* time_s[it1]

        # x ekseninde ne kadar gitti?
        r_m[it1, 0]= r_m[0, 0]+ v0_m_s[0]* np.cos(theta_rad)* time_s[it1]
        
        # y ekseninde ne kadar gitti?
        r_m[it1, 1]= r_m[0, 1]+ v0_m_s[1]* np.sin(theta_rad)* time_s[it1] + 0.5* g_m_s2[1]* time_s[it1]**2

        # Eger yukseklik 0 dan kucukse yerdedir
        if r_m[it1, 1] < 0:
            # Donguden cik
            break
    
    # Plot
    # Biz r_m matrisini istenilenden buyuk olusturmus olabiliriz cunku 
    # cisim yere carptiktan sonra hesaplama bitiyor. Cismin yere carptigindaki indeks it1
    # Bu yuzden grafigi 0'dan it1'e kadar cizdirecegim
    plt.plot(r_m[0:it1,0], r_m[0:it1,1], 'k', label='Projectile Motion %.1f s Time of flight' %time_s[it1])
    plt.xlabel('x ekseni [m]')
    plt.ylabel('y ekseni [m]')
    plt.legend()
    plt.show()

# Yere dussun
projectileMotion_2D_taygun(v0_m_s= np.array([10, 10]), r0_m=np.array([0, 10]), tFinal_s=5)
# Yere dusmesin
projectileMotion_2D_taygun(v0_m_s= np.array([10, 100]), r0_m=np.array([0, 0]), tFinal_s=5)
exit('')