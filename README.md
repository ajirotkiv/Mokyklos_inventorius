# Mokyklos_inventorius
Tai yra inventoriaus valdymo programą. Ji skirta mokyklos inventoriaus įvedimui į duomenų bazę ir padeda kontroliuoti ęsamą turtą.

## Pagrindinės savybės
* Naujo inventoriaus įvedimas.
* Inventoriaus redagavimas
* Inventoriaus trinimas.
* Inventoriaus paieška pagal nuroditą kriteriju.
* Inventoriaus sekimas pagal būseną, pvz. ar įranga naudojama, ar remontuojama.
* Inventoriaus atskirimas į ilgalaikį ir trumpalaikį.
* Inventoriaus priskirimas prie naudojimo vietos.
* Inventoriaus statistika.

## Diegimas
1. Atsisiųskite repozitoriją:
git clone https://github.com/ajirotkiv/Mokyklos_inventorius.git

2. cd Mokyklos_inventorius

3. Sukurkite virtualią aplinką:
python -m venv venv source venv/bin/activate # Windows naudokite: venv\Scripts\activate

4. Įidiekite reikalingas bibliotekas:
pip install -r requirements.txt

4. Paleiskite projektą (priklausomai nuo projekto tipo):
python .\manage.py runserver

P.S. Praneškite prašau apie aptiktus programos nesklandumus ir pageidavimus tolimesniam programos kūrimui :-)