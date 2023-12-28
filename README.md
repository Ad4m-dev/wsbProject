## Instalacja Selenium:

`pip install -U selenium`

## Instalacja chromedriver:
1. W ustawieniach chrome sprawdzić, jaką mamy wersję przeglądarki (taką samą wersję wybierzemy, instalując chromedriver)
2. Przejść na stonę: https://googlechromelabs.github.io/chrome-for-testing/
3. Pobrać wersję adekwatną dla swojej przeglądarki
4. Wypakować chromedriver z archiwum
5. Przenieść go do PATH do katalogu `/usr/bin`

## Instalacja PyCharm
1. Pobrać najnowszą wersję PyCharm Community Edition ze strony: https://www.jetbrains.com/pycharm/download/other.html
2. Wypakować PyCharm-2023.2.5.tar.gz do pustego katalogu za pomocą komendy: `tar -xzf PyCharm-2023.2.5.tar.gz`
3. Z podkatalogu `bin` uruchomić `pycharm.sh`

## Instalacja pytest:
`pip install -U pytest`

Domyślnie pytest może zainstalować się w katalogu `/home/username/.local/bin`.
Jeżeli ta ścieżka nie jest dodana do `PATH` należy ją dodać zgodnie z poniższą instrukcją.

### Dodawanie ścieżki do PATH:
1. Przejść do bashrc: `sudo nano .bashrc`
2. Wkleić eksport (podmienić username na swojego użytkownika): `export PATH="/home/username/.local/bin:$PATH"`
3. Zapisać zmiany
4. Dla pewności, że wszytko działa poprawnie zrestartować system
5. Zweryfikować wprowadzone zmiany: `echo $PATH`
## Generowanie raportów z testów w html:
### Instalacja pytest-html
`pip install pytest-html`
### Generowanie raportów
`pytest --html=reports/report.html`

## Weryfikacja bibliotek
Używając pycharm upewnić się, że poniższe biblioteki zostały zainstalowane:
(File → Settings → Python Interpreter)
- pytest
- pytest-html
- pytest-metadata
- selenium
