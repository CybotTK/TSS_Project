# **Simularea și Analiza Strategiilor în Teoria Jocurilor**

## **Descriere**
Acest proiect explorează concepte fundamentale din **teoria jocurilor** prin implementarea și testarea a două jocuri clasice: **Dilema Prizonierului** și **Stag Hunt**. Aceste simulări inițiale au scopul de a introduce și demonstra dinamica strategiilor de cooperare și competiție. Pe baza acestor rezultate, următorul pas va fi dezvoltarea unui **mediu de testare mai avansat** pentru a analiza în detaliu strategiile într-un joc economic mai complex – **Licitația Primului Preț**.

## **Simulări efectuate**
Până în acest moment, am realizat **3 rulări** pentru fiecare joc, fiecare constând în **20 de runde**. Aceste teste inițiale oferă o bază solidă pentru investigarea ulterioară a strategiilor în **jocuri bazate pe decizii**. 

📂 **Rezultatele complete ale simulărilor pot fi consultate aici:**  
<details>
<summary>📄 Simulari Dilema Prizonierului</summary>
<br>
**Simulare 1** <br>
Inițial, ambele părți cooperează, acumulând scoruri egale.
Pe parcurs, trădarea începe să apară, alternând între jucători.
Spre final, ambele părți încep să trădeze constant.
Rezultat: P1 - 29, P2 - 26 → Ușoară victorie pentru P1. <br>
**Simulare 2** <br>
Jucătorii alternează între cooperare și trădare, dar revin la un echilibru.
În ultimele runde, cooperarea este predominantă.
Rezultat: P1 - 30, P2 - 30 → Egalitate. <br>
**Simulare 3 **<br> 
Inițial, predomină trădarea, dar apoi se stabilește un echilibru.
În ultimele runde, trădarea devine mai frecventă.
Rezultat: P1 - 34, P2 - 31 → P1 câștigă. <br>
<br>
📌 **Observație**: Jucătorii care încep să trădeze mai devreme pot câștiga pe termen scurt, dar cooperarea duce adesea la rezultate mai echilibrate.
</details>
<details>
<summary>📄 Simulari Stag Hunt</summary>
<br>
**Simulare 1** <br>
P1 adoptă diverse strategii (random, selfish, cooperative).
P2 menține strategii mai consistente.
La final, P2 obține un scor mai mare prin alegerea constantă a iepurelui.
Rezultat: P1 - 40, P2 - 44 → P2 câștigă. <br>
**Simulare 2** <br>
Ambii jucători utilizează strategii tit-for-tat și cooperative.
Scorurile rămân egale până spre final.
În ultimele runde, P2 devine mai egoist și câștigă avantaj.
Rezultat: P1 - 52, P2 - 56 → P2 câștigă. <br>
**Simulare 3** <br> 
Inițial, strategii aleatorii și egoiste afectează scorurile.
P1 trece la strategii mai cooperative, dar P2 profită de asta.
Spre final, echilibrul revine, dar P2 păstrează un avantaj.
Rezultat: P1 - 30, P2 - 38 → P2 câștigă. <br>
<br>
📌 **Observație**: Jucătorii care rămân constanți și profită de cooperarea celorlalți tind să aibă scoruri mai mari.
</details>

🔎 Concluzie generală:

În Dilema Prizonierului, cooperarea susținută poate aduce rezultate mai bune pe termen lung, dar trădarea ocazională oferă avantaje punctuale.
În Stag Hunt, jucătorii care aleg constant "stag" pot obține scoruri ridicate, dar cei care aleg "hare" în mod egoist pot câștiga avantaj dacă partenerul cooperează prea mult.

## 📌 Resurse  
- [Graf cod Dilema Prizonierului](https://app.code2flow.com/vj1Gfgn6v1yG)  