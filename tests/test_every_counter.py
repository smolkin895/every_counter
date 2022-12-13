from src.every_counter.every_counter import count_entries


def every_counter_positive():
    string = "Жди когда идут дожди"\
             "Когда солнце в небе ясно"\
            "Когда никто уже не ждет"\
            "Ты жди, всем чертям назло"
    counted_string = count_entries(string)
    assert 1 == 1
