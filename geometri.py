import math

# İki nokta arasındaki mesafe
def mesafe_hesapla(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Bir noktanın bir doğruya olan dik uzaklık
# Doğru denklemi: Ax + By + C = 0 formatı
def dik_uzaklik_hesapla(x0, y0, A, B, C):
    pay = abs(A * x0 + B * y0 + C)
    payda = math.sqrt(A**2 + B**2)
    return pay / payda
def alan_hesapla(koordinatlar):
    """
    Gauss (Köşe Koordinatları) yöntemiyle çokgenin alanını hesaplar.
    koordinatlar: [(x1, y1), (x2, y2), ...] şeklinde bir liste olmalı.
    """
    n = len(koordinatlar)
    alan = 0.0
    for i in range(n):
        j = (i + 1) % n
        alan += koordinatlar[i][0] * koordinatlar[j][1]
        alan -= koordinatlar[j][0] * koordinatlar[i][1]
    return abs(alan) / 2.0