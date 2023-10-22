# Úkol 0
# Jak se jmenuje druh chyby, která nastane, když…

1. Dáš uvozovky jen na jednu stranu řetězce?
>>> print('Ahoj)
SyntaxError: unterminated string literal 

2. Zkusíš odečíst číslo od řetězce?
>>> 'Ahoj' - 2
TypeError: unsupported operand type(s) for -: 'str' and 'int'

3. Dělíš nulou?
>>> 42 / 0
ZeroDivisionError: division by zero

4. Použiješ proměnnou, která neexistuje?
>>> b - 5
NameError: name 'b' is not defined

5. Stiskneš Ctrl+C, když se program ptá na vstup (pomocí input)?
KeyboardInterrupt

6. Odsadíš příkaz bez předchozího if:?
IndentationError: unexpected indent

7. Po if: odsadíš jeden příkaz o čtyři mezery a druhý jen o dvě?
IndentationError: unindent does not match any outer indentation level

8. Neuzavřeš závorku?
SyntaxError: '(' was never closed

9. Zkusíš použít vykřičník (!) jako operátor?
SyntaxError: invalid syntax

10. Napíšeš v příkazu print(1, 2, 3) čárku navíc? Např. print(1,2,,3)?
SyntaxError: invalid syntax 

11. Zkusíš porovnat řetězec a číslo, např. 2 >"3"?
TypeError: '>' not supported between instances of 'int' and 'str'