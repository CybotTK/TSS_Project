# **Simularea și Analiza Strategiilor în Teoria Jocurilor**

## **Descriere**
Acest proiect explorează concepte fundamentale din **teoria jocurilor** prin implementarea și testarea a două jocuri clasice: **Dilema Prizonierului** și **Stag Hunt**. Aceste simulări inițiale au scopul de a introduce și demonstra dinamica strategiilor de cooperare și competiție. Pe baza acestor rezultate, următorul pas va fi dezvoltarea unui **mediu de testare mai avansat** pentru a analiza în detaliu strategiile într-un joc economic mai complex – **Licitația Primului Preț**.

## **Simulări efectuate**
Până în acest moment, am realizat **3 rulări** pentru fiecare joc, fiecare constând în **20 de runde**. Aceste teste inițiale oferă o bază solidă pentru investigarea ulterioară a strategiilor în **jocuri bazate pe decizii**. 

📂 **Rezultatele complete ale simulărilor pot fi consultate aici:**  
<details>
<summary>📄 Simulari Dilema Prizonierului</summary>
<br>
Simulare 1:
Runda 1: P1 - C, P2 - C | Scor: 1, 1
Runda 2: P1 - C, P2 - C | Scor: 2, 2
Runda 3: P1 - C, P2 - C | Scor: 3, 3
Runda 4: P1 - C, P2 - C | Scor: 4, 4
Runda 5: P1 - C, P2 - C | Scor: 5, 5
Runda 6: P1 - C, P2 - C | Scor: 6, 6
Runda 7: P1 - C, P2 - T | Scor: 9, 6
Runda 8: P1 - T, P2 - C | Scor: 9, 9
Runda 9: P1 - C, P2 - C | Scor: 10, 10
Runda 10: P1 - C, P2 - C | Scor: 11, 11
Runda 11: P1 - C, P2 - C | Scor: 12, 12
Runda 12: P1 - C, P2 - T | Scor: 15, 12
Runda 13: P1 - T, P2 - C | Scor: 15, 15
Runda 14: P1 - C, P2 - T | Scor: 18, 15
Runda 15: P1 - T, P2 - C | Scor: 18, 18
Runda 16: P1 - C, P2 - T | Scor: 21, 18
Runda 17: P1 - T, P2 - T | Scor: 23, 20
Runda 18: P1 - T, P2 - T | Scor: 25, 22
Runda 19: P1 - T, P2 - T | Scor: 27, 24
Runda 20: P1 - T, P2 - T | Scor: 29, 26

Scor final: P1 - 29, P2 - 26

Simulare 2:
Runda 1: P1 - C, P2 - T | Scor: 3, 0
Runda 2: P1 - T, P2 - T | Scor: 5, 2
Runda 3: P1 - T, P2 - C | Scor: 5, 5
Runda 4: P1 - C, P2 - T | Scor: 8, 5
Runda 5: P1 - T, P2 - C | Scor: 8, 8
Runda 6: P1 - C, P2 - C | Scor: 9, 9
Runda 7: P1 - C, P2 - T | Scor: 12, 9
Runda 8: P1 - T, P2 - C | Scor: 12, 12
Runda 9: P1 - C, P2 - T | Scor: 15, 12
Runda 10: P1 - T, P2 - C | Scor: 15, 15
Runda 11: P1 - C, P2 - T | Scor: 18, 15
Runda 12: P1 - T, P2 - T | Scor: 20, 17
Runda 13: P1 - T, P2 - T | Scor: 22, 19
Runda 14: P1 - T, P2 - T | Scor: 24, 21
Runda 15: P1 - T, P2 - C | Scor: 24, 24
Runda 16: P1 - C, P2 - T | Scor: 27, 24
Runda 17: P1 - T, P2 - C | Scor: 27, 27
Runda 18: P1 - C, P2 - C | Scor: 28, 28
Runda 19: P1 - C, P2 - C | Scor: 29, 29
Runda 20: P1 - C, P2 - C | Scor: 30, 30

Scor final: P1 - 30, P2 - 30

Simulare 3:
Runda 1: P1 - C, P2 - T | Scor: 3, 0
Runda 2: P1 - T, P2 - T | Scor: 5, 2
Runda 3: P1 - T, P2 - T | Scor: 7, 4
Runda 4: P1 - T, P2 - T | Scor: 9, 6
Runda 5: P1 - T, P2 - T | Scor: 11, 8
Runda 6: P1 - T, P2 - T | Scor: 13, 10
Runda 7: P1 - T, P2 - C | Scor: 13, 13
Runda 8: P1 - C, P2 - C | Scor: 14, 14
Runda 9: P1 - C, P2 - C | Scor: 15, 15
Runda 10: P1 - C, P2 - T | Scor: 18, 15
Runda 11: P1 - T, P2 - T | Scor: 20, 17
Runda 12: P1 - T, P2 - C | Scor: 20, 20
Runda 13: P1 - C, P2 - T | Scor: 23, 20
Runda 14: P1 - T, P2 - T | Scor: 25, 22
Runda 15: P1 - T, P2 - T | Scor: 27, 24
Runda 16: P1 - T, P2 - C | Scor: 27, 27
Runda 17: P1 - C, P2 - C | Scor: 28, 28
Runda 18: P1 - C, P2 - C | Scor: 29, 29
Runda 19: P1 - C, P2 - T | Scor: 32, 29
Runda 20: P1 - T, P2 - T | Scor: 34, 31

