# CV

Generate your CV in PDF format in Spanish and English using [RenderCV](https://github.com/rendercv/rendercv).

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Usage
```bash
# Generate both CVs
python render.py

# Generate only Spanish or English
python render.py es
python render.py en
```

PDFs are generated in `output/es/` and `output/en/`.

## Customization

Edit `cv_es.yaml` and `cv_en.yaml` with your information.

### Change theme
```yaml
design:
  theme: classic  # Options: classic, moderncv, sb2nov, engineeringresumes
```

### Change colors
```yaml
design:
  colors:
    name: rgb(0, 79, 144)
    section_titles: rgb(0, 79, 144)
    links: rgb(0, 79, 144)
```

## Documentation

- [RenderCV Docs](https://docs.rendercv.com/)
- [Examples](https://github.com/rendercv/rendercv/tree/main/examples)