# gpx2map

Aplikacja wykreśla trasę z pliku GPX na mapie OSM.

## Instalacja

    $ git clone https://github.com/artekw/gpx2map
    $ cd gpx2map
    $ mkdir maps; mkdir uploads
    $ chmod +x gpx2map.py


## Aplikacja w kontenerze Dockera

Plik Dockerfile napisany jest dla urządzeni opartych o architekturę armhf tj. CHIP, Raspberry Pi i inne. Dla x86 wymaga modyfikacji sekcji 'FROM'.

	$ git clone https://github.com/artekw/gpx2map
	$ cd gpx2map
    $ docker build -t gpx2map:latest .
    $ docker run -d -p 5000:5000 gpx2map


## Todo
 - statystyka trasy (długość, czas, wzniosy, spadki, prędkość)
 - dockerfile
 - cofanie z mapy do strony głównej
 - archiwum map
 - template formatki do uploudowania
 - iframe zamiast ładowania wygenerowanej strony ?!
 - kolor i szerokość trasy do wyboru przy upload gpx'a
 - bug - jak są tylko punkty wywala error - rysuje tylko z tras


License
----

MIT

**Free Software, Hell Yeah!**


