<div align="center">
   <h1>Open Hardware Monitor Dashboard for Raspberry Pi</h1>
   <h3>📊</h3>
   <h3>Check CPU, GPU & RAM usage/temps via dashboard on Raspberry Pi</h3>
   <a href="https://github.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/blob/master/README.md" target="__blank"><img alt="A badge with a label 'Lang 🇬🇧' - a link takes to README file in English" src="https://img.shields.io/badge/Lang-🇬🇧-012169?style=for-the-badge"></a>
   <a href="https://github.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/blob/master/README.pl-pl.md" target="__blank"><img alt="A badge with a label 'Lang 🇵🇱' - a link takes to README file in Polish" src="https://img.shields.io/badge/Lang-🇵🇱-dc143c?style=for-the-badge"></a>
</div><br/>

## ✨ Dashboard Design
![A screenshot of a dashboard design](https://raw.githubusercontent.com/Cezary924/Open-Hardware-Monitor-Dashboard-for-Raspberry-Pi/master/dashboard.png)
- Made to be displayed on a 480x320 3.5" RPi screen.
- Consists of 6 gauges showing different PC parameters:
   - CPU Load [%]
   - CPU Temp [°C]
   - RAM Load [%]
   - VRAM Load [%]
   - GPU Load [%]
   - GPU Temp [°C]

## PC Requirements
- Intel CPU
  > Other brands have not been tested yet.
- NVIDIA GPU
  > Other brands have not been tested yet.
- Installed and started Open Hardware Monitor's Server

## ⚙️ Installation
1. Clone this repo.
2. Install required libraries with this code:
```
pip install -r requirements.txt
```

## 🚀 Configuration & The First Start
1. To start, execute this command in the main directory:
```
python src/main.py
```
2. During the first launch, the script created a *config.ini* file in a *config* directory. Please, edit the file with your data *(server IP, port & )*.
   > At this step, please remember to run the server built into the Open Hardware Monitor app.
3. If the information provided is correct, the script will start successfully and create a dashboard window.
4. Enjoy!
