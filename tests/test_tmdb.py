import tmdb_client
import pytest
from unittest.mock import Mock


"""
# z tresci Modulu
def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w342'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url

# z tresci Modulu
def test_get_movies_list_type_popular():
   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list is not None

# z tresci Modulu
def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list
"""





def register_default_mock(monkeypatch):
   mock = Mock()
   monkeypatch.setattr("tmdb_client.requests.get", mock)
   return mock


def test_call_tmdb_api(monkeypatch):
   mock_endpoint = 'some'
   requests_mock = register_default_mock(monkeypatch)
   response = requests_mock.return_value
   response.json.return_value = mock_endpoint
   api = tmdb_client.call_tmdb_api(endpoint="movie/some")
   assert api == mock_endpoint


def test_get_single_movie(monkeypatch):
   mock_movie = 'Movie 666'
   requests_mock = register_default_mock(monkeypatch)
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   movie = tmdb_client.get_single_movie(movie_id=666)
   assert movie == mock_movie



def test_get_movie_images(monkeypatch):
   mock_movie = 'Movie 666'
   requests_mock = register_default_mock(monkeypatch)
   response = requests_mock.return_value
   response.json.return_value = mock_movie
   movie = tmdb_client.get_movie_images(movie_id=666)
   assert movie == mock_movie


