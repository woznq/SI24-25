
# Zadanie 1

Stałe indywiduowe to:

-   Markus
-   Cezar

Predykaty to:

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

b) Jeżeli Markus próbował dokonać zamachu na Cezara to nie mógł być wobec niego lojalny bo byłoby to sprzeczne z 7 predykatem.

c) w CNF
1.  Człowiek(Markus)
2.  Pompejańczyk(Markus)
3.  ¬Pompejańczyk(x) ∨ Rzymianin(x)
4.  Władca(Cezar)
5.  ¬Rzymianin(x) ∨ Lojalny(x, Cezar) ∨ Nienawidzi(x, Cezar)
6.  Lojalny(x, f(x)) dla pewnej funkcji f
7.  ¬Człowiek(x) ∨ ¬Władca(y) ∨ Lojalny(x, y) ∨ PróbowałZamachu(x, y)
8.  PróbowałZamachu(Markus, Cezar)

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



1.  ∀y(Pożywienie(y) → Lubi(Jan, y))
2.  Pożywienie(Jabłka)
3.  Pożywienie(Kurczak)
4.  ∀x ∀y((Je(x, y) ∧ Żyje(x)) → Pożywienie(y))
5.  Je(Adam, Orzeszki) ∧ Żyje(Adam)
6.  ∀y(Je(Adam, y) → Je(Basia, y))

b) CNF

1.  ¬Pożywienie(y) ∨ Lubi(Jan, y)
2.  Pożywienie(Jabłka)
3.  Pożywienie(Kurczak)
4.  ¬Je(x, y) ∨ ¬Żyje(x) ∨ Pożywienie(y)
5.  Je(Adam, Orzeszki) ∧ Żyje(Adam)
6.  ¬Je(Adam, y) ∨ Je(Basia, y)

c)
Trzeba dodać założenie, że orzeszki są pożywieniem, a wiedząc że Jan lubi każde pożywienie dowiedziemy, że lubi też orzeszki.

Teraz, korzystając z metody rezolucji, możemy udowodnić, że Jan lubi orzeszki. Rozważmy klauzulę 1 i 7. Możemy zastosować rezolucję, podstawiając y = Orzeszki, co daje nam Lubi(Jan, Orzeszki).

d)
Skoro Basia je wszystko to, co Adam to wiedząc, że Adam je orzeszki możemy stwierdzić na podstawie klauzuli 6, że Basia także je orzeszki.

# Zadanie 3
Markus nie żyje, jeżeli mamy rok 2021. Możemy to wykazać z dwóch predykatów. 
1.  UrodziłSię(Markus, 40)
2.  Zniszczone(Pompeje, 79)
3.  Wybuch(Wezuwiusz, 79)
4.  ∀x((Człowiek(x) ∧ Zniszczone(Pompeje, 79) ∧ Wybuch(Wezuwiusz, 79)) → ¬Żyje(x, 79))
5.  MaksymalnyWiek(150)
6.  ∀x((Człowiek(x) ∧ UrodziłSię(x, y)) → ¬Żyje(x, y+150))

Jeden wynika z faktu, że nie przeżył wybuchu Wezuwiusza, ponieważ erupcja zabiła wszystkich w 79. Drugi z faktu, że żaden człowiek nie żył dłużej niż 150 lat, a Markus urodził się w 40.