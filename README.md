### This project is the simplest hello world project
# 
### Pre-install
pip install nose coverage nosexcover --user

### Test Command
nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml tests/tests.py

### Sonar Command
sonar-scanner
