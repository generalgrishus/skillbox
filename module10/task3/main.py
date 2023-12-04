def validate(line, reg_good, reg_bad):
    tab = "\t" * 2
    try:
        if len(line.split()) < 3:
            raise IndexError
        name, email, age = line.split()
        if not name.isalpha():
            raise NameError
        if not "@" in email and not "." in email:
            raise SyntaxError
        if 10 < int(age) > 99:
            raise ValueError
    except IndexError:
        reg_bad.write(f'{line.rstrip()}{tab}НЕ присутствуют все три поля\n')
    except NameError:
        reg_bad.write(f'{line.rstrip()}{tab}Поле «Имя» содержит НЕ только буквы\n')
    except SyntaxError:
        reg_bad.write(f'{line.rstrip()}{tab}Поле «Имейл» НЕ содержит @ и точку\n')
    except ValueError:
        reg_bad.write(f'{line.rstrip()}{tab}Поле «Возраст» НЕ представляет число от 10 до 99\n')
    else:
        reg_good.write(line)


with (open("registrations.txt", 'r', encoding="utf8") as reg_file,
      open("registrations_bad.log", "w", encoding="utf") as good_file,
      open("registrations_good.log", "w", encoding="utf8") as bad_file):
    for file_line in reg_file:
        validate(file_line, bad_file, good_file)