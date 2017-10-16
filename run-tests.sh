touch backup.sqlite
cp payBob.sqlite backup.sqlite
rm -f payBob.sqlite
python databaseTests.py
rm -f payBob.sqlite
touch payBob.sqlite
cp backup.sqlite payBob.sqlite
rm -f backup.sqlite
