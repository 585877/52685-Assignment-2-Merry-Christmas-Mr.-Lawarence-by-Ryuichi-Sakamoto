note_list = [ [[84,79,77]],                                 # measure 1           F 9 major
          [[83,81,79,77]],                               # measure 2           G 9 major
          [[83,81,79,76]],                               # measure 3           E 9 minor
          [[79,76,69],[76,72,71,67]],                      # measure 4          A 7 minor 转 A 9 minor
          [[84,79,77]],                                   # measure 5          F 9 major
          [[83,79,77]],                                   # measure 6          G 7 major
          [[83,81,79,76]],                                # measure 7          E 9 minor
          [[79,76,69]],                                   # measure 8          A 7 minor
          [[76,72,67,65]],                                # measure 9          F 9 major
          [[76,71,67,65]],                                # measure 10         E 9 minor
          [[74,71,67,64]],                                # measure 11         C 9 major
          [[76,72,71,69],[76,72,71,67]],                   # measure 12         A 9 minor
          [[76,72,67,65]],                                 # measure 13         F 9 major
          [[76,71,67,65]],                                 # measure 14         E 9 minor
          [[74,71,67,64]],                                # measure 15          E 7 minor
          [[72,69,67,64]],                                # measure 16          G 9 major
          [[48,41]],                                      # measure 17          D 7 minor
          [[53,43]],                                      # measure 18          G 9 major
          [45,52,55],                                 # measure 19          A 7 minor 
          [45,57,55,[52,43]],                          # measure 20          A minor 转 E minor 
          [[48,41]],                                      # measure 21          D 7 minor
          [[53,43]],                                      # measure 22          G 9 major
          [45,52,[55,48]],                              # measure 23          A 7 minor
          [[55,48],[50,47,43]]]                            # measure 24         A 7 minor 转 E 7 minor
 
beat_list = [ [6],                     # measure 1
          [6],                     # measure 2
          [6],                     # measure 3
          [3,3],                  # measure 4
          [6],                     # measure 5
          [6],                     # measure 6
          [6],                     # measure 7
          [6],                     # measure 8
          [6],                     # measure 9
          [6],                     # measure 10
          [6],                     # measure 11
          [3,3],                  # measure 12
          [6],                     # measure 13
          [6],                     # measure 14
          [6],                     # measure 15
          [6],                     # measure 16
       [4],                           # measure 17
       [4],                           # measure 18
       [1,1,2],                     # measure 19
       [1,1,1,1],                  # measure 20
       [4],                           # measure 21
       [4],                           # measure 22
       [1,1,2],                     # measure 23
       [2,2]]                      # measure 24

for measure in range(len(note_list)):
    for note, beat in zip(note_list[measure], beat_list[measure]):
        playNote(note, beat)