# Çalışma 3 (01.04.2022)

## <span style="color:red">Yapılacaklar</span>.
- [ ] ????

# Çalışma 2 (28.03.2022)
- [ ] Nokta yükün oluşturduğu elektrik alani hesapla.
- [ ] İki nokta yükün oluşturduğu elektrik alanı hesapla.
  
## <span style="color:red">Yapılacaklar</span>.
- [ ] Tek yükün oluşturduğu elektrik alanı çiz.
- [ ] İki yükün oluşturduğu elektrik alan fonksiyonunu yaz.
- [ ] İki yük için elektrik alan vektörünü çiz.
- [ ] Üç veya daha fazla noktasal yükün elektrik alanını çiz.
- [ ] Matrix determinantını al.

## Örnekler
1. [Matplolib'de vektör çizme](https://www.geeksforgeeks.org/quiver-plot-in-matplotlib/)
2. [Matplolib'de alan çizme](https://matplotlib.org/2.0.2/examples/pylab_examples/quiver_demo.html)
4. [Elektrik Alan Çizimi](https://stackoverflow.com/questions/53275867/electric-field-lines)
3. [~~2 ve daha fazla yükün oluşturduğu elektrik alan Çizimi~~](https://scipython.com/blog/visualizing-a-vector-field-with-matplotlib/)


# Çalışma 1 (21.03.2022)
- [x] Visual Studio Code kullanımı
- [x] Git kullanımı
- [x] Bazı kod yazma standartları ve markdown
- [x] Python fonksiyonlar ve classlar
- [x] Hazır kod kullanmadan matris çarpımı
- [x] Projectile-Motion_taygun.py dosyasının adımlara bakmak.

## Naming Convention ve Markdown
1. [Wikipedia-naming-convention](https://en.wikipedia.org/wiki/Naming_convention_(programming)#Python_and_Ruby)
   - *Python and Ruby both recommend UpperCamelCase for class names, CAPITALIZED_WITH_UNDERSCORES for constants, and lowercase_separated_by_underscores for other names.*
2. [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

## Matris Çarpımı
1. [Programiz](https://www.programiz.com/python-programming/examples/multiply-matrix)
```python
# Program to multiply two matrices using nested loops
# 3x3 matrix
X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
# 3x4 matrix
Y = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
# result is 3x4
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
```