try:
  neco_udelej()
except ValueError:
  print('Tohle se provede, pokud nastane ValueError')
except NameError:
  print('Tohle se provede, pokud nastane NameError')
except Exception:
  print('Tohle se provede, pokud nastane jiná chyba')
  # (kromě SystemExit a KeyboardInterrupt, ty chytat nechceme)
except TypeError:
  print('Tohle se neprovede nikdy')
  # ("except Exception" výše ošetřuje i TypeError; sem se Python nedostane)
else:
  print('Tohle se provede, pokud chyba nenastane')
finally:
  print('Tohle se provede vždycky; i pokud v `try` bloku byl např. `return`')