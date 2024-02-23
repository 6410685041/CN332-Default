encrypt:

`openssl enc -aes-256-cbc -salt -in key.py -out key.enc -k <password>`

decrypt:

`openssl enc -d -aes-256-cbc -in key.enc -out key.py -k <password>`

activate:

make sure you remove the database first
`python script.py`