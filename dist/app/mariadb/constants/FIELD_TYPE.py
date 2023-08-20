"""
MariaDB FIELD_TYPE Constants

These constants represent the field types supported by MariaDB.
The field type is returned as second element of cursor description attribute.

Field types are defined in module *mariadb.constants.FIELD_TYPE*
"""

DECIMAL = 0
TINY = 1
SHORT = 2
LONG = 3
FLOAT = 4
DOUBLE = 5
NULL = 6
TIMESTAMP = 7
LONGLONG = 8
INT24 = 9
DATE = 10
TIME = 11
DATETIME = 12
YEAR = 13
NEWDATE = 14
VARCHAR = 15
BIT = 16
TIMESTAMP2 = 17
DATETIME2 = 18
TIME2 = 19
JSON = 245
NEWDECIMAL = 246
ENUM = 247
SET = 248
TINY_BLOB = 249
MEDIUM_BLOB = 250
LONG_BLOB = 251
BLOB = 252
VAR_STRING = 253
STRING = 254
GEOMETRY = 255