# CHANGELOG

## 0.1.3 / 2021-12-29
- separate versioning for files in isp/ 
- update requirements.txt and requirements_upgrade.txt

## 0.1.2 / 2021-05-19
- change isp/dicom.py - change debug messages
- change isp/safrs.py - changes in additional api results, add _extendedSystemCheck
- change isp/webapp.py - change cors header
- change app/__init__.py - add _extendedSystemCheck
- Some ui changes for _extendedSystemCheck

## 0.1.1 / 2021-04-27
- add isp/client.py - using the same api calls on server
- add isp/dicom.py - enables dicom calls via pynetdicom 
- change isp/webapp.py / safrs.py - allows multiple databases with bind parameter
- change isp/mpdf.py - add mode parameter to text() for markdown support

## 0.1.0 / 2021-01-16
- First Release
