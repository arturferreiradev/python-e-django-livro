# Exemplos de uso de lower() e upper()

print('Chamando a partir da própria classe:')

print('str.lower(\'AEIOU\') = %s' % str.lower('AEIOU'))

print('str.lower(\'aEiOu\') = %s' % str.lower('aEiOu'))

print('str.lower(\'AeIoU\') = %s' % str.lower('AeIoU'))

print('str.upper(\'aeiou\') = %s' % str.upper('aeiou'))

print('str.upper(\'aEiOu\') = %s' % str.upper('aEiOu'))

print('str.upper(\'AeIoU\') = %s' % str.upper('AeIoU'))

print('Chamando a partir de uma instância da classe:')

print('\'AEIOU\'.lower() = %s' % 'AEIOU'.lower())

print('\'aEiOu\'.lower() = %s' % 'aEiOu'.lower())

print('\'AeIoU\'.lower() = %s' % 'AeIoU'.lower())

print('\'aeiou\'.upper() = %s' % 'aeiou'.upper())

print('\'aEiOu\'.upper() = %s' % 'aEiOu'.upper())

print('\'AeIoU\'.upper() = %s' % 'AeIoU'.upper())