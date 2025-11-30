# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)
![LastUpdated](https://img.shields.io/badge/last_updated-2025--12--01_03:02:46-green)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **6,324 measurements** from **39** stations.
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38)

## River Water Level Map

![River Water Level Map](images/map.png)

## Latest measurements

*There were **26** measurements in the last **1 hour**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-12-01 03:02:46 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:02:27 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -1.565 |  |
| 2025-12-01 03:02:07 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:02:06 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:01:47 | Nawalapitiya (Mahaweli Ganga) | 1.97 | 🟢 Normal | -1.565 |  |
| 2025-12-01 03:01:23 | Nawalapitiya (Mahaweli Ganga) | 1.98 | 🟢 Normal | -1.565 |  |
| 2025-12-01 02:11:32 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 02:09:26 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-01 02:08:53 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2025-12-01 02:08:18 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-01 02:08:04 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-01 02:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.50 | 🟠 Minor Flood | 707.143 | 🔺 Rising |
| 2025-12-01 02:06:48 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.010 |  |
| 2025-12-01 02:06:43 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:06:40 | Kalawellawa (Millakanda) (Kalu Ganga) | 2.00 | 🟢 Normal | 707.143 | 🔺 Rising |
| 2025-12-01 02:06:21 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:05:50 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.055 |  |
| 2025-12-01 02:05:31 | Hanwella (Kelani Ganga) | 10.04 | 🔴 Major Flood | -0.064 |  |
| 2025-12-01 02:04:56 | Rathnapura (Kalu Ganga) | 6.06 | 🟡 Alert | -0.069 |  |
| 2025-12-01 02:04:38 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 02:03:53 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 02:03:47 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-01 02:03:35 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:03:16 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-01 02:03:15 | Urawa (Nilwala Ganga) | 0.77 | 🟢 Normal | -0.020 |  |

## Latest by Station

*⌛ = Latest measurement is older than **24 hours**.*

