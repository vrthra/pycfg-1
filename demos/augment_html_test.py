'''Augment a grammar and print it as HTML to stdout.'''

import cfg.core, cfg.slr

CFG = cfg.core.ContextFreeGrammar

G = CFG('''
E -> E+T | T
T -> T*F | F
F -> (E) | a
''')

print '<h1><var>G</var>:</h1>'
print G.html()
print '<h1><var>G&prime;</var>:</h1>'
print cfg.slr.augmented(G).html()

