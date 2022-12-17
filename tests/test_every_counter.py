from collections import Counter

from src.every_counter.every_counter import count_entries


def test_every_counter_positive():
    expected_result = Counter({'Когда': 2, 'Жди': 1,
                       'когда': 1, 'идут': 1,
                       'дожди': 1, 'солнце': 1,
                       'в': 1, 'небе': 1, 'ясно': 1,
                       'никто': 1, 'уже': 1, 'не': 1,
                       'ждет': 1, 'Ты': 1, 'жди': 1,
                       'всем': 1, 'чертям': 1, 'назло': 1})
    string = "Жди когда идут дожди "\
             "Когда солнце в небе ясно "\
            "Когда никто уже не ждет "\
            "Ты жди, всем чертям назло "
    counted_string = count_entries(string)
    assert expected_result == counted_string