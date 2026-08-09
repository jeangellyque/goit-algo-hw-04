def get_cats_info(path):
    result = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                if len(line.strip().split(',')) != 3:
                    print(f"Некоректний формат рядка у файлі: {line.strip()}")
                    continue
                id, name, age = line.strip().split(',')
                result.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"Файл не знайдено: {path}")
    except OSError:
        print(f"Помилка доступу до файлу: {path}")
    except Exception as error:
        print(f"ERROR: {error}")
    return result


if __name__ == "__main__":
    cats_path = "/Users/angelique/PycharmProjects/TechProject4/homework_2/cats.csv"
    print(f"Інформація про котів: {get_cats_info(cats_path)}")