
# Zadanie 1
- ##  A
Te osoby są dla siebie rodzeństwem.
- ##  B
Te osoby wnuczkami o różnych rodzicach  tej samej babci/dziadka .
-  ##  C
Te osoby są dziadkami jakiegoś wnuczka, nie są jednak małżeństwem.
-  ##  D
X jest pasierbem/pasierbicą Y.
- ##  E
Jest to rodzeństwo przyrodnie. Mają jednego wspólnego rodzica.
- ##  F
X jest szwagrem/szwagierką dla Y
- ##  G
X jest dzieckiem dziadka/babci Y oraz ojca/matki Y

# Zadanie 1.2
# A
```
osoba(a).
osoba(b).
osoba(y).
osoba(x).

rodzic(a,y).
rodzic(a,x).
rodzic(b,y).
rodzic(b,x).


dziecko(X,Y) :-
    rodzic(Y,X).

rodzenstwo_rodzone(X,Y) :-
    rodzic(A,X),
    rodzic(A,Y),
    rodzic(B,X),
    rodzic(B,Y),
    X \= Y,
    A \= B.
```
# B
```
rodzic(a,b).
rodzic(a,c).
rodzic(b,y).
rodzic(c,x).

dziecko(X,Y) :-
    rodzic(Y,X).

dziadek(X,Y) :-
    rodzic(X,A),
    dziecko(Y,A).
    
wnuk(X,Y) :-
    dziadek(Y,X).

wnuki_tego_samego_dziadka(X,Y) :-
    wnuk(X,A),
    wnuk(Y,A).


```
# C
```
rodzic(x,b).
rodzic(y,c).
rodzic(b,z).
rodzic(c,z).

dziecko(X,Y) :-
    rodzic(Y,X).

dziadek(X,Y) :-
    rodzic(X,A),
    dziecko(Y,A).
    
wnuk(X,Y) :-
    dziadek(Y,X).

ma_wspolnego_wnuka(X,Y) :-
    wnuk(A,X),
    wnuk(A,Y).
```
# D
```
rodzic(y,a).
rodzic(b,a).
rodzic(b,x).



rodzenstwo_przyrodnie(X,Y):-
    rodzic(A,X),
    rodzic(A,Y),
    not((rodzic(B,X), rodzic(B,Y), B \= A)),
    X \= Y.

macocha_lub_ojczym(X,Y) :-
    rodzic(X,A),
    rodzenstwo_przyrodnie(A,Y),
    not(rodzic(X,Y)).
 ```
# E
```
rodzic(a,x).
rodzic(a,y).
rodzic(b,x).
rodzic(c,y).


dziecko(X,Y) :-
    rodzic(Y,X).

rodzenstwo_przyrodnie(X,Y) :-
    rodzic(C,X),
    rodzic(C,Y),
    X \= Y.
```
 # F
 ```
 rodzic(a,y).
rodzic(a,b).
rodzic(b,z).
rodzic(x,z).


rodzenstwo_przyrodnie(X,Y) :-
    rodzic(C,X),
    rodzic(C,Y),
    X \= Y.

malzonek(X,Y) :-
    dziecko(A,X),
	dziecko(A,Y).

szwagier(X,Y) :-
    rodzenstwo_przyrodnie(Y,A),
    malzonek(X,A).
```
# G
```

```
