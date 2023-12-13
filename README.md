[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-DataPrakiraanCuaca

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GBPFnKZa4AAqdsA.jpeg)

Program ini dirancang untuk melakukan web scraping pada situs berita Kompas dengan memanfaatkan </br>parameter seperti kategori (category), tanggal, dan halaman (page). </br>Tujuan utama dari program ini adalah untuk mengumpulkan informasi berita dari Kompas sesuai </br>dengan kriteria yang diinputkan oleh pengguna.

## Requirements

- **Python >= 3.11.4**
- **pyquery >= 2.0.0**
- **pytz >= 2023.3.post1**
- **Requests >= 2.31.0**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-Kompas

# Change Directory
cd craw-Kompas

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```sh
python main.py --site=News --page=2 --date=2023-12-08 --output=data
```

### Flags

| Flag     | Alias |             Description             | Example           | Default |
| :------- | :---: | :---------------------------------: | :---------------- | :-----: |
| --site   |  -s   | [category](Category.md) of the site | --site=News       |  News   |
| --page   |  -p   |       number page of the site       | --page=2          |    1    |
| --date   |  -d   |          date of the site           | --date=2023-12-08 |   now   |
| --output |  -o   |        json file output path        | --output=data     |  data   |

# Sample Output

```json
{
  "timestamp": "2023-12-13T03:42:54",
  "source": "meteofactory",
  "productioncenter": "NC Jakarta",
  "data": [
    {
      "kabupaten": {
        "en_US": "Jakarta Barat",
        "id_ID": "Kota Jakarta Barat"
      },
      "provinsi": "DKI Jakarta",
      "coordinate": "106.731319 -6.203019",
      "parameter": {
        "kelembapan_udara": {
          "type": "hourly",
          "timerange": [
            {
              "datetime": "2023-12-13T00:00:00",
              "value": {
                "%": 80.0
              }
            }
            // more time
          ]
        },
        "kelembapan_udara_maksimum": {
          "type": "daily",
          "timerange": [
            {
              "datetime": "2023-12-13T12:00:00",
              "value": {
                "%": 80.0
              }
            }
            // more time
          ]
        },
        "suhu_udara_maksimum": {
          "type": "daily",
          "timerange": [
            {
              "datetime": "2023-12-13T12:00:00",
              "value": {
                "C": 31.0,
                "F": 87.8
              }
            }
            // more time
          ]
        },
        "kelembapan_udara_minimum": {
          "type": "daily",
          "timerange": [
            {
              "datetime": "2023-12-13T12:00:00",
              "value": {
                "%": 65.0
              }
            }
            // more time
          ]
        },
        "suhu_udara_minimum": {
          "type": "daily",
          "timerange": [
            {
              "datetime": "2023-12-13T12:00:00",
              "value": {
                "C": 23.0,
                "F": 73.4
              }
            }
            // more time
          ]
        },
        "suhu_udara": {
          "type": "hourly",
          "timerange": [
            {
              "datetime": "2023-12-13T00:00:00",
              "value": {
                "C": 25.0,
                "F": 77.0
              }
            }
            // more time
          ]
        },
        "cuaca": {
          "type": "hourly",
          "timerange": [
            {
              "datetime": "2023-12-13T00:00:00",
              "value": "Cerah Berawan / Partly Cloudy"
            }
            // more time
          ]
        },
        "arah_angin": {
          "type": "hourly",
          "timerange": [
            {
              "datetime": "2023-12-13T00:00:00",
              "value": {
                "deg": 247.5,
                "CARD": "West-Southwest",
                "SEXA": 24730.0
              }
            }
            // more time
          ]
        },
        "kecepatan_angin": {
          "type": "hourly",
          "timerange": [
            {
              "datetime": "2023-12-13T00:00:00",
              "value": {
                "Kt": 2.0,
                "MPH": 2.3015589,
                "KPH": 3.704,
                "MS": 1.028888888
              }
            }
            // more time
          ]
        }
      }
    }
    // more kabupaten
  ]
}
```
