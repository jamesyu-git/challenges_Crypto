start appium server by default port 4723
appium --use-plugins=inspector --allow-cors --relaxed-security

excute test and generate report
pytest --html=.\report\report.html .\test.py
