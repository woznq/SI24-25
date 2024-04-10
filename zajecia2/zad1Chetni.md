

# Zadanie 1

Stałe indywiduowe to:

-   Markus
-   Cezar

Predykaty to:
```
-   Człowiek(x): x jest człowiekiem
-   Pompejańczyk(x): x jest pompejańczykiem
-   Rzymianin(x): x jest Rzymianinem
-   Władca(x): x jest władcą
-   Lojalny(x, y): x jest lojalny wobec y
-   Nienawidzi(x, y): x nienawidzi y
-   PróbowałZamachu(x, y): x próbował dokonać zamachu na y
1.  Człowiek(Markus)
2.  Pompejańczyk(Markus)
3.  ∀x(Pompejańczyk(x) → Rzymianin(x))
4.  Władca(Cezar)
5.  ∀x(Rzymianin(x) → (Lojalny(x, Cezar) ∨ Nienawidzi(x, Cezar)))
6.  ∀x ∃y(Lojalny(x, y))
7.  ∀x ∀y((Człowiek(x) ∧ Władca(y) ∧ ¬Lojalny(x, y)) → PróbowałZamachu(x, y))
8.  PróbowałZamachu(Markus, Cezar)
```
b) 
```¬Rzymianin(Markus) ∨ Lojalny(Markus, Cezar) ∨ Nienawidzi(Markus, Cezar)```
Mamy jednak``` Pompejczyk(Markus)``` co jest równe z ```Rzymianin(Markus)```
```PróbowałZamachu(Markus, Cezar)``` tylko kiedy ```¬Lojalny(Marcus,Cezar)```
Mamy więc sprzeczność, co oznacza, że nasze założenie było błędne. Zatem Markus nie mógł być lojalny wobec Cezara.

c) w CNF
```
1.  Człowiek(Markus)
2.  Pompejańczyk(Markus)
3.  ¬Pompejańczyk(x1) ∨ Rzymianin(x1)
4.  Władca(Cezar)
5.  ¬Rzymianin(x1) ∨ Lojalny(x1, Cezar) ∨ Nienawidzi(x1, Cezar)
6.  Lojalny(x3, f(x3)) dla pewnej funkcji f
7.  ¬Człowiek(x1) ∨ ¬Władca(x2) ∨ ¬Lojalny(x1, x2) ∨ ¬PróbowałZamachu(x1, x2)
8.  PróbowałZamachu(Markus, Cezar)
```
d)
Stawiamy hipotezę ```¬Nienawidzi(Marcus,Cezar)```
Zgodnie z rezolucją negujemy hipotezę``` ¬Nienawidzi(Marcus,Cezar)```
Z punktu 2 wiemy, że ```Pompejańczyk(Markus)```, więc musi być``` Rzymianin(Markus).```
Z punktu 5 mamy ```∀x(Rzymianin(x) → (Lojalny(x, Cezar) ∨ Nienawidzi(x, Cezar)))```,
 więc
  ```Rzymianin(Markus) → (Lojalny(Markus, Cezar) ∨ Nienawidzi(Markus, Cezar)). ```
Ponieważ
 ```Rzymianin(Markus)```, to musi być``` Lojalny(Markus, Cezar) ∨ Nienawidzi(Markus, Cezar)```.
 Ale założyliśmy, że ```¬Nienawidzi(Markus, Cezar)```, więc musi być ```Lojalny(Markus, Cezar).```
Z punktu 7 mamy
``` ∀x ∀y((Człowiek(x) ∧ Władca(y) ∧ ¬Lojalny(x, y)) → PróbowałZamachu(x, y))```, 
więc
``` (Człowiek(Markus) ∧ Władca(Cezar) ∧ ¬Lojalny(Markus, Cezar)) → PróbowałZamachu(Markus, Cezar).```
 Z punktu 1 wiemy, że``` Człowiek(Markus)```, 
 z punktu 4, że ```Władca(Cezar)```, 
 a z punktu 8, że ```PróbowałZamachu(Markus, Cezar)```.
 Ale wiemy, że``` Lojalny(Markus, Cezar)```, więc mamy sprzeczność.
 Zatem nasze założenie, że ```¬Nienawidzi(Markus, Cezar)```, jest błędne.

# Zadanie 2
Stałe indywiduowe to:

