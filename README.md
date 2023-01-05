<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Parking Lot Manager</h3>

  <p align="center">
    (PLM)
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tartalomjegyzék</summary>
  <ol>
    <li>
      <a href="#about-the-project">A Projektről</a>
      <ul>
        <li><a href="#built-with">Így készült</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Kezdjünk neki</a>
      <ul>
        <li><a href="#prerequisites">Előfeltételek</a></li>
        <li><a href="#installation">Telepítés</a></li>
      </ul>
    </li>
    <li><a href="#usage">Használat</a></li>
    <li><a href="#contributing">Közreműködők</a></li>
    <li><a href="#license">Licensz</a></li>
    <li><a href="#contact">Elérhetőség</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## A Projektről

A Parking Lot manager egy parkolóház rendszám alapú beléptetését kezelő program.
A parkolóház bejáratánál a **rendszámot felismerve** egy **MySQL adatbázis** segítségével dönti el, hogy az adott jármű bejöhet-e, avagy sem.

Az adatbázisban tároljuk:
* Az **érvényes, és leját** bérlettel rendelkező **rendszámokat**
* A **szektor(oka)t**, amely(ek)re a bérlet érvényes (volt)
* A rendszámokat használó személyek **e-mail címét**

<p align="right">(<a href="#readme-top">vissza az elejére</a>)</p>



### Built With

Az alább látható library-k voltak használva a projekt elkészítésekor:
* [![MySQLConnector]][MySQLConnector-url]
* [![Matplotlib][Matplotlib]][Matplotlib-url]
* [![Beautifulsoup]][Beautifulsoup-url]
* [![Dateutil]][Dateutil-url]

<p align="right">(<a href="#readme-top">vissza az elejére</a>)</p>



<!-- GETTING STARTED -->
## Kezdjünk neki

Hogy kezdjük a használatot:

### Előkövetelmények

<p align="left">Kelleni fog a:</p>
* <a href="https://www.python.org/downloads/windows/">Python</a>
* <a href="https://pip.pypa.io/en/stable/installation/">Pip</a>

### Letöltés

Az alábbi utasítások követésével tudja letölteni, és használni az appot.

1. Szerezze be a client_secret.json-t, az email küldés működéséhez
1. Klónozza a repót
   ```sh
   git clone https://github.com/ThisIsJustAGuy/LicensePlateRecognision
   ```
3. Telepítse ezeket a köyvtárakat
   > MySQL connector

  ```sh
  pip install mysql-connector-python
  ```

  > Gmail-es levélküldéshez szükséges

  ```sh
  pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  pip install beautifulsoup4
  ```

  > Matplotlib, amely magával hozza a Numpy-t is

  ```sh 
  pip install matplotlib
  ```

  > Dateutil

  ```sh
  pip install python-dateutil
  ```
4. Hozza létre a szükséges adatbázist  
5. Futtassa.... ide majd ha kész kiegészül

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Közreműködők

* [BB]Borbély Bálint
* [FL]Fábry László

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## Licensz

A projektet MIT licesz védi. További információért tekintse meg a `LICENSE` fájlt.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/ThisIsJustAGuy/LicensePlateRecognision/graphs/contributors
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]:https://github.com/ThisIsJustAGuy/LicensePlateRecognision/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/ThisIsJustAGuy/LicensePlateRecognision/blob/main/LICENSE

[BB]: https://github.com/ThisIsJustAGuy
[FL]: https://github.com/fabrylaszlo
[Matplotlib]: https://matplotlib.org/_static/images/logo_dark.svg
[Matplotlib-url]: https://matplotlib.org
[MySQLConnector]: https://pypi.org/static/images/logo-small.fecb6dab.svg
[MySQLConnector-url]: https://pypi.org/project/mysql-connector-python/
[Beautifulsoup]:
[Beautifulsoup-url]: https://beautiful-soup-4.readthedocs.io/en/latest/
[Dateutil]:
[Dateutil-url]: https://dateutil.readthedocs.io/en/stable/
