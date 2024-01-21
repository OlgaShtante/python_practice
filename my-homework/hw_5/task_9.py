def convert_nrzi_to_binary(nrzi_code):
    binary_code = ''
    previous_bit = '0'

    for symbol in nrzi_code:
        if symbol == '|':
            binary_code += previous_bit
        elif symbol in '¯_':
            previous_bit = '1' if previous_bit == '0' else '0'
            binary_code += previous_bit

    return binary_code

def convert_binary_to_int(binary_code):
    return int(binary_code, 2)

def format_output(nrzi_line, binary_code, line_sum):
    # formatting using f-strings, %, format
    print(f'NRZI: {nrzi_line}; binary: {binary_code}; integer: {line_sum}')
    print('NRZI: %s; binary: %s; integer: %s' % (nrzi_line, binary_code, line_sum))
    print('NRZI: {}; binary: {}; integer: {}'.format(nrzi_line, binary_code, line_sum))

def count_total_sum():
    nrzi_lines = [
        '|¯¯|_|¯¯¯¯¯|_|¯|_',
        '|¯¯¯¯¯¯|___|¯|___|¯',
        '|¯|_|¯|______|¯¯|_',
        '|¯|__|¯¯|___|¯|__|¯'
    ]

    total_sum = 0
    for nrzi_line in nrzi_lines:
        binary_code = convert_nrzi_to_binary(nrzi_line)
        line_sum = convert_binary_to_int(binary_code)
        total_sum += line_sum

        format_output(nrzi_line, binary_code, line_sum)

    # total sum formatting
    print(f'{total_sum}')
    print('%s' % total_sum)
    print('{}'.format(total_sum))

# call function to print formatted data
count_total_sum()