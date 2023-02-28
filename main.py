"""
Utwórz program do zarządzania bazą szkolną. Istnieje możliwość tworzenia trzech typów
użytkowników (uczeń, nauczyciel, wychowawca) a także zarządzania nimi.

Po uruchomieniu programu można wpisać jedną z następujących komend: utwórz, zarządzaj,
koniec.

Polecenie "utwórz" - Przechodzi do procesu tworzenia użytkowników.
Polecenie "zarządzaj" - Przechodzi do procesu zarządzania użytkownikami.
Polecenie "koniec" - Kończy działanie aplikacji.

Proces tworzenia użytkowników:

Należy wpisać opcję, którą chcemy wybrać: uczeń, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "uczeń" - Należy pobrać imię i nazwisko ucznia (jako jedna zmienna, można
pobrać je jako dwie zmienne, jeżeli zostanie to poprawnie obsłużone) oraz nazwę klasy
(np. "3C")
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela (jako jedna zmienna,
labo dwie, jeżeli zostanie to poprawnie obsłużone), nazwę przedmiotu prowadzonego,
a następnie w nowych liniach nazwy klas, które prowadzi nauczyciel,
aż do otrzymania pustej linii.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko wychowawcy (jako jedna zmienna,
albo dwie, jeżeli zostanie to poprawnie obsłużone), a także nazwę prowadzonej klasy.
Polecenie "koniec" - Wraca do pierwszego menu.

Proces zarządzania użytkownikami:

Należy wpisać opcję, którą chcemy wybrać: klasa, uczen, nauczyciel, wychowawca, koniec.
Po wykonaniu każdej z opcji (oprócz "koniec") wyświetla to menu ponownie.
Polecenie "klasa" - Należy pobrać klasę, którą chcemy wyświetlić (np. "3C") program ma
wypisać wszystkich uczniów, którzy należą do tej klasy, a także wychowawcę tejże klasy.
Polecenie "uczeń" - Należy pobrać imię i nazwisko uczenia, program ma wypisać wszystkie
 lekcje, które ma uczeń a także nauczycieli, którzy je prowadzą.
Polecenie "nauczyciel" - Należy pobrać imię i nazwisko nauczyciela, program ma wypisać
wszystkie klasy, które prowadzi nauczyciel.
Polecenie "wychowawca" - Należy pobrać imię i nazwisko nauczyciela, a program ma wypisać
wszystkich uczniów, których prowadzi wychowawca.
Polecenie "koniec" - Wraca do pierwszego menu.
"""

DOSTEPNE_KOMENDY = (
    'utworz',
    'zarzadzaj',
    'koniec',
)
uczniowie = []
nauczyciele = []
wychowawcy = []
class Uczen:
    def __init__(self, name, klasa):
        self.name = name
        self.klasa = klasa
class Nauczyciel:
    def __init__(self, name, przedmiot, klasa):
        self.name = name
        self.przedmiot = przedmiot
        self.klasa = klasa
class Wychowawca:
    def __init__(self, name, klasa):
        self.name = name
        self.klasa = klasa
while True:
    print(f'Komenda: {DOSTEPNE_KOMENDY}')
    komenda = input('Wprowadz Komende:').strip()
    print(f'Wprowadzona Komenda: {komenda.upper()}')
    if komenda not in DOSTEPNE_KOMENDY:
        print('Zla Komenda')
    if komenda == 'koniec':
        print('Koniec Programu, Milego Dnia')
        break
    elif komenda == 'utworz':
        print(f'Wykonuje Akcje {komenda.upper()}...')
        POLECENIA = (
            'uczen',
            'nauczyciel',
            'wychowawca',
            'koniec',
        )
        while True:
            print(f'Polecenie: {POLECENIA}')
            polecenie = input('wprowadz polecenie:').strip()
            print(f'Wprowadzono Polecenie: {polecenie.upper()}')
            if polecenie not in POLECENIA:
                print('Zle Polecenie')
            if polecenie == 'koniec':
                print('Koniec, Powrot do Glownego Menu')
                break
            elif polecenie == 'uczen':
                print(f'Wykonuje Polecenie... {polecenie.upper()}')
                name = input('Podaj Imie i Nazwisko Ucznia:')
                klasa = input('Podaj Nazwe Klasy Ucznia:')
                s = Uczen(name=name, klasa=klasa)
                uczniowie.append(s)
            elif polecenie == 'nauczyciel':
                print(f'Wykonuje Polecenie... {polecenie.upper()}')
                name = input('Podaj Imie i Nazwisko Nauczyciela:')
                przedmiot = input('Podaj Nazwe Przedmiotu Nauczyciela:')
                klasa = input('Podaj Nazwe Klasy Prowadzonej przez Nauczyciela:')
                n = Nauczyciel(name=name, przedmiot=przedmiot, klasa=klasa)
                nauczyciele.append(n)
            elif polecenie == 'wychowawca':
                print(f'Wykonuje Polecenie... {polecenie.upper()}')
                name = input('Podaj Imie i Nazwisko Wychowawcy:')
                klasa = input('Podaj Nazwe Klasy Wychowawcy:')
                w = Wychowawca(name=name, klasa=klasa)
                wychowawcy.append(w)
    elif komenda == 'zarzadzaj':
        print(f'Wykonuje Akcje {komenda.upper()}...')
        POLECENIA_B = (
            'klasa',
            'uczen',
            'nauczyciel',
            'wychowawca',
            'koniec',

        )
        while True:
            print(f'Dostepne Polecenia: {POLECENIA_B}')
            polecenie_b = input('Wprowadz Polecenie:').strip()
            print(f'Wykonuje Polecenie... {polecenie_b.upper()}')
            if polecenie_b not in POLECENIA_B:
                print('Zle Polecenie')
            if polecenie_b == 'koniec':
                print('Koniec, Wracam do Glownego Menu')
                break
            elif polecenie_b == 'klasa':
                print(f'Wykonuje Polecenie... {polecenie_b.upper()}')
                klasa = input('Wpisz Klase: ')
                w = Wychowawca(name=name, klasa=klasa)
                s = Uczen(name=name, klasa=klasa)
                print(f'Uzniowie Klasy {klasa} : {s.name}, Wychowawca: {w.name}')

            elif polecenie_b == 'uczen':
                print(f'Wykonuje Polecenie... {polecenie_b.upper()}')
                name = input('Podaj Imie i Nazwisko Ucznia: ')
                s = Uczen(name=name, klasa=klasa)
                n = Nauczyciel(name=name, przedmiot=przedmiot, klasa=klasa)
                print(f'Uczen: {name}, Klasa: {s.klasa}, Przedmioty: {n.przedmiot}')
            elif polecenie_b == 'nauczyciel':
                print(f'Wykonuje Polecenie... {polecenie_b.upper()}')
                name = input('Podaj Imie i Nazwisko Nauczyciela: ')
                n = Nauczyciel(name=name, przedmiot=przedmiot, klasa=klasa)
                print(f'Nauczyciel: {name}, Wykłada: {n.przedmiot}, w Klasach: {n.klasa}')
            elif polecenie_b == 'wychowawca':
                print(f'Wykonuje Polecenie... {polecenie_b.upper()}')
                name = input('Podaj Imie i Nazwisko Wychowawcy: ')
                w = Wychowawca(name=name, klasa=klasa)
                print(f'Wychowawca: {name}, Wychowuje Klase; {w.klasa}')


