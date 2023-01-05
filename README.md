<!-- PROJECT SHIELDS -->
[[Közreműködők]][contributors-url]&emsp;
[[Issues]][issues-url]&emsp;
[[MIT Licensz]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center" id="readme-top">

  <h3 align="center">Parking Lot Manager</h3>

  <p align="center">
    (PLM)
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Tartalomjegyzék</summary>
  <ol>
    <li>
      <a href="#about-the-project">A Projektről</a>
      <ul>
        <li><a href="#built-with">Ezzel készült</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Kezdjünk neki</a>
      <ul>
        <li><a href="#prerequisites">Előfeltételek</a></li>
        <li><a href="#installation">Letöltés</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Közreműködők</a></li>
    <li><a href="#license">Licensz</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
<div id="about-the-project"></div>
<h2> A Projektről </h2>

A Parking Lot manager egy parkolóház rendszám alapú beléptetését kezelő program.
A parkolóház bejáratánál a **rendszámot felismerve** egy **MySQL adatbázis** segítségével dönti el, hogy az adott jármű bejöhet-e, avagy sem.

Az adatbázisban tároljuk:
* Az **érvényes, és leját** bérlettel rendelkező **rendszámokat**
* A **szektor(oka)t**, amely(ek)re a bérlet érvényes (volt)
* A rendszámokat használó személyek **e-mail címét**

<p align="right">(<a href="#readme-top">vissza az elejére</a>)</p>


<div id="built-with"></div>
<h2> Ezzel készült </h2>

Az alább látható library-k voltak használva a projekt elkészítésekor:
* [MySQLConnector][MySQLConnector-url]
* [Matplotlib][Matplotlib-url]
* [Beautifulsoup][Beautifulsoup-url]
* [Dateutil][Dateutil-url]

<p align="right">(<a href="#readme-top">vissza az elejére</a>)</p>



<!-- GETTING STARTED -->
<div id="getting-started"></div>
<h2> Kezdjünk neki </h2>

<div id="prerequisites"></div>
<h2> Előkövetelmények </h2>

Kelleni fog:
* [Python][Python-url]
* [Pip][Pip-url]

<div id="installation"></div>
<h2> Letöltés </h2>

Az alábbi utasítások követésével tudja letölteni, és használni az appot.

1. Szerezze be a client_secret.json-t, az email küldés működéséhez
2. Klónozza a repót
   ```sh
   git clone https://github.com/ThisIsJustAGuy/LicensePlateRecognision
   ```
3. Telepítse ezeket a köyvtárakat:
  * MySQL connector

    ```sh
    pip install mysql-connector-python 
    ```

  * Gmail-es levélküldéshez szükséges

    ```sh
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    pip install beautifulsoup4
    ```

  * Matplotlib, amely magával hozza a Numpy-t is

    ```sh
    pip install matplotlib
    ```

  * Dateutil

    ```sh
    pip install python-dateutil
    ```
4. Hozza létre a szükséges adatbázist  
5. Futtassa.... ide majd ha kész kiegészül

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<div id="contributing"></div>
<h2> Közreműködők </h2>

* [Borbély Bálint][BB]
* [Fábry László][FL]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
<div id="license"></div>
<h2> Licensz </h2>

A projektet MIT licesz védi. További információért tekintse meg a `LICENSE` fájlt.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-url]: https://github.com/ThisIsJustAGuy/LicensePlateRecognision/graphs/contributors
[issues-url]:https://github.com/ThisIsJustAGuy/LicensePlateRecognision/issues
[license-url]: https://github.com/ThisIsJustAGuy/LicensePlateRecognision/blob/main/LICENSE

[Python-url]: https://www.python.org/downloads/windows/
[Pip-url]: https://pip.pypa.io/en/stable/installation/
[BB]: https://github.com/ThisIsJustAGuy
[FL]: https://github.com/fabrylaszlo
[Matplotlib-url]: https://matplotlib.org
[MySQLConnector-url]: https://pypi.org/project/mysql-connector-python/
[Beautifulsoup-url]: https://beautiful-soup-4.readthedocs.io/en/latest/
[Dateutil-url]: https://dateutil.readthedocs.io/en/stable/
