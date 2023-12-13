[![Twitter: romy](https://img.shields.io/twitter/follow/RomySihananda)](https://twitter.com/RomySihananda)

# craw-DataPrakiraanCuaca

![](https://raw.githubusercontent.com/RomySaputraSihananda/RomySaputraSihananda/main/images/GBPFnKZa4AAqdsA.jpeg)

Program ini dirancang melakukan crawling data prakiraan cuaca dari [BMKG](https://data.bmkg.go.id). Aplikasi ini</br> memanfaatkan modul **xmltodict** untuk mengolah data XML menjadi dictionary </br>dan **requests** untuk mengambil data dari layanan prakiraan cuaca. </br>Tujuan utama dari program ini adalah untuk mengumpulkan informasi cuaca terkini</br> dari [BMKG](https://data.bmkg.go.id) sesuai dengan provinsi yang diinputkan oleh pengguna.

## Requirements

- **Python >= 3.11.4**
- **Requests >= 2.31.0**
- **xmltodict >= 0.12.0**

## Installation

```sh
# Clonig Repository
git clone https://github.com/romysaputrasihananda/craw-DataPrakiraanCuaca

# Change Directory
cd craw-DataPrakiraanCuaca

# Install Requirement
pip install -r requirements.txt
```

## Example Usages

```sh
python main.py --provinsi=DKIJakarta --output=data
```

### Flags

| Flag       | Alias |             Description             | Example               |  Default   |
| :--------- | :---: | :---------------------------------: | :-------------------- | :--------: |
| --provinsi |  -p   | name of the [province](Province.md) | --provinsi=DKIJakarta | DKIJakarta |
| --output   |  -o   |        json file output path        | --output=data         |    data    |

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
