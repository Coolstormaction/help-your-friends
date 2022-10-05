import googletrans
import bookDescription
import timeit

preferedLang = ''
preferedLangCode = ''
starList = ["⭐"]

def checkForValidBookInp(bookList, bookName) -> bool:
    if bookName in bookList: return True
    else: return False

def checkForValidLanguageCode(langCode) -> bool:
    data = googletrans.LANGCODES
    for key, value in data.items():
        if value == langCode:
            global preferedLang
            preferedLang = key
            return True
    return False