| Measured At | Station (River Basin) | Level (m) | Alert Level | Rate-of-Rise (m/hr) | Rising Alert |
| --- | --- | ---: | --- | ---: | --- |
| 2025-11-27 20:03:23⌛ | Peradeniya (Mahaweli Ganga) | 10.56 | 🔴 Major Flood | 0.595 | 🔺 Rising |
| 2025-11-27 13:00:40⌛ | Weraganthota (Mahaweli Ganga) | 8.37 | 🔴 Major Flood | 0.467 | 🔺 Rising |
| 2025-11-28 06:04:09⌛ | Moragaswewa (Deduru Oya) | 8.33 | 🔴 Major Flood | 0.051 | 🔺 Rising |
| 2025-12-01 02:04:38 | Nagalagam Street (Kelani Ganga) | 2.53 | 🔴 Major Flood | 0.000 |  |
| 2025-12-01 00:09:25 | Thanthirimale (Malwathu Oya) | 10.64 | 🔴 Major Flood | -0.033 |  |
| 2025-12-01 02:05:31 | Hanwella (Kelani Ganga) | 10.04 | 🔴 Major Flood | -0.064 |  |
| 2025-12-01 02:07:08 | Kalawellawa (Millakanda) (Kalu Ganga) | 7.50 | 🟠 Minor Flood | 707.143 | 🔺 Rising |
| 2025-11-28 02:13:33⌛ | Manampitiya (Mahaweli Ganga) | 5.95 | 🟠 Minor Flood | 0.095 | 🔺 Rising |
| 2025-11-27 08:02:16⌛ | Thaldena (Mahaweli Ganga) | 4.25 | 🟠 Minor Flood | 0.050 | 🔺 Rising |
| 2025-11-27 18:42:59⌛ | Galgamuwa (Mee Oya) | 6.12 | 🟠 Minor Flood | 0.045 | 🔺 Rising |
| 2025-11-30 14:56:34 | Ellagawa (Kalu Ganga) | 11.94 | 🟠 Minor Flood | 0.044 | 🔺 Rising |
| 2025-12-01 02:11:32 | Putupaula (Kalu Ganga) | 4.29 | 🟠 Minor Flood | 0.000 |  |
| 2025-12-01 02:02:20 | Dunamale (Aththanagalu Oya) | 4.80 | 🟠 Minor Flood | -0.050 |  |
| 2025-12-01 01:02:59 | Horowpothana (Yan Oya) | 7.41 | 🟡 Alert | -0.019 |  |
| 2025-12-01 02:04:56 | Rathnapura (Kalu Ganga) | 6.06 | 🟡 Alert | -0.069 |  |
| 2025-12-01 00:24:57 | Badalgama (Maha Oya) | 5.05 | 🟡 Alert | -0.313 |  |
| 2025-12-01 02:09:26 | Kithulgala (Kelani Ganga) | 2.39 | 🟢 Normal | 0.037 | 🔺 Rising |
| 2025-12-01 02:03:53 | Norwood (Kelani Ganga) | 1.36 | 🟢 Normal | 0.020 | 🔺 Rising |
| 2025-12-01 02:06:21 | Wellawaya (Kirindi Oya) | 1.23 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:06:43 | Deraniyagala (Kelani Ganga) | 1.45 | 🟢 Normal | 0.000 |  |
| 2025-12-01 03:02:06 | Siyambalanduwa (Heda Oya) | 1.25 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:01:44 | Thawalama (Gin Ganga) | 2.09 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:01:36 | Kuda Oya (Kirindi Oya) | 1.94 | 🟢 Normal | 0.000 |  |
| 2025-12-01 02:06:48 | Panadugama (Nilwala Ganga) | 3.53 | 🟢 Normal | -0.010 |  |
| 2025-12-01 02:08:04 | Thanamalwila (Kirindi Oya) | 1.64 | 🟢 Normal | -0.010 |  |
| 2025-12-01 02:02:12 | Katharagama (Menik Ganga) | 0.94 | 🟢 Normal | -0.010 |  |
| 2025-12-01 02:03:47 | Thalgahagoda (Nilwala Ganga) | 1.02 | 🟢 Normal | -0.011 |  |
| 2025-12-01 02:08:53 | Baddegama (Gin Ganga) | 2.24 | 🟢 Normal | -0.019 |  |
| 2025-12-01 03:02:27 | Pitabeddara (Nilwala Ganga) | 1.10 | 🟢 Normal | -0.020 |  |
| 2025-12-01 02:08:18 | Holombuwa (Kelani Ganga) | 1.45 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:02:07 | Nakkala (Kumbukkan Oya) | 1.74 | 🟢 Normal | -0.020 |  |
| 2025-12-01 02:03:16 | Yaka Wewa (Ma Oya) | 1.29 | 🟢 Normal | -0.020 |  |
| 2025-12-01 03:02:46 | Urawa (Nilwala Ganga) | 0.75 | 🟢 Normal | -0.020 |  |
| 2025-11-30 14:03:57 | Padiyathalawa (Maduru Oya) | 1.17 | 🟢 Normal | -0.021 |  |
| 2025-12-01 00:00:09 | Moraketiya (Walawe Ganga) | 1.41 | 🟢 Normal | -0.030 |  |
| 2025-12-01 02:05:50 | Magura (Kalu Ganga) | 2.30 | 🟢 Normal | -0.055 |  |
| 2025-12-01 01:09:10 | Giriulla (Maha Oya) | 3.64 | 🟢 Normal | -0.073 |  |
| 2025-12-01 02:01:41 | Glencourse (Kelani Ganga) | 14.46 | 🟢 Normal | -0.247 |  |
| 2025-12-01 03:02:10 | Nawalapitiya (Mahaweli Ganga) | 1.96 | 🟢 Normal | -1.565 |  |

## River Water Level Charts by Station

### Peradeniya (Mahaweli Ganga)

