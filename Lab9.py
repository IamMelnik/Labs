print('В первой строке введите время вcтречи. Во второй строке время прибытия')

h1, m1 = map(int, input().split(sep=':'))
h2, m2 = map(int, input().split(sep=':'))

# Перевод в минуты
m1 = 60 * h1 + m1
m2 = 60 * h2 + m2

m1 = m1 + 15

if m1 > 1439:
    m1 -= 1440

if m2 > m1:
    print('Встреча не состоится')
else:
    print('Встреча состоится')
