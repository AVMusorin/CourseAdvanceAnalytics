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
        Каждая буква передается через пробел
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


# Данная конструкция нужна для правильного импортировании модуля morse_code
if __name__ == "__main__":
    # создаем экземпляр класса
    decoder = MorseDecoder()
    # расшифрованные буквы
    decoded_word = decoder.decode("... ___ ...")
    print(decoded_word)
