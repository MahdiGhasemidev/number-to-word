
from constance import ABOVE_100, TENS, UNDER_TWENTY


def number_to_word(number:int) -> str:
    """ return number to word format

    :param number: number you want in word format
    :type number: int
    :return: number in word
    :rtype: str
    """
    if number < 20 :
        return UNDER_TWENTY[number]
    if number < 100 :
        reminder = number % 10
        num = number // 10-2 #! Because Tens list  starts from Twenty!
        return TENS[num] + ("" if reminder == 0 else " " + UNDER_TWENTY[reminder])

    #* 140
    #* 140 % 100 = 100
    #* 40 -> return number_to_word()
    #* 1380?
    #? 1380 % 1000
    pivot = max([key for key in ABOVE_100 if key <= number]) #! exp: number = 123, pivot = 100
    remaind = number % pivot
    p1 = number_to_word(number // pivot) #! exp: number = 123, p1=num_to_word(123//100) -> p1 = num_to_word(1)
    p2 = ABOVE_100[pivot]
    if remaind == 0:
        return f" {p1} {p2}"

    return f"{p1} {p2} {number_to_word(number % pivot)}"


if __name__ == "__main__":
    # assert number_to_word(100) == 'One Hundered'
    number = int(input("Enter a Number : "))

    if number >=0 and number <= 999_999_999_999:
        print(number_to_word(number))
    else:
        print(f"'{number}' is out of range!!!")
