#!/user/bin/env python3



def main():
    
  char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk ")
    
  char_stat = input(" What statistic do you want to know about? real name, powers, archenemy ")

  marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

  character = marvelchars.get(char_name)
  stats = character.get(char_stat)

  print(f"{char_name}'s {char_stat} is: {stats}")

        
main()
