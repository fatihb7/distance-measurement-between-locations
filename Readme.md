
# Calculating distance between two points

Scripts that calculates the distance from the **"Moscow Ring Road"** location to the location sent via HTTP api.

Flask was used to occur the API. Google maps apis was used for the calculation.

> **WARNING: You must use your google maps api key. If you don't have a key, you can get a key by reading the link below.**

> [Google Maps API](https://developers.google.com/maps/documentation/embed/get-api-key)

## Install dependencies libraries
You can install easy by use docker.
```bashs
docker-compose up
```
You can also install dependency libraries and run **"app.py"** script.

```bash
pip install -r requirements.txt
python app.py
```

## Usage example

```bash
curl http://127.0.0.1:105/api/calcdist?location=kars
```
The results of all requests are logged in the .log file. Your request's response contains the results.