-   Jan
-   Jabłka
-   Kurczak
-   Orzeszki
-   Adam
-   Basia

Predykaty to:
-   Lubi(x, y): x lubi y
-   Pożywienie(x): x jest pożywieniem
-   Je(x, y): x je y
-   Żyje(x): x żyje


```
1.  ∀x: (Pożywienie(x1) → Lubi(Jan, x1))
2.  Pożywienie(Jabłka)
3.  Pożywienie(Kurczak)
4.  ∀x : ∀y  :  Je(x1, x2) ∧ Żyje(x1) → Pożywienie(x2)
5.  Je(Adam, Orzeszki) ∧ Żyje(Adam)
6.  ∀x : Je(Adam, x2) → Je(Basia, x2)
```
b) CNF
```
1.  ¬Pożywienie(x1) ∨ Lubi(Jan, x1)
2.  Pożywienie(Jabłka)
3.  Pożywienie(Kurczak)
4.  ¬Je(x1, x2) ∨ ¬Żyje(x1) ∨ Pożywienie(x2)
5.  Je(Adam, Orzeszki)
6.  Żyje(Adam)
7.  ¬Je(Adam, x3) ∨ Je(Basia, x3)
8.  ¬lubi(Jan, orzeszki)
```
c)
Trzeba dodać założenie, że orzeszki są pożywieniem, a wiedząc że Jan lubi każde pożywienie dowiedziemy, że lubi też orzeszki.
```¬Pożywienie(Jabłka) ∨ Lubi(Jan,Jabłka) + Pożywienie(Jabłka) = Lubi(Jan,Jabłka)```
```¬Je(Adam,Orzeszki) ∨ ¬Żyje(Adam) ∨ Pożywienie(Orzeszki) + Żyje(Adam) = Je(Adam,Orzeszki)``` = ```Pozywienie(orzeszki)```
```¬Pożywienie(Orzeszki) ∨ Lubi(Jan,Orzeszki) + ¬Lubi(Jan,Orzeszki) + pożywienie(orzeszki) /= sprzeczność koniec dowodu```


d)
```¬Je(Adam, x) ∨ Je(Basia, x)```
```Je(Adam, Orzeszki)``` więc x = orzeszki
Jeżeli dodamy ```Pożywnienie(Orzeszki) to ¬Je(Basia, x) ∨ ¬Żyje(Basia) ∨ Pożywienie(x)``` z tego stwierdzenia dowiedziemy, że Basia je orzeszki.


# Zadanie 3
Markus nie żyje, jeżeli mamy rok 2021. Możemy to wykazać z dwóch predykatów. 
```
1.  mężczyzna(Marcus)
2.  Pompejczyk(Marcus)
3.  Urodzony(Markus, 40)
4.  ∀x : mężczyzna(x) → śmiertelnik(x)
5.  ∀x : Pompejczyk(x) → umarł(x,79)
6.  Wybuch(Wezuwiusz, 79)
7.  ∀x ∀t ∀t śmiertelnik(x) ∧ Urodzony(x,t1) ∧ diff(t2-t1,150) → umarł(x,t2)
8.  rok = 2021
9.  ∀x : ∀t: zyje(x,t) → ¬umarł(x,t)
10. ∀x : ∀t: umarł(x,t) → ¬zyje(x,t)
11. ∀x : ∀t1 : ∀t2 : umarł(x,t1) ∧ diff(t2,t1) → martwy(x,t2)
```
Sposoby korzystają z reguł powyżej.
Sposób 1:
```
¬zyje(Marcus,teraz)
umarł(Marcus,teraz)
umarł(Marcus,t1) ∧ diff(teraz,t1)
Pompejczyk(Marcus) ∧ diff(teraz,79)
diff(teraz,79)
diff(2021,79)
```
Sposób 2:
```
¬zyje(Marcus,teraz)
umarł(Marcus,teraz)
śmiertelnik(Marcus) ∧ Urodzony(Marcus,t1) ∧ diff(teraz-t1,150)
mężczyzna(Marcus) ∧ Urodzony(Marcus,t1) ∧ diff(teraz-t1,150)
Urodzony(Marcus,t1) ∧ diff(teraz-t1,150)
diff(teraz-40,150)
diff(1981,150)
```
