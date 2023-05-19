# Build the docker image


# Run the docker image

```sh
docker-compose -f docker-compose.yml up
```

# payload example:

```json
{
    "points": "2,2;-1,30;20,11;4,5",
}
```

# response example:

```json
{
    "closest_points": [],
}
```


# included sqlite db 
    
```sh
username: root
password: root
```

# call the api with the following url:

```sh
http://localhost:8000/geoapp/distance/

```


