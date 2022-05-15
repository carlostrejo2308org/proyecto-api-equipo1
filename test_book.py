from cgitb import text
from os import times
from unittest.mock import patch
import json
import urllib.request
import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self) -> None:
        self.libro = Book()

    def test_extraer(self):
        cases = [
            ("UpNHAQAAMAAJ", "{'title': 'The Dropout: Schools Search for Clues to His Problems; Information: Terms and Computations. Reprint from School Life, May 1963', 'subtitle': '', 'authors': ['United States. Education Office'], 'publisher': '', 'publishedDate': '1963', 'description': '', 'pageCount': 15, 'categories': ''}"),
            ("DgbhAAAAMAAJ", "{'title': 'Search INFORM.', 'subtitle': '', 'authors': '', 'publisher': 'Data Courier', 'publishedDate': '1986', 'description': '', 'pageCount': 362, 'categories': ''}"),
            ("gqDf__ULmR8C", "{'title': 'Flexible Query Answering Systems', 'subtitle': '8th International Conference, FQAS 2009, Roskilde, Denmark, October 26-28, 2009, Proceedings', 'authors': ['Troels Andreasen', 'Ronald R. Yager', 'Henrik Bulskov', 'Henning Christiansen', 'Henrik Legind Larsen'], 'publisher': 'Springer Science & Business Media', 'publishedDate': '2009-10-15', 'description': 'This volume constitutes the Proceedings of the 8th International Conference on Flexible Query Answering Systems, FQAS 2009, held in Roskilde, Denmark, October 26–28, 2009. FQAS 2009 was preceded by the 1994, 1996 and 1998 editions held in Roskilde, Denmark, the FQAS 2000 held in Warsaw, Poland, the 2002 held in Copenhagen, Denmark, and the 2004 and 2006 editions held in Lyon, France, and in Milan, Italy, respectively. FQAS is the premier conference concerned with the very important issue of providing users of information systems with ?exible querying capabilities, and withaneasyandintuitiveaccesstoinformation.Themainobjectiveistoachieve more expressive, informative, cooperative, and productive systems which faci- tate retrieval from information repositories such as databases, libraries, hete- geneous archives and the World-Wide Web. In targeting this objective, the c- ference draws on several research areas, such as information retrieval, database management, information ?ltering, knowledge representation, soft computing, management of multimedia information, and human–computer interaction. The conference provides a unique opportunity for researchers, developers and pr- titioners to explore new ideas and approaches in a multidisciplinary forum. The overalltopic of the FQAS conferences is innovative query systems aimed at providing easy, ?exible and human-friendly access to information. Such s- tems arebecoming increasinglyimportantalsodue to the huge andalwaysgr- ing number of users as well as the growing amount of available information.', 'pageCount': 676, 'categories': ['Computers / Natural Language Processing', 'Computers / System Administration / Storage & Retrieval', 'Computers / Databases / Data Mining', 'Computers / Intelligence (AI) & Semantics', 'Computers / Databases / General', 'Computers / Information Technology', 'Computers / Software Development & Engineering / General']}"),
            ("a","No Existe")
            ]
    
        for inp, expected in cases:
            with self.subTest(inp=inp, expected=expected):
                obtained = str(self.libro.ExtraerElementos(inp))
                self.assertEqual(obtained, expected, "(%s) deberia ser %s" % (inp, expected))

    @patch("book.Book.ExtraerElementos", return_value="{'title': 'Search INFORM.', 'subtitle': '', 'authors': '', 'publisher': 'Data Courier', 'publishedDate': '1986', 'description': '', 'pageCount': 362, 'categories': ''}")
    def test_mockeando(self,mock_entrada):
        librito = Book()
        cases = {
            ("a5"),
            ("asdpokf"),
            ("0d56f"),
        }
        for inp in cases:
            with self.subTest(inp = inp):
                obtenido = librito.ExtraerElementos(inp)
                self.assertEqual(obtenido, "{'title': 'Search INFORM.', 'subtitle': '', 'authors': '', 'publisher': 'Data Courier', 'publishedDate': '1986', 'description': '', 'pageCount': 362, 'categories': ''}")
       
if __name__ == "__main__":
    unittest.main()