![Peradeniya](images/stations/peradeniya.png)

### Weraganthota (Mahaweli Ganga)

![Weraganthota](images/stations/weraganthota.png)

### Moragaswewa (Deduru Oya)

![Moragaswewa](images/stations/moragaswewa.png)

### Nagalagam Street (Kelani Ganga)

![Nagalagam Street](images/stations/nagalagam-street.png)

### Thanthirimale (Malwathu Oya)

![Thanthirimale](images/stations/thanthirimale.png)

### Hanwella (Kelani Ganga)

![Hanwella](images/stations/hanwella.png)

### Kalawellawa (Millakanda) (Kalu Ganga)

![Kalawellawa (Millakanda)](images/stations/kalawellawa-(millakanda).png)

### Manampitiya (Mahaweli Ganga)

![Manampitiya](images/stations/manampitiya.png)

### Thaldena (Mahaweli Ganga)

![Thaldena](images/stations/thaldena.png)

### Galgamuwa (Mee Oya)

![Galgamuwa](images/stations/galgamuwa.png)

### Ellagawa (Kalu Ganga)

![Ellagawa](images/stations/ellagawa.png)

### Putupaula (Kalu Ganga)

![Putupaula](images/stations/putupaula.png)

### Dunamale (Aththanagalu Oya)

![Dunamale](images/stations/dunamale.png)

### Horowpothana (Yan Oya)

![Horowpothana](images/stations/horowpothana.png)

### Rathnapura (Kalu Ganga)

![Rathnapura](images/stations/rathnapura.png)

### Badalgama (Maha Oya)

![Badalgama](images/stations/badalgama.png)

### Kithulgala (Kelani Ganga)

![Kithulgala](images/stations/kithulgala.png)

### Norwood (Kelani Ganga)

![Norwood](images/stations/norwood.png)

### Wellawaya (Kirindi Oya)

![Wellawaya](images/stations/wellawaya.png)

### Deraniyagala (Kelani Ganga)

![Deraniyagala](images/stations/deraniyagala.png)

### Siyambalanduwa (Heda Oya)

![Siyambalanduwa](images/stations/siyambalanduwa.png)

### Thawalama (Gin Ganga)

![Thawalama](images/stations/thawalama.png)

### Kuda Oya (Kirindi Oya)

![Kuda Oya](images/stations/kuda-oya.png)

### Panadugama (Nilwala Ganga)

![Panadugama](images/stations/panadugama.png)

### Thanamalwila (Kirindi Oya)

![Thanamalwila](images/stations/thanamalwila.png)

### Katharagama (Menik Ganga)

![Katharagama](images/stations/katharagama.png)

### Thalgahagoda (Nilwala Ganga)

![Thalgahagoda](images/stations/thalgahagoda.png)

### Baddegama (Gin Ganga)

![Baddegama](images/stations/baddegama.png)

### Pitabeddara (Nilwala Ganga)

![Pitabeddara](images/stations/pitabeddara.png)

### Holombuwa (Kelani Ganga)

![Holombuwa](images/stations/holombuwa.png)

### Nakkala (Kumbukkan Oya)

![Nakkala](images/stations/nakkala.png)

### Yaka Wewa (Ma Oya)

![Yaka Wewa](images/stations/yaka-wewa.png)

### Urawa (Nilwala Ganga)

![Urawa](images/stations/urawa.png)

### Padiyathalawa (Maduru Oya)

![Padiyathalawa](images/stations/padiyathalawa.png)

### Moraketiya (Walawe Ganga)

![Moraketiya](images/stations/moraketiya.png)

### Magura (Kalu Ganga)

![Magura](images/stations/magura.png)

### Giriulla (Maha Oya)

![Giriulla](images/stations/giriulla.png)

### Glencourse (Kelani Ganga)

![Glencourse](images/stations/glencourse.png)

### Nawalapitiya (Mahaweli Ganga)

![Nawalapitiya](images/stations/nawalapitiya.png)

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)