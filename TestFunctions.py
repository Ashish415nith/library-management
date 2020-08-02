from User import Member, Librarian


lib = Librarian("HoneySingh", "Lahore", 30, "ABCD420", "KKR420")
print(lib)
lib.addBook('Shoe Dog','Phil Knight', '2015',312)
lib.addBookItem("Shoe Dog", "01aa", "A1")
lib.addBookItem("Shoe Dog", "02aa", "A2")
lib.addBookItem("Shoe Dog", "03aa", "A3")
lib.addBook('Moonwalking with Einstien','J Foer', '2017',318)
lib.addBookItem("Moonwalking with Einstien", "01BB", "B1")
lib.addBookItem("Moonwalking with Einstien", "02BB", "B2")
lib.addBookItem("Moonwalking with Einstien", "03BB", "B3")
lib.addBook("The fault in our stars", "john green", "2012","678")
lib.addBookItem("The fault in our stars", "01CC", "C1")
lib.addBookItem("The fault in our stars", "02CC", "C2")
lib.addBookItem("The fault in our stars", "03CC", "C2")
lib.viewBooks()
lib.removeBookItem("01aa")
lib.viewBooks()
lib.removeBook("Moonwalking with Einstien")
lib.viewBooks()

member1 = Member("Avinash", "palampur", 23, "AEKK44542", "VDES521")
member2 = Member("Atul", "Karachi", 19, "ERTH234", "FGDGS34")
member3 = Member("Ashish", "palampur", 21, "EFSG34", "GSG345DG")
member4 = Member("Amit","Taliban",34,"4FGGERG","AFAG234")
print(member1)
print(member2)
print(member3)
print(member4)

member1.viewBooks()
member1.search_by_book_name("The fault in our stars")
member1.search_by_book_name("Shoe Dog")
member1.search_by_author_name("john green")
member1.search_by_author_name("JK rowling")

member1.issue_book("The fault in our stars", 8)
member2.issue_book("Shoe Dog", 10)
member1.viewBooks()

lib.view_issued_books()

member1.return_book("001CC")
member1.viewBooks()

member2.issue_book("Shoe Dog")

lib.viewMembers()

lib.removeMember("Amit")
member1.issue_book("The fault in our stars")
lib.viewMembers()
lib.view_issued_books()
