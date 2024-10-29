note_list = [ [88,86,88,93,88,86,88,86,88,93,88,86],         # measure 1
         [88,86,88,91,88,86,88,86,88,91,88,86],           # measure 2
          [86,84,86,91,86,84,86,84,84,91,86,84],           # measure 3
          [86,84,86,91,86,84,83,81,83,88,83,81],           # measure 4
         [88,86,88,93,88,86,88,86,88,93,88,86],           # measure 5
         [88,86,88,91,88,86,88,86,88,91,88,86],           # measure 6
         [86,84,86,95,86,84,91,84,84,95,86,84],           # measure 7
         [86,84,86,95,86,84,91,84,84,95,86,84],           # measure 8
         [88,86,88,[93,81],88,86,88,86,88,[93,81],88,86],      # measure 9
         [88,86,88,[91,79],88,86,88,86,88,[91,79],88,86],      # measure 10
         [86,84,86,[91,79],86,84,86,84,84,[91,79],86,84],      # measure 11
         [86,84,86,[91,79],86,84,83,81,83,[88,76],83,81],      # measure 12
         [88,86,88,[93,81],88,86,88,86,88,[93,81],88,86],      # measure 13
         [88,86,88,[91,79],88,86,88,86,88,[91,79],88,86],      # measure 14
         [86,84,86,95,86,84,91,84,84,95,86,84],           # measure 15
         [86,84,86,95,86,84,91,84,84,95],                   # measure 16
        [[62,57],64,62,57,62],                                      # measure 17
        [[62,57],62,64,62,64,67,64],                              # measure 18
        [62,64,62,57,60],                                         # measure 19
        [[73,64,60],[71,64,59],67,[64,59]],                              # measure 20
        [[62,57],64,62,57,62],                                     # measure 21
        [[62,57],62,64,62,64,67,64],                             # measure 22
        [62,64,62,60,57],                                        # measure 23
        [57,52] ]                                                     # measure 24
 
beat_list = [ [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 1
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 2
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 3
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 4
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 5
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 6
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 7
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 8
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 9
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 10
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 11
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 12
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 13
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 14
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 15
          [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5],          # measure 16
          [0.5,0.5,0.5,0.5,2],                                            # measure 17
          [1,0.5,0.5,0.5,0.5,0.5,0.5],                                        # measure 18
          [0.5,0.5,0.5,0.5,2],                                            # measure 19
          [0,1,0.5,0.5,1],                                   # measure 20
          [0.5,0.5,0.5,0.5,2],                                            # measure 21
          [1,0.5,0.5,0.5,0.5,0.5,0.5],                                        # measure 22
          [0.5,0.5,0.5,0.5,2],                                            # measure 23
          [2,2] ]                                                           # measure 24

for measure in range(len(note_list)):
    for note, beat in zip(note_list[measure], beat_list[measure]):
        playNote(note, beat)                                                                    