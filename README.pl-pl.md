<div align="center">
   <h1>Open Hardware Monitor Dashboard for Raspberry Pi</h1>
   <h3>📊</h3>
   <h3>Sprawdź użycie/temperaturę CPU, GPU i RAMu poprzez dashboard na Raspberry Pi</h3>
   <a href="https://github.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/blob/master/README.md" target="__blank"><img alt="Etykieta z napisem 'Jęz 🇬🇧' - link prowadzi do pliku README w języku angielskim" src="https://img.shields.io/badge/Jęz-🇬🇧-012169?style=for-the-badge"></a>
   <a href="https://github.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/blob/master/README.pl-pl.md" target="__blank"><img alt="Etykieta z napisem 'Jęz 🇵🇱' - link prowadzi do pliku README w języku polskim" src="https://img.shields.io/badge/Jęz-🇵🇱-dc143c?style=for-the-badge"></a>
</div><br/>

## ✨ Dashboard Design
![Zrzut ekranu układu dashboard typu 1](https://raw.githubusercontent.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/master/dashboard1.png)
![Zrzut ekranu układu dashboard typu 2](https://raw.githubusercontent.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/master/dashboard2.png)
- Przeznaczony do wyświetlania na ekranie RPi.
- Składa się z 6 mierników odpowiadających parametrom PC:
   - użycie CPU [%]
   - temperatura CPU [°C]
   - użycie RAM [%]
   - użycie VRAM [%]
   - użycie GPU [%]
   - temperatura GPU [°C]

## 🖥️ Wymaganie sprzętowe
- Procesor Intel
  > Inne marki nie były jeszcze sprawdzane.
- Karta graficzna NVIDIA
  > Inne marki nie były jeszcze sprawdzane.
- Zainstalowany i uruchomiony serwer Open Hardware Monitor
  > PC musi spełniać wszelkie dodatkowe wymagania sprzętowe aplikacji OHM.

## ⚙️ Instalacja
1. Sklonuj to repozytorium.
2. Zainstaluj wymagane biblioteki przy pomocy tego polecenia:
```
pip install -r requirements.txt
```

## 🚀 Konfiguracja & Pierwsze Uruchomienie
   > Skrypt potrzebuje 30s na uruchomienie, cierpliwości!
1. Aby uruchomić skrypt, wykonaj to polecenie będąc w głównym folderze:
```
python src/bot.py
```
2. Podczas pierwszego uruchomienia, skrypt stworzy plik *config.ini* w folderze *config*. Dokonaj edycji tego pliku umieszczając w nim swoje dane *(IP serwera, port, okres między aktualizacjami, typ dashboardu, szer. ekr., wys. ekr., odśw. ekr.)*.
   > W tym miejscu pamiętaj, aby uruchomić serwer wbudowany w aplikację Open Hardware Monitor.
3. Jeśli wprowadzone informacje są prawidłowe, skrypt pomyślnie się uruchomi i stworzy okno zawierające dashboard.
4. Gotowe!
