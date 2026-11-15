# Werim

**Hasattan önce bil.**

Research code for estimating district-level sunflower yield in Thrace (Tekirdağ, Kırklareli, Edirne) weeks before harvest, using Sentinel-2 NDVI and ERA5-Land weather data.

Prepared for TÜBİTAK 2204-A (deadline: 4 January 2027).

## Research question

How accurately can district-level sunflower yield in Thrace be predicted, as of the end of June, for a year the model has never seen?

## Structure

| Folder | Contents |
|---|---|
| `data/raw` | Original downloads (TÜİK, Earth Engine exports). Not in git. |
| `data/processed` | Cleaned tables, e.g. `dataset.csv`. Not in git. |
| `notebooks` | Exploration and analysis notebooks |
| `src` | Reusable Python code |
| `report` | TÜBİTAK report (Turkish) and figures |
| `docs` | Decisions, logs, sources, ideas |

## Setup

```bash
python3.14 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