Scor final: P1 - 34, P2 - 31
</details>
<details>
<summary>📄 Simulari Stag Hunt</summary>
<br>
Simularea 1:

Round: P1(random -> stag) vs P2(random -> stag) -> Scores: P1(3), P2(3)
Round: P1(random -> hare) vs P2(random -> hare) -> Scores: P1(4), P2(4)
Round: P1(random -> hare) vs P2(random -> hare) -> Scores: P1(5), P2(5)
Round: P1(random -> stag) vs P2(cooperative -> stag) -> Scores: P1(8), P2(8)
Round: P1(tit_for_tat -> stag) vs P2(cooperative -> stag) -> Scores: P1(11), P2(11)
Round: P1(selfish -> hare) vs P2(cooperative -> stag) -> Scores: P1(13), P2(11)
Round: P1(selfish -> hare) vs P2(cooperative -> stag) -> Scores: P1(15), P2(11)
Round: P1(cooperative -> stag) vs P2(cooperative -> stag) -> Scores: P1(18), P2(14)
Round: P1(cooperative -> stag) vs P2(cooperative -> stag) -> Scores: P1(21), P2(17)
Round: P1(cooperative -> stag) vs P2(cooperative -> stag) -> Scores: P1(24), P2(20)
Round: P1(cooperative -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(27), P2(23)
Round: P1(cooperative -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(30), P2(26)
Round: P1(cooperative -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(33), P2(29)
Round: P1(cooperative -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(36), P2(32)
Round: P1(cooperative -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(39), P2(35)
Round: P1(cooperative -> stag) vs P2(selfish -> hare) -> Scores: P1(39), P2(37)
Round: P1(cooperative -> stag) vs P2(selfish -> hare) -> Scores: P1(39), P2(39)
Round: P1(cooperative -> stag) vs P2(selfish -> hare) -> Scores: P1(39), P2(41)
Round: P1(cooperative -> stag) vs P2(selfish -> hare) -> Scores: P1(39), P2(43)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(selfish -> hare) -> Scores: P1(40), P2(44)
Final Score: P1(40), P2(44)

Simularea 2:

Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(3), P2(3)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(6), P2(6)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(9), P2(9)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(12), P2(12)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(15), P2(15)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(18), P2(18)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(21), P2(21)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(24), P2(24)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(27), P2(27)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(30), P2(30)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(33), P2(33)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(36), P2(36)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(39), P2(39)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(42), P2(42)
Round: P1(cooperative -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(45), P2(45)
Round: P1(cooperative -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(48), P2(48)
Round: P1(cooperative -> stag) vs P2(cooperative -> stag) -> Scores: P1(51), P2(51)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(selfish -> hare) -> Scores: P1(51), P2(53)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(selfish -> hare) -> Scores: P1(51), P2(55)
Round: P1(selfish -> hare) vs P2(selfish -> hare) -> Scores: P1(52), P2(56)
Final Score: P1(52), P2(56)

Simularea 3:

Round: P1(selfish -> hare) vs P2(random -> hare) -> Scores: P1(1), P2(1)
Round: P1(random -> stag) vs P2(random -> hare) -> Scores: P1(1), P2(3)
Round: P1(random -> stag) vs P2(random -> hare) -> Scores: P1(1), P2(5)
Round: P1(random -> stag) vs P2(random -> stag) -> Scores: P1(4), P2(8)
Round: P1(tit_for_tat -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(7), P2(11)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat -> stag) -> Scores: P1(10), P2(14)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(selfish -> hare) -> Scores: P1(10), P2(16)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(selfish -> hare) -> Scores: P1(11), P2(17)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(selfish -> hare) -> Scores: P1(12), P2(18)
Round: P1(selfish -> hare) vs P2(selfish -> hare) -> Scores: P1(13), P2(19)
Round: P1(selfish -> hare) vs P2(selfish -> hare) -> Scores: P1(14), P2(20)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(selfish -> hare) -> Scores: P1(14), P2(22)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(selfish -> hare) -> Scores: P1(15), P2(23)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(selfish -> hare) -> Scores: P1(16), P2(24)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(selfish -> hare) -> Scores: P1(16), P2(26)
Round: P1(tit_for_tat_with_forgiveness -> hare) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(18), P2(26)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(21), P2(29)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(24), P2(32)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(27), P2(35)
Round: P1(tit_for_tat_with_forgiveness -> stag) vs P2(tit_for_tat_with_forgiveness -> stag) -> Scores: P1(30), P2(38)
Final Score: P1(30), P2(38)
</details>

## 📌 Resurse  
- [Graf cod Dilema Prizonierului](https://app.code2flow.com/vj1Gfgn6v1yG)  