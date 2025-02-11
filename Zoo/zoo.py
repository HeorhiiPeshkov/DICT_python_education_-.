print('I love animals!\nLets check out the animals...\nThe deer looks fine.\nThe lion looks healthy.')

animals = ["camel", "lion", "deer", "goose", "bat", "rabbit"]

camel = (r"""___.-''''-.
/___ @ |
',,,,. | _.'''''''._
' | / \
| \ _.-' \
| '.-' '-.
| ',
| '',
',,-, ':;
',,| ;,, ,' ;;
! ; !'',,,',',,,,'! ; ;:
: ; ! ! ! ! ; ; :;
; ; ! ! ! ! ; ; ;,
; ; ! ! ! ! ; ;
; ; ! ! ! ! ; ;
;,, !,! !,! ;,;
/_I L_I L_I /_I''''""")

lion = r"""The lion habitat...
,w.
,YWMMw ,M ,
_.---.._ ..---._.'MMMMMw,wMWmW,
_.-"" ''' YP"WMMMMMMMMMb,
.-' .' .' MMMMW^WMMMM;
_, .'.-'"; , / .--"" :MMM[==MWMW^;
,mM^" ,-'.' / ; ; / , MMMMb_wMW" @\
,MM:. .'.-' .' ; \ ; , MMMMMMMW "=./-,
WMMm__,-'.' / _.\ F'''-+,, ;_,_.dMMMMMMMM[,_ / `=_}
"^MP__.-' ,-' _.--"" `-, ; \ ; ;MMMMMMMMMMW^``; |
/ .' ; ; ) )`{ \ `"^W^`, \ :
/ .' / ( .' / Ww._ `. `"
/ Y, `, `-,=,_{ ; MMMP`""-, `-._.-,
(--, ) `,_ / `) \/"") ^" `-, -;"\:
The lion is roaring!"""

deer = r"""
The deer habitat...
/| |\
`__\\ //'

\__`\ |'/
`_\\ //_'
_.,:---;,._
\_: :_/
|@. .@|
| |
,\.-./ \
;;`-' `---__________-----.-.
;;; \_\
';;; |
; | ;
\ \ \ | /
\_, \ / \ |\
|';| |,,,,,,,,/ \ \ \_
| | | \ / |
\ \ | | / \ |
| || | | | | |
| || | | | | |
| || | | | | |
|_||_| |_| |_|
/_//_/ /_/ /_/
Pretty good!"""

goose = r"""
The goose habitat...

_
,-"" "".
,' ____ `.
,' ,' `. `._
(`. _..--.._ ,' ,' \ \
(`-.\ .-"" ""' / ( d _b
(`._ `-"" ,._ ( `-( \
<_ ` ( <`< \ `-._\
<`- (< < :
( (_<_< ;
`------------------------------------------
Beautiful!"""

bat = r"""
The bat habitat...
_________________ _________________
~-. \ |\___/| / .-~
~-. \ / o o \ / .-~
> \\ W // <
/ /~---~\ \
/_ | | _\
~-. | | .-~
; \ / i
/___ /\ /\ ___\
~-. / \_/ \ .-~
V V
It's doing fine."""

rabbit = r"""
The rabbit habitat...
,
/| 
/ | ,-~ /
Y :| // /
| jj /( .^
>-"~"-v"
/ Y
jo o |
( ~T~ j
>._-' _./
/ "~" |
Y _, |
/| ;-"~ _ l
/ l/ ,-"~ \
\//\/ .- \
Y / Y
l I !
]\ _\ /"\
(" ~----( ~ Y. )
It looks fine!"""

animalyw = int(input('Please enter the number of the habitat you would like to view:\n>'))
if animalyw in range(0, 5):
    animalyw = True
    while True:
        if animalyw == 0:
            print(camel)
        elif animalyw == 1:
            print(lion)
        elif animalyw == 2:
            print(deer)
        elif animalyw == 3:
            print(goose)
        elif animalyw == 4:
            print(bat)
        elif animalyw == 5:
            print(rabbit)
        elif animalyw == exit:
            print('See you later!')
        break