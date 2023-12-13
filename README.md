# craw-DataPrakiraanCuaca

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
