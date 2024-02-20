encrypt:

`openssl enc -aes-256-cbc -salt -in GoogleService-Info.plist -out GoogleService-Info.enc -k <password>`

decrypt:

`openssl enc -d -aes-256-cbc -in GoogleService-Info.enc -out GoogleService-Info.plist -k <password>`