def find_athlets(know_english, sportsmen, more_than_20_years):
    return [student for student in know_english if student in sportsmen and student in more_than_20_years]


if __name__ == "__main__":
    know_english = ["Vasya", "Jimmy", "Max", "Peter", "Eric", "Zoi", "Felix"]
    sportsmen = ["Don", "Peter", "Eric", "Jimmy", "Mark"]
    more_than_20_years = ["Peter", "Julie", "Jimmy", "Mark", "Max"]
    print(find_athlets(know_english, sportsmen, more_than_20_years))
