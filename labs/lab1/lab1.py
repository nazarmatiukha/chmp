import math as m


def equal(x1, x2, X1, X2):
   dif1 = abs(x1-X1)
   dif2 = abs(x2-X2)
   err1 = round(abs(dif1/x1), 5)
   err2 = round(abs(dif2/x2), 5)
   print (f"Граничні відносні похибки: \nx1: {dif1}\nx2: {dif2}\nГраничні відносні похибки:\nx1: {err1}\nx2: {err2}")
   if err1 > err2:
       print("Друга рівність точніше")
   else:
       print("Перша рівність точніше")


if __name__ == '__main__':
   x1 = 62
   x2 = 7/22
   x1_1 = round(m.sqrt(x1), 2)
   x2_2 = round(x2, 3)
   X1 = round(m.sqrt(x1), 5)
   X2 = round(x2, 6)
   equal (x1_1, x2_2, X1, X2)

