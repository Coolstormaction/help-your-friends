import bookDescription
import functions
import time
import random
import googletrans
import audio
from rich import print

bookList = [
    "Harry Potter",
    "The Alchemist",
    "The Hound of The Baskervilles",
    "Rich Dad Poor Dad",
]
inappropriateBookList = []
longUsage = False
ifFeedback = random.choice([True, False])
starList = []

bookDescriptionDict = {
    bookList[0]: bookDescription.bookDescription.harry_potter(),
    bookList[1]: bookDescription.bookDescription.the_alchemist(),
    bookList[2]: bookDescription.bookDescription.sh_holmes(),
    bookList[3]: bookDescription.bookDescription.rich_dad_poor_dad(),
}

while True:
    startTime = time.time()
    print(
        f"""
    ============Commands===============
    avbooks => Get List of Available books
    read => Read a Book from stock
    clang => Change your preferred language
    feedback => Give your feedback, if you enter something like "Content NSFW" or "People using this code for a long time", we will take actions.
    add => Add a book to our stock
    audiobook => Hear a book as audio

    ============Books===============
    We currently have {len(bookList)} in our collection!

    They are - {', '.join(bookList)}
    """
    )
    cmd = input(">>> ")
    if cmd == "avbooks":
        print(", ".join(bookList))
    if cmd == "clang":
        lang = input(
            "What is your preferred language? (Please enter Language codes only) - "
        )
        translator = googletrans.Translator()
        for book in bookDescriptionDict:
            bookDescriptionDict[book] = translator.translate(bookDescriptionDict[book], lang).text

    if cmd == "read":
        book = input("Which book do you want to read? - ")
        check = functions.checkForValidBookInp(bookList, book)
        if check == True and book not in inappropriateBookList:
            print(bookDescriptionDict[book])
        if book in inappropriateBookList:
            print("This book contains content marked as NSFW.")
            ifCont = input(
                "Do you accept you are of legal age and wish to continue? - [Y] Yes [N] No "
            )
            if ifCont == "Y":
                print(bookDescriptionDict[book])
            else:
                print("Thanks for your confirmation.")
        if not check:
            print("This book is not in our stock right now! Please come back later.")

    if cmd == "add":
        book = input("Which book do you want to add? - ")
        description = input("Enter the content of the book - ")

        bookDescriptionDict[book] = description
        bookList.append(book)

    if cmd == "feedback":
        feedbackInp = input("Enter your valuable feedback! - ")
        if (
            "nsfw" in feedbackInp
            or "not sfw" in feedbackInp
            or "Content NSFW" in feedbackInp
        ):
            book_inp = input("Enter the book that's is appropriate or NSFW - ")
            runCheck = functions.checkForValidBookInp(bookList, book_inp)
            if runCheck:
                inappropriateBookList.append(book_inp)
                print(
                    "Book named {book_inp} is now marked as NSFW and if anyone tries to read will be blocked by a legal age confirmation message."
                )
            else:
                print("Not a valid book, please try again.")
        if "too long" in feedbackInp or "using for too long" in feedbackInp:
            print("Done!")
            longUsage = True
    if longUsage:
        if time.time() - startTime > 7200:
            print("You have used this program for more than 2 hours now. Please take a break.")
    if ifFeedback:
        star = int(     
            input(
                "How many stars would you give to this program? Enter an number now!\n"
            )
        )
        for i in range(star):
            starList.append("⭐")
        print(f"Thanks! We now have {''.join(starList)} stars now.")
    if cmd == "audiobook":
        book = input("Which book do you want to hear as audio? - ")
        valid = functions.checkForValidBookInp(bookList, book)
        if valid:
            audio.speak(bookDescriptionDict[book])
        else:
            print("Not a valid book. Please try again.")