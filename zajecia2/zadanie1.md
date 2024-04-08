
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
rodzic(a,x).
rodzic(b,x).
rodzic(a,z).
rodzic(b,y).
rodzic(z,y).


dziadek(X,Y) :-
    rodzic(X,A),
    dziecko(Y,A).
    


dziwna_relacja(X,Y) :-
    rodzic(A,Y),
    rodzic(A,X),
    rodzic(B,X),
    dziadek(B,Y),
    A \= B,
    X \= Y.
```
# Zad 2
```
mezczyzna(jan).
mezczyzna(henryk).
mezczyzna(slawek).
mezczyzna(konrad).
mezczyzna(antoni).
mezczyzna(jakub).
mezczyzna(dawid).
mezczyzna(marcin).

osoba(jan).
osoba(henryk).
osoba(slawek).
osoba(konrad).
osoba(antoni).
osoba(jakub).
osoba(krystyna).
osoba(katarzyna).
osoba(iwona).
osoba(wiktoria).
osoba(zofia).
osoba(jozefa).
osoba(dawid).
osoba(marcin).
osoba(anna).
osoba(lena).



rodzic(zofia,jan).
rodzic(antoni,henryk).
rodzic(henryk,slawek).
rodzic(henryk,iwona).
rodzic(jozefa,slawek).
rodzic(jozefa,iwona).
rodzic(jan,katarzyna).
rodzic(jan,konrad).
rodzic(konrad,lena).
rodzic(anna,lena).
rodzic(krystyna,katarzyna).
rodzic(krystyna,konrad).
rodzic(katarzyna,jakub).
rodzic(katarzyna,wiktoria).
rodzic(slawek,jakub).
rodzic(slawek,wiktoria).
rodzic(dawid,marcin).
rodzic(katarzyna,marcin).



kobieta(X) :-
    osoba(X),
    \+ mezczyzna(X).
    


ojciec(X,Y) :-
    mezczyzna(X),
    rodzic(X,Y),
    osoba(X),
    osoba(Y).


matka(X,Y) :-
    kobieta(X),
    rodzic(X,Y),
	osoba(X),
    osoba(Y).
 

corka(X,Y) :-
    kobieta(X),
    rodzic(Y,X),
    osoba(X),
    osoba(Y).



brat_rodzony(X,Y) :-
    mezczyzna(X),
    rodzic(A,X),
    rodzic(A,Y),
    rodzic(B,X),
    rodzic(B,Y),
    osoba(X),
    osoba(Y),
    osoba(A),
    osoba(B),
    A \= B,
    X \= Y.


brat_przyrodni(X, Y) :-
    mezczyzna(X),
    rodzic(A, X),   
    rodzic(A, Y),   
    rodzic(B, X),   
    rodzic(C, Y),   
    osoba(X),      
    osoba(Y),      
    osoba(A),      
    osoba(B),      
    osoba(C),      
    A \= B,        
    A \= C,
    B \= C,
    X \= Y.

 



kuzyn(X,Y) :-
    mezczyzna(X),
    rodzic(A,X),
    rodzic(B,Y),
    rodzic(C,A),
    rodzic(C,B),
    A \= B,
    X \= Y,
    osoba(X),      
    osoba(Y),      
    osoba(A),      
    osoba(B),      
    osoba(C),      
    A \= C.  


dziadek_od_strony_ojca(X,Y):-
    mezczyzna(X),
    mezczyzna(A),
    rodzic(X,A),
    rodzic(A,Y),
    osoba(X),
    osoba(Y),
    osoba(A),
    X \= Y.
    

dziadek_od_strony_matki(X,Y):-
    mezczyzna(X),
    kobieta(A),
    rodzic(X,A),
    rodzic(A,Y),
    osoba(X),
    osoba(Y),
	osoba(A).
    

dziadek(X,Y):-
    mezczyzna(X),
    rodzic(X,A),
    rodzic(A,Y),
    osoba(A),
    osoba(Y),
    osoba(X).
    
    

babcia(X,Y):-
    kobieta(X),
    rodzic(X,A),
    rodzic(A,Y),
    osoba(A),
    osoba(Y),
    osoba(X).
    

wnuczka(X,Y):-
    kobieta(X),
    (dziadek(Y,X);
    babcia(Y,X)),
    osoba(Y),
    osoba(X).
    

przodek_do2pokolenia_wstecz(X,Y) :-
    osoba(X),
    osoba(Y),
    (babcia(X,Y);
    dziadek(X,Y);
    ojciec(X,Y);
    matka(X,Y)),
    X \= Y.

    


przodek_do3pokolenia_wstecz(X,Y) :-
    osoba(X),
    osoba(Y),
    (przodek_do2pokolenia_wstecz(X,A),
    (ojciec(A,Y);
    matka(A,Y));
    ojciec(X,Y);
    matka(X,Y)),
    X \= Y.
```
