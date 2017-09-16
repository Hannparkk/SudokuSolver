def solve(solution, r_idx, c_idx):
    # fill options of numbers ranging 1-9
    for fill in range(1, 10):
        found = False
        # check the column
        for row in range(9):
            if solution [row][c_idx] == fill:
                found = True
                break
        # check the row
        for col in range(9):
            if solution[r_idx][col] == fill:
                found = True
                break
        # check the box
        box_row_spot = r_idx % 3
        box_col_spot = c_idx % 3
        for row in range(r_idx - box_row_spot, r_idx - box_row_spot + 3):
            for col in range(c_idx - box_col_spot, c_idx - box_col_spot + 3):
                if solution[row][col] == fill:
                    found = True
                    break
        # not found -> fill box and move on
        if found == False:
            solution [r_idx][col_idx] = fill
            next_r = r_idx
            next_c = c_idx
            while solution [next_r][next_c] != 0:
                 next_c = (next_c + 1) % 9
                 if next_c == 0:
                     next_r += 1
                     if next_r == 9:
                         return True
            ret = solve(solution, next_r, next_c)
            # we did it!
            if ret == True:
                return ret
            # else reset box to 0 and move on to try next fill options
            else:
                solution[r_idx][c_idx] = 0
    # none of the fill options worked -> messed up somewhere further back -> go to last box filled and retry
    if solution[r_idx][c_idx] == 0:
        return False
