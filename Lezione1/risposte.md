# Risposte - Pallina che rimbalza

## Domande di comprensione

1. **Cosa succede se rimuovi `screen.fill(BG_COLOR)`? Perché?**
   Se si toglie quella riga la pallina lascia una scia del suo stesso colore.

2. **Cosa succede se rimuovi `pygame.display.flip()`?**
   Non si vede più niente sullo schermo. Praticamente il computer disegna le cose ma senza questa istruzione non le fa vedere.

3. **Se `BALL_RADIUS = 30` e `SCREEN_W = 800`, qual è il valore massimo che `ball_x` può raggiungere prima del rimbalzo?**
   Il valore massimo è 770. Ho fatto semplicemente 800 (la larghezza) meno 30 (il raggio).

4. **La pallina si muove di 5 pixel per frame a 60 FPS. Quanti pixel percorre in un secondo? E in 10 secondi?**
   In un secondo fa 300 pixel, perché basta moltiplicare 5 per 60. In 10 secondi percorre 3000 pixel.

5. **Cosa succede se imposti `vel_x = 0`? E se imposti `vel_x = vel_y = 0`?**
   * Se metto `vel_x = 0`, la pallina si muove solo in verticale, andando su e giù senza mai spostarsi a destra o a sinistra.
   * Se metto a zero tutte e due, la pallina sta ferma immobile al centro dello schermo.

6. **Perché correggiamo la posizione (`ball_x = SCREEN_W - BALL_RADIUS`) oltre a invertire la velocità? Cosa succederebbe senza la correzione?**
   La correggiamo perché quando la pallina arriva sul bordo potrebbe essere già uscita un po' fuori dallo schermo. Se non aggiustiamo la posizione e le facciamo solo cambiare direzione, rischia di rimanere bloccata nel bordo e inizia a rimbalzare all'infinito su se stessa.

---

## Esperimenti

**Esperimento 1 — Velocità**
Ho provato a cambiare le velocità. Se metto valori uguali (tipo 5 e 5) la pallina si muove in diagonale dritta. Se invece metto la X a 20 e la Y a 2, la pallina va velocissima da una parete all'altra e in verticale si sposta pochissimo.

**Esperimento 2 — Dimensione**
Ho messo un raggio molto più grande (es. 400) e la pallina è diventata gigante. Per far sì che la pallina una volta ingandita non esca dallo schermo ho aumentato i valori di `SCREEN_W` e `SCREEN_H`.

**Esperimento 3 — Colore dinamico**
Prima di tutto all'inizio del codice ho scritto 'import random' poi ho incollato all'interno del blocco del rimbalzo BALL_COLOR = (random.randint(0,255), random.randint(0,255), random.randint(0,255)) per ogni if creato.

**Esperimento 4 — Gravità**
Ho aggiunto `GRAVITY = 0.3` e ho messo `vel_y += GRAVITY` nel codice. La pallina adesso cade verso il basso accelerando, come se cadesse per davvero. Ho notato che non torna alla stessa altezza di prima: ogni volta che rimbalza a terra perde un po' di quota, credo perché la gravità la spinge in giù di continuo.