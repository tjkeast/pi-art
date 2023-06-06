# pi-art

## Developement

### Setup

Start venv

```
source .venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Run application

```
python main.py
```

### Help

Lock dependencies

```
pip freeze -l > requirements.txt
```

Run with Docker

```
docker build -t pi-art .
docker run -it pi-art
```