def test_get_single_movie_cast(monkeypatch):
   mock_cast = {
                  'id': 666, 
                  'cast': 
                        [
                           {'adult': False, 'gender': 1, 'id': 10055, 'known_for_department': 'Acting', 'name': 'Fernanda Montenegro', 'original_name': 'Fernanda Montenegro', 'popularity': 0.899, 'profile_path': '/bja0rn1BjAnA5Z5VbEvL2apvMT5.jpg', 'cast_id': 29, 'character': 'Isadora "Dora" Teixeira', 'credit_id': '52fe4267c3a36847f801bb41', 'order': 0}, 
                           {'adult': False, 'gender': 2, 'id': 10059, 'known_for_department': 'Acting', 'name': 'Vinícius de Oliveira', 'original_name': 'Vinícius de Oliveira', 'popularity': 1.015, 'profile_path': '/eDMbfBmAZoT24vTbv0ecpC2MRnH.jpg', 'cast_id': 31, 'character': 'Josué Fontenele de Paiva', 'credit_id': '52fe4267c3a36847f801bb49', 'order': 1}, 
                           {'adult': False, 'gender': 1, 'id': 10057, 'known_for_department': 'Acting', 'name': 'Marília Pêra', 'original_name': 'Marília Pêra', 'popularity': 1.133, 'profile_path': '/9gxyrjoTlBPjEp6SnISeFU4hVMs.jpg', 'cast_id': 30, 'character': 'Irene', 'credit_id': '52fe4267c3a36847f801bb45', 'order': 2}, 
                           {'adult': False, 'gender': 2, 'id': 10061, 'known_for_department': 'Acting', 'name': 'Othon Bastos', 'original_name': 'Othon Bastos', 'popularity': 1.693, 'profile_path': '/86uykdZHCr1Stzg0fmUeQwIlsnc.jpg', 'cast_id': 33, 'character': 'César', 'credit_id': '52fe4267c3a36847f801bb51', 'order': 3}, 
                           {'adult': False, 'gender': 2, 'id': 10062, 'known_for_department': 'Acting', 'name': 'Otávio Augusto', 'original_name': 'Otávio Augusto', 'popularity': 2.705, 'profile_path': '/b19b1hPh2IrAcvo1DAloVofHcq1.jpg', 'cast_id': 34, 'character': 'Pedrão', 'credit_id': '52fe4267c3a36847f801bb55', 'order': 4}, 
                           {'adult': False, 'gender': 2, 'id': 8600, 'known_for_department': 'Acting', 'name': 'Matheus Nachtergaele', 'original_name': 'Matheus Nachtergaele', 'popularity': 1.4, 'profile_path': '/c8w75b4TlLdXEnnpAgd4R22NDGY.jpg', 'cast_id': 36, 'character': 'Isaías Paiva', 'credit_id': '52fe4267c3a36847f801bb5d', 'order': 5}, 
                           {'adult': False, 'gender': 2, 'id': 52584, 'known_for_department': 'Acting', 'name': 'Caio Junqueira', 'original_name': 'Caio Junqueira', 'popularity': 0.6, 'profile_path': '/oO2ncA8EDcszRl4T3d82rPVRQ4w.jpg', 'cast_id': 50, 'character': 'Moisés Paiva', 'credit_id': '5785198ac3a3684f94005830', 'order': 6}, 
                           {'adult': False, 'gender': 1, 'id': 10063, 'known_for_department': 'Acting', 'name': 'Stela Freitas', 'original_name': 'Stela Freitas', 'popularity': 0.6, 'profile_path': '/wip6RvU9Up5zze4Tifwq8EIpdIw.jpg', 'cast_id': 35, 'character': 'Yolanda', 'credit_id': '52fe4267c3a36847f801bb59', 'order': 7}, 
                           {'adult': False, 'gender': 0, 'id': 55011, 'known_for_department': 'Acting', 'name': 'Maria Menezes', 'original_name': 'Maria Menezes', 'popularity': 1.38, 'profile_path': None, 'cast_id': 55, 'character': 'Waitress', 'credit_id': '57851bc192514137c20042cf', 'order': 8}, 
                           {'adult': False, 'gender': 2, 'id': 1337623, 'known_for_department': 'Acting', 'name': 'Sergio Kato', 'original_name': 'Sergio Kato', 'popularity': 1.286, 'profile_path': '/pL1S4OlYO9bHtE9xXrIwJIWooxh.jpg', 'cast_id': 58, 'character': "Dora's Client", 'credit_id': '57851ca4925141044a002852', 'order': 9}, 
                           {'adult': False, 'gender': 0, 'id': 10060, 'known_for_department': 'Acting', 'name': 'Soia Lira', 'original_name': 'Soia Lira', 'popularity': 0.6, 'profile_path': '/omMVXaJv8DgkdpAl1JLKLZ9QhE8.jpg', 'cast_id': 32, 'character': 'Ana Fontenele', 'credit_id': '52fe4267c3a36847f801bb4d', 'order': 10}, 
                           {'adult': False, 'gender': 0, 'id': 933139, 'known_for_department': 'Acting', 'name': 'Rita Assemany', 'original_name': 'Rita Assemany', 'popularity': 0.652, 'profile_path': '/Aqsplr60u1QubIK7JCpZqTMnNQA.jpg', 'cast_id': 51, 'character': "Jessé's Wife", 'credit_id': '57851a09c3a3685ae0004e99', 'order': 11}, 
                           {'adult': False, 'gender': 2, 'id': 55010, 'known_for_department': 'Acting', 'name': 'Harildo Deda', 'original_name': 'Harildo Deda', 'popularity': 0.6, 'profile_path': '/2hDKyomCoT2nrtmKnjhLBTR61lI.jpg', 'cast_id': 52, 'character': 'Bené', 'credit_id': '57851a71c3a36867910029d9', 'order': 12}, 
                           {'adult': False, 'gender': 0, 'id': 1511425, 'known_for_department': 'Acting', 'name': 'Gildásio Leite', 'original_name': 'Gildásio Leite', 'popularity': 0.6, 'profile_path': None, 'cast_id': 53, 'character': 'Man in the bus', 'credit_id': '57851ad892514137c2004265', 'order': 13}, 
                           {'adult': False, 'gender': 0, 'id': 1364415, 'known_for_department': 'Acting', 'name': 'Nanego Lira', 'original_name': 'Nanego Lira', 'popularity': 0.6, 'profile_path': '/qqjgCJgVFhkDHmnC7TYyFGzpZU4.jpg', 'cast_id': 54, 'character': 'Nordeste preacher', 'credit_id': '57851b13c3a36857d9005022', 'order': 14}, 
                           {'adult': False, 'gender': 2, 'id': 1331384, 'known_for_department': 'Art', 'name': 'José Pereira da Silva', 'original_name': 'José Pereira da Silva', 'popularity': 0.6, 'profile_path': None, 'cast_id': 56, 'character': "Dora's Client", 'credit_id': '57851c2dc3a3684ef7005d41', 'order': 15}, 
                           {'adult': False, 'gender': 0, 'id': 230171, 'known_for_department': 'Acting', 'name': 'Everaldo Pontes', 'original_name': 'Everaldo Pontes', 'popularity': 0.6, 'profile_path': '/jGYjtd1Iez626GzWBkULNpKhuHD.jpg', 'cast_id': 57, 'character': "Dora's Client", 'credit_id': '57851c51c3a36820130017fd', 'order': 16}, 
                           {'adult': False, 'gender': 0, 'id': 1415432, 'known_for_department': 'Acting', 'name': 'Inaldo Santana', 'original_name': 'Inaldo Santana', 'popularity': 0.6, 'profile_path': None, 'cast_id': 59, 'character': "Dora's Client in Nordeste", 'credit_id': '57851cdcc3a36857d900513b', 'order': 17}, 
                           {'adult': False, 'gender': 0, 'id': 1200357, 'known_for_department': 'Acting', 'name': 'Gideon Rosa', 'original_name': 'Gideon Rosa', 'popularity': 0.6, 'profile_path': None, 'cast_id': 60, 'character': 'Jessé', 'credit_id': '57851d50c3a3685ae0005094', 'order': 18}, 
                           {'adult': False, 'gender': 0, 'id': 2375801, 'known_for_department': 'Acting', 'name': 'Antonieta Noronha', 'original_name': 'Antonieta Noronha', 'popularity': 0.6, 'profile_path': '/tdfYsuKvj4VfNNosLRx8nE8FXEK.jpg', 'cast_id': 63, 'character': 'Violeta', 'credit_id': '5d42650f7719d7001162905e', 'order': 19}
                        ]
               }

   requests_mock = Mock()
   requests_mock.return_value = mock_cast
   monkeypatch.setattr("tmdb_client.call_tmdb_api", requests_mock)
   assert tmdb_client.get_single_movie_cast(movie_id=666)



if __name__ == '__main__':
    pytest.main()