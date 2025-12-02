import random

countries = {
    "Georgia": "Tbilisi",
    "Russia": "Moscow",
    "Japan": "Tokyo",
    "Brazil": "Brasilia",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Egypt": "Cairo",
    "Armenia": "Yerevan",
    "Turkey": "Ankara"
}

leaderboard = []

def welcome_message():
    print("welcome, this is a country guessing name")
    print("you will be asked for capitals cities of countries.")
    print("try to get correct as many as possible\n")


def get_random_country(avaliable_countries):
    return random.choice(avaliable_countries)

def play_game():
    correct = 0
    incorrect = 0
    avaliable_countries = list(countries.keys())

    while avaliable_countries:
        country = get_random_country(avaliable_countries)
        capital = countries[country]
        answer = input(f"what country has the capital city '{capital}'? ").strip()

        if answer.lower() == country.lower():
            print("congrats its right\n")
            correct += 1
        else:
            print(f"incorrect , correct answer is  '{country}'.\n")
            incorrect += 1

        avaliable_countries.remove(country)

    print(f"game over your score: {correct} correct, {incorrect} incorrect.\n")
    return correct


if __name__ == "__main__":
    welcome_message()
    name = input("Enter your name: ").strip()
    play_game()

