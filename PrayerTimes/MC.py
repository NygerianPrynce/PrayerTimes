def monthconv(month):
    monthConversions = {
        "January": "Jan",
        "February": "Feb",
        "March": "Mar",
        "April": "Apr",
        "May": "May",
        "June": "Jun",
        "July": "Jul",
        "August": "Aug",
        "September": "Sep",
        "October": "Oct",
        "November": "Nov",
        "December": "Dec",
    }
    frontw = month.index(" ")
    frontact = month[:frontw]
    backw = month.index(" ")
    backact = month[backw+1:]
    backw2 = backact.index(" ")
    backact2 = backact[backw2+1:]
    word = month.index(" ")
    actual = month[word+1:]
    mword = actual.index(" ")
    final = actual[:mword]
    fax = frontact + " " + monthConversions.get(final) + " " + backact2
    return fax
def monthnum(month):
    monthnum = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
    }
    word = month.index(" ")
    actual = month[word+1:]
    mword = actual.index(" ")
    tr = actual[:mword]
    done = monthnum.get(tr)
    return done
def year(month):
    word = month.index(" ")
    actual = month[word + 1:]
    mword = actual.index(" ")
    tr = actual[mword + 1:]
    return tr

