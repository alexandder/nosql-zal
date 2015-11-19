= Technologie nosql - zaliczenie
Aleksander Bolt <aleksanderbolt@yahoo.com>
:icons: font

:===
Procesor,21312

bsondump subreddit.bson > subreddit.json
time mongorestore -d nosql -c subreddit subreddit.bson
https://dl.dropboxusercontent.com/u/15056258/mongodb/reddit.zip


Ponieważ w opisie subredditów znajdują się często słowa z pojedynczym apostrofem (na przykład don't), zastępujemy znak ' znakiem spacji. W przeciwnym wypadku otrzymalibyśmy błąd przy próbie wstawienia danych. Można to zrobić np. tak

sed "s/'/ /g" subreddit.json > subreddits.json
