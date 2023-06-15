# Wtyczka do programu qgis

### Założenia projektu
Celem projektu było utworzenie wtyczki do programu qgis, która będzie liczyła różnicę wysokości między dwoma punktami oraz pole powierzchni minimum trzech punktów.

# Podstawowe funkcje
- liczenie różnicy wysokości dwóch zaznaczonych punktów
- liczenie pola powierzchni minimum trzech zaznaczonych punktów
# Wymagania
system operacyjny Windows 10 lub 11
-program QGIS wersja 3.22
-python 3.9
-biblioteka PyQt5
-biblioteka qgis.utilis
-biblioteka qgis.PyQt
# Interfejs
![image](https://github.com/adamsalanski/Wtyczka/assets/129080884/56ba3703-57d1-4d37-b2ac-3c7a74d2329a)

- 1 - Pole obliczenia różnicy wysokości
- 2 - Pole obliczenia pola powierzchni
- 3 - Pole wyświetlające wyniki
# Jak wybrać punkty?
Należy w programie qgis otworzyć plik z interesującymi nas punktami i zaznaczyć je przy pomocy narzędnia "Zaznacz obiekt"
# Obsługa wtyczki
Po ściągnięciu wszystkich plików do wtyczki należy umieścić je w folderze o nazwie wtyczka_as 

Po zaznaczeniu interesujących nas punktów w programie qgis wchodzimy w okno "Wtyczki" --> "Projekt2" --> "Projekt2" powinno nam się otworzyć okno z naszą wtyczką, teraz możemy skorzystać z opcji obliczenia różnicy wysokości lub pola powierzchni w tym celu wystarczy kliknąć na odpowiednio na przyciski "Policz_roznice_wysokosci" lub "Policz_pole" wynik pojawi się w oknie obok. Gdybyśmy jednak zaznaczyli zbyt małą ilość ponktów wyświetli się stosowny komunikat.
# Przykładowe obliczenie różnicy wysokości:
W celu obliczenia różnicy wysokości możemy skorzystać z pliku "plik_do_obliczenia_roznicy_wysokosci" zamieszczonego w plikach. Wybieramy 2 punkty z warstwy "turbiny" następnie wchodzimy w zakładkę "Wtyczki"-->"Projekt2"-->"Projekt2" i wybieramy opcję Policz_roznice_wysokosci.

Przykładowy wynik:
![image](https://github.com/adamsalanski/Wtyczka/assets/129080884/797827cd-09b5-4f88-b963-fb8a97cd65c4)

# Znane błędy
- funkcja liczenia różnicy wysokości zadziała poprawnie wyłącznie ,gdy wartości wysokości bedą zlokalizowane w 2 kolumnie tabeli atrybutów, w przeciwnym wypadku skrypt będzie pobierał niewłaściwe dane i tego nie udało nam się rozwiązać  
