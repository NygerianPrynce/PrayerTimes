
"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Fadhil Lawal
Date:   7/1/2020
"""
import json,os
import ast
from urllib.request import Request, urlopen # Python 3
def analog(s):
    """Returns a copy of s in analog form

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    word = s.index(":")
    front = int(s[1:word])
    back = (s[word+1:])
    if front > 12:
        front = front - 12
    front = str(front)
    back = str(back)
    true = front + ":" + back
    return true

def before_space(s):
    """Returns a copy of s up to, but not including, the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space
    """
    word = s.index(" ")
    actual = s[:word]
    return actual


def after_space(s):
    '''Returns a copy of s after the first space

    Parameter s: the string to slice
    Precondition: s is a string with at least one space'''

    word = s.index(" ")
    actual2 = s[word+1:]
    return actual2


def first_inside_quotes(s):
    '''Returns the first substring of s between two (double) quotes

    A quote character is one that is inside a string, not one that
    delimits it.  We typically use single quotes (') to delimit a
    string if we want to use a double quote character (") inside of it.

    Examples:
    first_inside_quotes('A "B C" D') returns 'B C'
    first_inside_quotes('A "B C" D "E F" G') returns 'B C',
    because it only picks the first such substring

    Parameter s: a string to search
    Precondition: s is a string containing at least two double quotes'''
    word = s.index("\"")
    actual = s[word+1:]
    mword = actual.index("\"")
    return actual[:mword]


def get_fajr(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('Fajr')
    json = json[result + 7:]
    result2 = json.index(" ")
    json = json[:result2]
    json = json.replace(" ","\"")
    json = analog(json)
    return json

def get_dhuhr(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('Dhuhr')
    json = json[result + 8:]
    result2 = json.index(" ")
    json = json[:result2]
    json = json.replace(" ","\"")
    json = analog(json)
    return json

def get_asr(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('Asr')
    json = json[result + 6:]
    result2 = json.index(" ")
    json = json[:result2]
    json = json.replace(" ","\"")
    json = analog(json)
    return json

def get_maghrib(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('Maghrib')
    json = json[result + 10:]
    result2 = json.index(" ")
    json = json[:result2]
    json = json.replace(" ","\"")
    json = analog(json)
    return json

def get_isha(json):
    '''Returns the lhs value in the response to a currency query

    Given a JSON response to a currency query, this returns the
    string inside double quotes (") immediately following the keyword
    "lhs". For example, if the JSON is
    '{ "ok":true, "lhs":"1 Bitcoin", "rhs":"9916.0137 Euros", "err":"" }'
    then this function returns '1 Bitcoin' (not '"1 Bitcoin"').

    This function returns the empty string if the JSON response
    contains an error message.

    Parameter json: a json string to parse
    Precondition: json is the response to a currency query'''
    result = json.find('Isha')
    json = json[result + 7:]
    result2 = json.index(" ")
    json = json[:result2]
    json = json.replace(" ","\"")
    json = analog(json)
    return json

def get_json(date, json):
    result = json.find(date)
    json = json[result - 243:result-82]
    return json


def prayertime_response(adress, month, year):
    '''Returns a JSON string that is a response to a currency query.

    A currency query converts amt money in currency src to the
    currency dst. The response should be a string of the form

    '{ "ok":true, "lhs":"<old-amt>", "rhs":"<new-amt>", "err":"" }'

    where the values old-amount and new-amount contain the value
    and name for the original and new currencies. If the query is
    invalid, both old-amount and new-amount will be empty, while
    "ok" will be followed by the value false (and "err" will have
    an error message).

    Parameter src: the currency on hand (the LHS)
    Precondition: src is a string with no spaces or non-letters

    Parameter dst: the currency to convert to (the RHS)
    Precondition: dst is a string with no spaces or non-letters

    Parameter amt: amount of currency to convert
    Precondition: amt is a float'''
    url = 'http://api.aladhan.com/v1/calendarByAddress?address=Sultanahmet Mosque, Istanbul, Turkey&method=2&month=04&year=2017'
    #url = 'https://api.aladhan.com/v1/calendarByAddress?address=Sultanahmet%20Mosque,%20Istanbul,%20Turkey&method=2&month=04&year=2017'
    url = url.replace("Sultanahmet Mosque, Istanbul, Turkey", adress)
    url = url.replace("04", str(month))
    url = url.replace("2017", str(year))
    switch = str.maketrans(" ", "%")
    url = url.translate(switch)
    req = Request(url, headers = {'User-Agent': 'Chrome', 'Content-Type': 'application/json'})
    response = urlopen(req).read().decode('utf-8')
    jsonString = json.loads(response)
    return str(jsonString)
