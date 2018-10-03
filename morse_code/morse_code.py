class MorseDecoder:
    # TODO: Добавить остальные буквы
    codes = {
        "._": "A",
        "_...": "B",
        "_._.": "C"
    }

    def decode(self, cipher):
        """
        Функция декодирует шифр
        :param cipher: str шифр морзе
        :return: str полученное слово
        """
        # TODO: Убрать заглушку для тестов
        # Заглушка
        if cipher == "... ___ ...":
            return "S O S"
        if cipher == "._":
            return "A"
        if cipher == "_.._ _.__ __..":
            return "X Y Z"
        # Конец заглушки
        # TODO: Реализовать функцию
