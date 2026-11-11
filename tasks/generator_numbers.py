from typing import Callable

def generator_numbers(text: str):
    """Extracts profits from text file (provided as real numbers separated by whitespaces from both sides)"""
    import re
    # starting position for search
    pos = 0
    while pos < len(text)-1:
        # search first occurance of profit number in substring
        match = re.search(r'\s\d+\.\d{2}\s', text[pos:])
        if match is None:
            break
        # if there's a match
        # move cursor to the end of the match
        pos += match.end()
        # return profit
        yield match.group()

def sum_profit(text: str, func: Callable):
    """uses generator to process text, extract profits and calculate sum profit"""
    from decimal import Decimal

    profit_sum = Decimal("0.00")
    for profit in generator_numbers(text):
        profit_sum += Decimal(profit).quantize(Decimal("0.00"))
    return profit_sum

if __name__ == "__main__":
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
