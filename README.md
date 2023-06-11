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
Po zaznaczeniu interesujących nas punktów w programie qgis wchodzimy w okno "Wtyczki" --> "Projekt2" --> "Projekt2" powinno nam się otworzyć okno z naszą wtyczką, teraz możemy skorzystać z opcji obliczenia różnicy wysokości lub pola powierzchni w tym celu wystarczy kliknąć na odpowiednio na przyciski "Policz_roznice_wysokosci" lub "Policz_pole" wynik pojawi się w oknie obok. Gdybyśmy jednak zaznaczyli zbyt małą ilość ponktów wyświetli się stosowny komunikat.
# Znane błędy
- funkcja liczenia różnicy wysokości zadziała poprawnie wyłącznie ,gdy kolumny zawierające wartości id.X,Y,Z będą usytuowane w następującej kolejności id,X,Y,Z. w przeciwnym wypadku skrypt będzie pobierał niewłaściwe dane i tego nie udało nam się rozwiązać  
