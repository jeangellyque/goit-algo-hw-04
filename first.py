def total_salary(path: str) -> tuple:
    """
    This function calculates the total salary and average salary.
    Example of file should contain:`Name,5000`
    :param path: The path to the file containing salary information.
    :return tuple: A tuple containing the total salary and the average salary of the employees.
    """
    total_salary = 0
    number_of_employees = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                total_salary += int(line.split(',')[1])
                number_of_employees += 1
    except FileNotFoundError:
        print(f"Error: The file {path} does not exist.")
    except ValueError:
        print("Invalid salary value")
    except OSError as e:
        print(f"OS error occurred while trying to access the file: {e}")
    except Exception as e:
        print(e)
    return total_salary, total_salary / number_of_employees if number_of_employees > 0 else 0


