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
        new_list = []
        for i in cipher.split(" "):
            try:
                new_list.append(self.codes[i])
            except KeyError:
                print(f"Такого кода не существует {i}")
        return " ".join(new_list)

        # return " ".join([self.codes[i] for i in cipher.split(" ")])


# Данная конструкция нужна для правильного импортировании модуля morse_code
if __name__ == "__main__":
    # создаем экземпляр класса
    decoder = MorseDecoder()
    # расшифрованные буквы
    decoded_word = decoder.decode("._ _... ...._ ._")
    print(decoded_word)
