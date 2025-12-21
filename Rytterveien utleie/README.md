# Rytterveien Hytte Informasjon

Dette er en Flask-applikasjon som genererer en HTML-side med informasjon for gjester av Rytterveien hytta. Siden støtter flere språk (norsk, dansk, tysk, engelsk) og kan eksporteres til PDF for utskrift.

## Installasjon

1. Sørg for at Python er installert (versjon 3.7+).
2. Installer avhengigheter: `pip install -r requirements.txt`

## Kjøring

Kjør applikasjonen med: `python rytterveien.py`

Appen vil kjøre på http://localhost:5000 (eller http://0.0.0.0:5000 hvis tilgjengelig på nettverket).

På hytta kan du finne IP-adressen til maskinen (f.eks. via `ipconfig` på Windows) og dele den med gjestene, slik at de kan få tilgang via mobil.

## Bruk

- Åpne siden i en nettleser.
- Velg språk fra dropdown.
- Fyll inn datoer for boblebad hvis nødvendig.
- Klikk "Last ned som PDF" for å generere en PDF-fil.
- For utskrift, bruk nettleserens utskriftsfunksjon eller PDF-en.

## Tilpasning

- Legg til bilder for søppelsortering i `templates/index.html`.
- Juster CSS i `static/css/style.css` for bedre utseende.
- Legg til flere språk i `static/js/script.js`.