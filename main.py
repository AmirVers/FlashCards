from Card import Card
from Deck import Deck
from Storage import DATA_PATH, load_data, save_data


def main():
    while True:
        data = load_data(DATA_PATH)
        decks = [Deck.fromDict(d) for d in data.get("decks", [])]
        print("\n === Добро пожаловать в FLASHCARDS 🦸🏻‍♂️")
        print("1 - Показать все колоды")
        print("2 - Добавить колоду")
        print("3 - Выбрать колоду")
        print("4 - Сохранить и выйти")

        choice = int(input("Ваш выбор: "))

        if choice == 1:
            if not len(decks):
                print("Пустая колода")
                continue
            for idx, val in enumerate(decks):
                print(f"{idx + 1} - {val.title}")

        elif choice == 2:
            title = input("Название колоды: ")
            decks.append(Deck(title))
            save_data(DATA_PATH, {"decks": [deck.toDict() for deck in decks]})
            print("✅ Успешно добавлено")

        elif choice == 3:
            for idx, val in enumerate(decks):
                print(f"{idx + 1} - {val.title}")
            try:
                idx = int(input("Выберите номер колоды: ")) - 1
                if 0 <= idx < len(decks):
                    deck_menu(decks[idx], decks)
                else:
                    print("Введите доступный индекс")
            except ValueError:
                print("Введите число.")

        elif choice == 4:
            save_data(DATA_PATH, {"decks": [deck.toDict() for deck in decks]})
            print("Все успешно сохранено, досвидания 👋🏻")
            break


def deck_menu(deck, decks):
    while True:
        print("1 - Показать все карточки")
        print("2 - Добавить новую карточку")
        print("3 - Тренироваться")
        print("4 - Выйти")

        choice = int(input("Ваш выбор: "))

        if choice == 1:
            if not deck.cards:
                print("Пустая колода, добавьте что нибудь 💬")
            else:
                for idx, val in enumerate(deck.cards):
                    print(
                        f"Question {idx + 1}: {val.question}, Answer: {val.answer}, Success rate: {val.success_rate}"
                    )

        elif choice == 2:
            new_q = input("Введите вопрос: ")
            new_a = input("Введите ответ: ")
            deck.addCard(new_q, new_a)
            save_data(DATA_PATH, {"decks": [deck.toDict() for deck in decks]})
            print("✅ Успешно добавлена карта")

        elif choice == 3:
            deck.train()
            save_data(DATA_PATH, {"decks": [deck.toDict() for deck in decks]})

        elif choice == 4:
            break

        else:
            print("Выберите одно из доступных вариантов")


if __name__ == "__main__":
    main()
