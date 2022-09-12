# Based Fighter's Game Design Document
## A dumb open source fighter game written in Python
This should be a living document, updated as needed.

# Characters
Start with character archetypes that should be in the game, then expand out from there.
## The Shoto (Ryu, Ken)
- Fireball (236+P)
- Dragon Punch (623+P)
- Tatsumaki (214+K)
## The Charger (Guile)
- Fireball (4[60f],6+P)
- Flash Kick (2[60f]+8K)
## The Grappler (Zangief)
- SPD (6248+P)[^SPD]
- Lariat (PPP or KKK)[^Lariat]

# Gameplay
First and foremost this is a fighting game. Fighting is its core.
## Style of fighting game
TODO:
- Decide if this is a 6 button or a 4 button fighter. Or go crazy and make characters have their own styles.
- Health System can be classic (like Street Fighter) or something else. Possible armor system?
- Timer? If so, how long, if not, how do we prevent games lasting too long
- Supers? Super bars?
- Unique mechanics or unique resources
- Comeback mechanic
- Traditional?[^Trad] Anime?[^Anime] Mortal Kombat?[^MK] Tekken?[^Tekken]

[^SPD]: This move is often listed as a 360° symbol in move lists. However, only the cardinal directions need to be pushed (2684) in Street Fighter style games and it doesn't matter what order they are pushed. 
  For example, the grappler can shimmy back and forth (6,4), crouch (2), jump(8), and punch (P) and the grab will come out.
[^Lariat]: This move should disable the grapplers hurtbox so she can approach will be walled out with fireballs.
  This can either be accomplished by completely removing the hurtbox or just making the hurtboxes immune to projectiles.
[^Trad]: Traditional fighters, like Street Fighter usually are more ground based fighters with holding back as the block.
  Holding down and back blocks lows and mids, but does not block overheads.
  Holding back while standing blocks mids and overheads, but not lows.
  Combo game is usually pretty short and consists of 3-7 hits on most characters (not counting multi hit moves like Special Moves)
[^Anime]: Anime fighters, like Dragonball FighterZ, usually have a lot of aerial combat. Mechanics like air dashing, air blocking, and air grabs, are very common
  Holding down and back blocks lows and mids, but does not block overheads.
  Holding back while standing blocks mids and overheads, but not lows.
  Combo game can often be incredibly long and complicated. (See https://youtu.be/mG_3hLCmzfo?t=240)
[^MK]: Mortal Kombat style games usually have a block button (as opposed to holding back), but usually follow the same format of high and lows blocking.
[^Tekken]: Tekken is kind of unique in the fact that their is much higher emphasis on High and Mid moves with Lows being less frequent and often very laggy
  Aerial combat is almost non existent
  Block can be done by either holding back or not doing anything