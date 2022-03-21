# Çalışma 1 (21.03.2022)
- [ ] Visual Studio Code kullanımı
- [ ] Git kullanımı
- [ ] Bazı kod yazma standartları ve markdown
- [ ] Python fonksiyonlar ve classlar
- [ ] Hazır kod kullanmadan matris çarpımı
- [ ] Projectile-Motion_taygun.py dosyasının adımlara bakmak.

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