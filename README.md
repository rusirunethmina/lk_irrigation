# lk_irrigation 🇱🇰

![Status: Live](https://img.shields.io/badge/status-live-brightgreen)

Realtime Data about *River Water Levels* in Sri Lanka, from the [Irrigation Deptartment](https://www.irrigation.gov.lk)'s [Hydrology and Disaster Management](https://www.irrigation.gov.lk/web/index.php?option=com_content&view=article&id=27&Itemid=128&lang=en) Division.

- [Complete Dataset](data/rwlds) with **5,699 measurements**
- [Scrape and load logic](src/lk_irrigation/rwld/RiverWaterLevelDataLoadMixin.py)
- [Original Data source](https://www.arcgis.com/apps/dashboards/2cffe83c9ff5497d97375498bdf3ff38) Public Domain. Please share and reuse!

## Latest 20 Measurements

| Measured At | Station (River) | Level (m) | Alert Level |
| --- | --- | ---: | --- |
| 2025-11-30 12:28:47 | Padiyathalawa (Maduru Oya) | 1.20 | 🟢 Normal |
| 2025-11-30 12:12:21 | Yaka Wewa (Mukunu Oya) | 1.63 | 🟢 Normal |
| 2025-11-30 12:08:51 | Hanwella (Kelani Ganga) | 10.75 | 🔴 Major Flood |
| 2025-11-30 12:08:46 | Holombuwa (Gurugoda Oya) | 1.98 | 🟢 Normal |
| 2025-11-30 12:08:46 | Urawa (Urubokka Ganga) | 0.85 | 🟢 Normal |
| 2025-11-30 12:07:43 | Nagalagam Street (Kelani Ganga) | 2.27 | 🔴 Major Flood |
| 2025-11-30 12:06:55 | Panadugama (Nilwala Ganga) | 3.83 | 🟢 Normal |
| 2025-11-30 12:06:20 | Rathnapura (Kalu Ganga) | 6.96 | 🟡 Alert |
| 2025-11-30 12:05:28 | Baddegama (Gin Ganga) | 2.59 | 🟢 Normal |
| 2025-11-30 12:04:46 | Deraniyagala (Seethawaka Ganga) | 1.66 | 🟢 Normal |
| 2025-11-30 12:04:08 | Thalgahagoda (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:26 | Glencourse (Kelani Ganga) | 17.47 | 🟠 Minor Flood |
| 2025-11-30 12:03:18 | Pitabeddara (Nilwala Ganga) | 1.27 | 🟢 Normal |
| 2025-11-30 12:03:18 | Moraketiya (Walawe Ganga) | 1.80 | 🟢 Normal |
| 2025-11-30 12:03:12 | Putupaula (Kalu Ganga) | 4.25 | 🟠 Minor Flood |
| 2025-11-30 12:02:29 | Kithulgala (Kelani Ganga) | 2.48 | 🟢 Normal |
| 2025-11-30 12:02:24 | Dunamale (Aththanagalu Oya) | 5.19 | 🟠 Minor Flood |
| 2025-11-30 12:02:20 | Siyambalanduwa (Heda Oya) | 1.39 | 🟢 Normal |
| 2025-11-30 12:02:15 | Kuda Oya (Kuda Oya) | 2.06 | 🟢 Normal |
| 2025-11-30 12:02:13 | Katharagama (Menik Ganga) | 1.19 | 🟢 Normal |

![Maintainer](https://img.shields.io/badge/maintainer-nuuuwan-red)
![MadeWith](https://img.shields.io/badge/made_with-python-blue)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)