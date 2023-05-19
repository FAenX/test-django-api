[]: # File: Readme.md
[]: # Project: Readme.md
# Run using dicker compose

```sh
docker-compose -f docker-compose.yml up
```

# call the api with the following url:

```sh
POST request:
http://localhost:8000/geoapp/distance/

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
    "closest_points": [[2, 2], [4, 5]]
}
```


# included sqlite db 
    
```sh
username: root
password: root
```





