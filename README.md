# **Simularea și Analiza Strategiilor în Teoria Jocurilor**

## **Descriere**
Acest proiect explorează concepte fundamentale din **teoria jocurilor** prin implementarea și testarea a două jocuri clasice: **Dilema Prizonierului** și **Stag Hunt**. Aceste simulări inițiale au scopul de a introduce și demonstra dinamica strategiilor de cooperare și competiție. Pe baza acestor rezultate, următorul pas va fi dezvoltarea unui **mediu de testare mai avansat** pentru a analiza în detaliu strategiile într-un joc economic mai complex – **Licitația Primului Preț**.

## **Simulări efectuate**
Până în acest moment, am realizat **3 rulări** pentru fiecare joc, fiecare constând în **20 de runde**. Aceste teste inițiale oferă o bază solidă pentru investigarea ulterioară a strategiilor în **jocuri bazate pe decizii**. 

📂 **Rezultatele complete ale simulărilor pot fi consultate aici:**  
<details>
<summary>📄 Simulari Dilema Prizonierului</summary>
<br>
Scorul reprezinta anii de inchisoare (bigger is worse)

1. **Always Cooperate**<br>
Când joacă împotriva unei strategii identice (Always Cooperate), scorurile sunt egale și maximizate pentru ambele părți.<br>
Împotriva Always Betray, este complet exploatat și obține un scor de 60-0 în defavoarea sa.<br>
Împotriva unei strategii aleatorii, este din nou exploatat, dar nu la fel de sever, datorită rundelor ocazionale de cooperare ale adversarului.<br>
Împotriva Tit-for-Tat, scorurile sunt din nou egale și maximizate, deoarece ambele strategii cooperează în fiecare rundă.<br>
2. **Always Betray**<br>
Împotriva propriei sale strategii, obține un scor intermediar (40-40), ceea ce arată că trădarea reciprocă duce la un echilibru slab.<br>
Împotriva Always Cooperate, câștigă decisiv (60-0), ceea ce arată că poate exploata complet strategiile naive.<br>
Împotriva unei strategii aleatorii, performanța este mediocră, deoarece adversarul cooperează și trădează fără un model clar.<br>
Împotriva Tit-for-Tat, pierde grav (0-60) deoarece Tit-for-Tat începe cooperând, dar pedepsește imediat orice trădare.<br>
3. **Random Strategy**<br>
Împotriva unei alte strategii aleatorii, rezultatele sunt destul de echilibrate (31-31).<br>
Împotriva Always Cooperate, o exploatează dar nu în mod extrem, deoarece ocazional cooperează și permite adversarului să câștige câteva puncte.<br>
Împotriva Always Betray, este exploatat într-o măsură moderată.<br>
Împotriva Tit-for-Tat, pierde în majoritatea cazurilor, deoarece Tit-for-Tat reacționează la trădările sale și menține un avantaj constant.<br>
4. **Tit-for-Tat**<br>
Performanță excelentă în fața Always Cooperate, deoarece maximizează scorurile pentru ambele părți.<br>
Învinge Always Betray cu un scor zdrobitor (60-0), arătând că pedepsirea trădării constante funcționează bine.<br>
Împotriva unei strategii aleatorii, câștigă în majoritatea cazurilor, deoarece reacționează eficient la trădări.<br>
Împotriva propriei sale strategii, are un rezultat optim (20-20), deoarece ambele părți cooperează mereu.<br>
<br>

🔎 **Concluzie**:
Tit-for-Tat pare să fie una dintre cele mai robuste strategii, reușind să se apere împotriva exploatării și să obțină scoruri maxime împotriva strategiilor prietenoase.<br>
Always Cooperate este o strategie slabă în medii competitive, fiind ușor exploatată.<br>
Always Betray este bună împotriva strategiilor naive, dar pierde categoric împotriva celor care răspund la trădări.<br>
Strategia aleatorie nu are o performanță clară și depinde mult de șansa fiecărei runde.<br>

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
<br>
🔎 Concluzie:
În Stag Hunt, jucătorii care aleg constant "stag" pot obține scoruri ridicate, dar cei care aleg "hare" în mod egoist pot câștiga avantaj dacă partenerul cooperează prea mult.
</details>

## 📌 Resurse  
- [Graf cod Dilema Prizonierului](https://app.code2flow.com/vj1Gfgn6v1yG)  