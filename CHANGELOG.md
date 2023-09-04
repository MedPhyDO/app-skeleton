# CHANGELOG

## 0.2.0 / 2023-09-01
- changes for python 3.11
  - change isp/mpdf.py - mathtext() and pandas() changes
  - change isp/safrs.py _get_connection to set/get db_bind in config
    - RQLQuery for compatibility with sqlalchemy >=1.4 since newer rqlalchemy (0.4.5) depends on sqlalchemy <2.0 and >=1.2
    - suppress double call appInfo/appError depends on _s_get() and _s_count()
  - isp/webapp.py 
    - change __init__ and _create_app to set/get db_bind in config
    - use javascript openapi-explorer instead python based flask_swagger_ui

## 0.1.6 / 2023-04-19
- install with python 3.10
- even more changes in isp/ files
- change requirements for known security vulnerabilities
- some changes in tests/

## 0.1.5 / 2022-05-13
- more changes in isp/ files
- change requirements for known security vulnerabilities

## 0.1.4 / 2022-03-28
- many changes in isp/ files
- rename app/db to app.skeleton
- many changes in tests/

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
