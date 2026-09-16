import re
def normalize_phone(phone_number):
    step1 = phone_number.strip()
    step2 = re.sub(r"[^\d+]", "", step1)



    if step2.startswith("380"):
        step2 = "+" + step2

    elif not step2.startswith("+"):
        step2 = "+38" + step2
    print(step2)
    return step2
    #pattern1 = r"[;,\-:!\.\(\)A-Za-z]"
    #replacement = ""
    #stepremovesymbols = re.sub(pattern1, replacement, step1)
    #stepremovespaces = re.sub(" ", "", stepremovesymbols)
   
    #if len(stepremovespaces) <= 10 and !(stepremovespaces.startswith("380")):
     #   stepremovespaces = "+38" + stepremovespaces
    #if stepremovespaces[0] != "+":
    #    stepremovespaces = "+" + stepremovespaces
    


#normalize_phone("    +38(050)123-32-34")
#normalize_phone("     0503451234")
#normalize_phone("(050)8889900")
#normalize_phone("38050-111-22-22")
#normalize_phone("38050 111 22 11   ")

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
