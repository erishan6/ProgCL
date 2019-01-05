# -*- coding: utf-8 -*-

number_system = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 10 ** (3 * 1),
    'million': 10 ** (3 * 2),
    'billion': 10 ** (3 * 3),
    'trillion': 10 ** (3 * 4),
    'quadrillion': 10 ** (3 * 5),
    'quintillion': 10 ** (3 * 6),
    'sextillion': 10 ** (3 * 7),
    'septillion': 10 ** (3 * 8),
    'octillion': 10 ** (3 * 9),
    'nonillion': 10 ** (3 * 10),
    'decillion': 10 ** (3 * 11)
}


def number_formation(number_words):
    numbers = []
    for number_word in number_words:
        numbers.append(number_system[number_word])
    if len(numbers) == 4:
        return (numbers[0] * numbers[1]) + numbers[2] + numbers[3]
    elif len(numbers) == 3:
        return numbers[0] * numbers[1] + numbers[2]
    elif len(numbers) == 2:
        if 100 in numbers:
            return numbers[0] * numbers[1]
        else:
            return numbers[0] + numbers[1]
    else:
        return numbers[0]


def word_to_num(number_sentence):
    number_sentence = number_sentence.replace('-', ' ').replace(',', ' ')
    number_sentence = number_sentence.lower()

    split_words = number_sentence.strip().split()

    clean_numbers = []

    for word in split_words:
        if word in number_system:
            clean_numbers.append(word)

    bignumber_dict = {}
    bignumber_dict['decillion'] = clean_numbers.index('decillion') if 'decillion' in clean_numbers else -1
    bignumber_dict['nonillion'] = clean_numbers.index('nonillion') if 'nonillion' in clean_numbers else -1
    bignumber_dict['octillion'] = clean_numbers.index('octillion') if 'octillion' in clean_numbers else -1
    bignumber_dict['septillion'] = clean_numbers.index('septillion') if 'septillion' in clean_numbers else -1
    bignumber_dict['sextillion'] = clean_numbers.index('sextillion') if 'sextillion' in clean_numbers else -1
    bignumber_dict['quintillion'] = clean_numbers.index('quintillion') if 'quintillion' in clean_numbers else -1
    bignumber_dict['quadrillion'] = clean_numbers.index('quadrillion') if 'quadrillion' in clean_numbers else -1
    bignumber_dict['trillion'] = clean_numbers.index('trillion') if 'trillion' in clean_numbers else -1
    bignumber_dict['billion'] = clean_numbers.index('billion') if 'billion' in clean_numbers else -1
    bignumber_dict['million'] = clean_numbers.index('million') if 'million' in clean_numbers else -1
    bignumber_dict['thousand'] = clean_numbers.index('thousand') if 'thousand' in clean_numbers else -1
    # print(bignumber_dict)

    total_sum = 0

    if len(clean_numbers) > 0:
        if len(clean_numbers) == 1:
            total_sum += number_system[clean_numbers[0]]
        else:
            i = 0
            for number in bignumber_dict:
                if bignumber_dict[number] != -1:
                    multiplier = number_formation(clean_numbers[i:bignumber_dict[number]])
                    total_sum += multiplier * number_system[number]
                    i = bignumber_dict[number] + 1
            hundreds = number_formation(clean_numbers[i:])

            total_sum += hundreds

    return total_sum


if __name__ == '__main__':
    print(word_to_num('fourteen trillion, five hundred sixty-two billion , eleven million sixty-seven'))
    print(word_to_num('fifty-five'))
