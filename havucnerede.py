import random
from termcolor import colored

print(
    colored('''
    Oyunculaarrrr!!! 
    
    Havuç hangi kutuda oyununa hoşgeldiniz.                
                
    Oyun başladiğinda her ikinizin birer kutusu olacak.
    İçinizden seçeceğim birisine diğerinin gözleri kapali iken kutusunun içini göstereceğim.
    Sonra diğer oyuncu tahminde bulunacak. 
    Havuç o kutunun içinde mi yoksa arkadaşi kutularin yerini değiştirmiş olabilir mi?
    
    ''',
            'yellow',
            attrs=['bold'])
)  

input('Başlamak için bir tuşa basiniz')


first_player = input(
    colored('İlk oyuncu. Bana adini söyler misin? ', 'magenta'))
second_player = input(
    colored('Şimdi de gizemli arkadaşin bana adini behşeder mi lütfen? ',
            'cyan'))


player_names = first_player[:5] + '|.........X.........|' + second_player[:5]
print(player_names)

left_box_closed = colored(
    '''
 _________ 
/        /| 
+-------+ |
|   {}   | |
|       | /
+-------+/
''', 'magenta')

right_box_closed = colored(
    '''
                 _________ 
                /        /|
                +-------+ |
                |   {}   | |
                |       | /
                +-------+/
''', 'cyan')

left_box_full = colored(
    '''
  __VV___ 
 |  VV   |
 |__||___| 
/   ||   /| 
+-------+ |
|   {}   | |
|       | /
+-------+/
    ''', 'magenta')

left_box_empty = colored(
    '''
  _______ 
 |       |
 |_______| 
/        /| 
+-------+ |
|  {}    | |
|       | /
+-------+/
    ''', 'magenta')

right_box_full = colored(
    '''
                  __VV___ 
                 |  VV   |
                 |__||___| 
                /   ||   /| 
                +-------+ |
                |  {}    | |
                |       | /
                +-------+/
    ''', 'cyan')

right_box_empty = colored(
    '''
                  _______ 
                 |       |
                 |_______| 
                /        /| 
                +-------+ |
                |  {}    | |
                |       | /
                +-------+/
    ''', 'cyan')

print(left_box_closed.format('A') + right_box_closed.format('B'))


print('''
    Oyuncu {p1}. Soldaki A kutusu senin.
        
    Oyuncu {p2}. Tahmin edeceğin üzere sağdaki B kutusu da senin.    
    ve şimdi gözlerini kapamalisin.
    Sakin açma haaa!!!
    Oyuncu {p1}. Arkadaşinin bakmadiğindan emin olduktan sonra bir tuşa bas.
    
'''.format(p1=first_player.upper(), p2=second_player.upper()))
input()



state = random.randint(1, 2)


carrot_in_left_box = state == 1


if state == 1:
    print(left_box_full.format('A'), right_box_closed.format('B'))
else:
    print(left_box_empty.format('A'), right_box_closed.format('B'))

input(
    colored('Devam etmek için lütfen bir tuşa bas {}'.format(first_player),
            'magenta'))


print('\n' * 200)

print(
    colored(
        '''
    Oyuncu {p1}. Artik gizemli arkadaşin {p2} gözlerini açabilir.
    Oyuncu {p2}, sence arkadaşinin kutusunda havuç var mi? Bunu iyice bir düşün.
    Yeterince düşündün mü {p2}?
    Peki ya kutunu {p1} ile değiştirmek ister misin ;)
    Olur diyorsan E olmaz diyorsan H tuşla ve enter'a bas.
'''.format(p1=first_player.upper(), p2=second_player.upper()), 'green'))


while True:
    p2_response = input('..:').upper()
    if not (p2_response == 'E' or p2_response == 'H'):
        print(second_player + ' Lütfen Evet için E, hayir için H yaz')
    else:
        break

print(
    colored(
        '''
    
    İşte sonuçlar :)
    Sonuçlar için lütfen bir tuşa basin.
    \a
''', 'blue'))
input()


if p2_response == 'E':
    left_box_full, right_box_empty = right_box_full, left_box_empty  

if carrot_in_left_box:
    print(left_box_full.format('A'), right_box_empty.format('B'))
else:
    print(right_box_full.format('B'), left_box_empty.format('A'))

print('Oynadiğiniz için teşekkürler :) Görüşmek üzere') 