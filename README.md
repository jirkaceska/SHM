# Informační systém SHM
## Naklonování repozitáře
Aplikaci naklonujete použitím příkazu:
```
git clone https://github.com/jirkaceska/SHM.git
```
Pro rozběhnutí aplikace je zapotřebí mít nainstalován **Python 3** (použitá verze k vývoji byla 3.6.9). Tato verze má v sobě již zabudovaný správce balíčků **pip**.

## Instalace Djanga
Aplikace běží v frameworku [Django](https://www.djangoproject.com/). Pro jeho instalaci použijte příkaz:
```
python -m pip install Django
```

## Instalace závislostí
Aplikace má několik závislostí, které je potřeba doinstalovat:
```
pip3 install django-bootstrap4
pip3 install django-crispy-forms
pip3 install django-stdimage
pip3 install python-dateutil
```

## Migrace
Pro vytvoření potřebných databázových tabulek je potřeba příkaz:
```
python manage.py migrate
```

## Spuštění serveru
Server spustíte použitím příkazu:
```
python manage.py runserver
```
Běžící aplikaci pak naleznete na adrese [http://localhost:8000/](http://localhost:8000/)
