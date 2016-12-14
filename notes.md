
# Parts of an HTTP Request
1. Status Code
2. Verb (GET = read, POST = create new, PUT = replace, PATCH = partial update, DELETE)
3. URL (with params)
4. Headers
5. Data

## Testing that the adding func, POST, works correctly
# invalid add JSON request
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X POST \
    --data '{"country_name": "Narnia"}' \
    http://127.0.0.1:9999/countries/ \
    | less


# valid add JSON request
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X POST \
    --data '{"country_name": "Narnia", "country_abrev": "NN"}' \
    http://127.0.0.1:9999/countries/ \
    | less



## Edit jsons --- Narnia is ({'country_name': u'Narnia', 'country_abrev': u'NN', 'country_id': 257})
# invalid edit JSON request
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X PUT \
    --data '{"country_id": 2,"country_name": "Narnit"}' \
    http://127.0.0.1:9999/countries/2 \
    | less

curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X PUT \
    --data '{"country_id": 2, "country_name": "Narnia", "country_abrev": "NR"}' \
    http://127.0.0.1:9999/countries/2 \
    | less


# valid edit JSON request
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X PUT \
    --data '{"country_id": 257, "country_name": "Narnit", "country_abrev": "NT"}' \
    http://127.0.0.1:9999/countries/257 \
    | less



## Test the delete


# invalid delete JSON request
# not very helpful right now, as it is deleting based on id
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X DELETE \
    --data '{"country_id": 2000, "country_name": "Narnit"}' \
    http://127.0.0.1:9999/countries/2000 \
    | less



# valid delete JSON request
curl -i -s \
    --header "Content-Type: application/json" \
    --header "Accept: application/json" \
    -X DELETE \
    http://127.0.0.1:9999/countries/257 \
    | less



## Yay






