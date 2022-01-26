def find_athlets(know_english, sportsmen, more_than_20_years):
    """
    Функция для отбора на соревнования
    :param know_english: список хорошо владебщих английским
    :param sportsmen: список спортсменов
    :param more_than_20_years: список стедентов старше 20
    :return: список подходящих для соревнования
    """
    return [student for student in know_english if student in sportsmen and student in more_than_20_years]


if __name__ == "__main__":
    know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
    sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
    more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]
    print(find_athlets(know_english, sportsmen, more_than_20_years))
