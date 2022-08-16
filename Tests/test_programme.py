import pytest

from Tests.test_base import set_keyboard_input
from programme import check_document_existance, get_doc_owner_name, remove_doc_from_shelf, add_new_shelf, directories, \
    delete_doc

fixture_for_test_check_document_existance_good = [('2207 876234', True),
                                                  ('11-2', True),
                                                  ('10006', True),
                                                  ('54', False),
                                                  ('rgdg', False,),
                                                  ('-1', False)]


# тестирование функции по получению информации о документах
# тестирование наличия документа
@pytest.mark.parametrize('doc_number, expected_result', fixture_for_test_check_document_existance_good)
def test_check_document_existance_good(doc_number, expected_result):
    assert check_document_existance(doc_number) == expected_result


# тестирование получения имени владельца по номеру документа

fixture_for_test_get_doc_owner_name_good = [('2207 876234', 'Василий Гупкин'),
                                            ('10006', 'Аристарх Павлов')]


@pytest.mark.parametrize('doc_number, expected_result', fixture_for_test_get_doc_owner_name_good)
def test_get_doc_owner_name_good(doc_number, expected_result):
    set_keyboard_input([doc_number])
    assert get_doc_owner_name() == expected_result


fixture_for_test_get_doc_owner_name_bad = [(AssertionError, '2207 876234', 'Аристарх Павлов'),
                                           (AssertionError, '10006', 'Василий Гупкин'),
                                           (AssertionError, 'ytre', 'Аристарх Павлов'),
                                           (AssertionError, '11-2', 'Gtr ПАВ')]


@pytest.mark.parametrize('expected_exception, doc_number, expected_result', fixture_for_test_get_doc_owner_name_bad
                         )
def test_get_doc_owner_name_bad(expected_exception, doc_number, expected_result):
    with pytest.raises(expected_exception):
        set_keyboard_input([doc_number])
        assert get_doc_owner_name() == expected_result


# тестирование удаления документа с полки
# в функцию remove_doc_from_shelf() добавлена строка return directories вместо break

fixture_for_test_remove_doc_from_shelf_good = [('2207 876234', {
    '1': ['11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
})
                                               ]


@pytest.mark.parametrize('doc_number, expected_result', fixture_for_test_remove_doc_from_shelf_good)
def test_remove_doc_from_shelf_good(doc_number, expected_result):
    assert remove_doc_from_shelf(doc_number) == expected_result


@pytest.mark.parametrize('expected_exception, doc_number, expected_result',
                         [(AssertionError, '111', directories),
                          (AssertionError, 'erw', directories),
                          (AssertionError, '%$#', directories)
                          ])
def test_remove_doc_from_shelf_bad(expected_exception, doc_number, expected_result):
    directories
    assert remove_doc_from_shelf(doc_number) == expected_result


# тестирование добавления новой полки
fixture_for_test_add_new_shelf = [('4', {
    '1': ['11-2', '5455 028765'],
    '2': ['10006'],
    '3': [],
    '4': []
})
                                  ]


@pytest.mark.parametrize('shelf_number, expected_result', fixture_for_test_add_new_shelf)
def test_add_new_shelf(shelf_number, expected_result):
    assert add_new_shelf('4') == expected_result


# тестирование удаления документа
# в функцию delete_doc() добавлены строки     else: return False в цикл if doc_exists
fixture_for_test_delete_doc_good = [('10006', ('10006', True)),
                                    ('11-2', ('11-2', True))]


@pytest.mark.parametrize('doc_number, expected_result', fixture_for_test_delete_doc_good)
def test_delete_doc_good(doc_number, expected_result):
    set_keyboard_input([doc_number])
    assert delete_doc() == expected_result


fixture_for_test_delete_doc_bad = [(AssertionError, '111', False),
                                   (AssertionError, 'erw', False),
                                   (AssertionError, '%$#', False)
                                   ]


@pytest.mark.parametrize('expected_exception, doc_number, expected_result', fixture_for_test_delete_doc_bad)
def test_delete_doc_bad(expected_exception, doc_number, expected_result):
    set_keyboard_input([doc_number])
    assert delete_doc() == expected_result
