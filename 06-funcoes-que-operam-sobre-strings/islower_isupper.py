# Exemplos de uso de islower() e isupper()

print('Chamando a partir da propria classe:')

print('str.islower(\'AEIOU\') = %s' % str.islower('AEIOU'))

print('str.islower(\'aEiOu\') = %s' % str.islower('aEiOu'))

print('str.islower(\'AeIoU\') = %s' % str.islower('AeIoU'))

print('str.islower(\'aeiou\') = %s' % str.islower('aeiou'))

print('str.isupper(\'AEIOU\') = %s' % str.isupper('AEIOU'))

print('str.isupper(\'aEiOu\') = %s' % str.isupper('aEiOu'))

print('str.isupper(\'AeIoU\') = %s' % str.isupper('AeIoU'))

print('str.isupper(\'aeiou\') = %s' % str.isupper('aeiou'))

print('Chamando a partir de uma instância da classe:')

print('\'AEIOU\'.islower() = %s' % 'AEIOU'.islower())

print('\'aEiOu\'.islower() = %s' % 'aEiOu'.islower())

print('\'AeIoU\'.islower() = %s' % 'AeIoU'.islower())

print('\'aeiou\'.islower() = %s' % 'aeiou'.islower())

print('\'AEIOU\'.islower() = %s' % 'AEIOU'.isupper())

print('\'aEiOu\'.islower() = %s' % 'aEiOu'.isupper())

print('\'AeIoU\'.islower() = %s' % 'AeIoU'.isupper())

print('\'aeiou\'.islower() = %s' % 'aeiou'.isupper())