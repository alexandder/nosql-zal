= Technologie nosql - zaliczenie
Aleksander Bolt <aleksanderbolt@yahoo.com>
:icons: font


bsondump subreddit.bson > subreddit.json


Ponieważ w opisie subredditów znajdują się często słowa z pojedynczym apostrofem (na przykład don't), zastępujemy znak ' znakiem spacji. W przeciwnym wypadku otrzymalibyśmy błąd przy próbie wstawienia danych. Można to zrobić np. tak

sed "s/'/ /g" subreddit.json > subreddits.json
