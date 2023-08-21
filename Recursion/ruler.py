def draw_line(tick_length, tick_label=''):
    """Draw one line with given tick length (followed by optional label)"""
    line = '-'* tick_length
    if tick_label:
        line += ' ' +tick_label
    print(line)

def draw_interval(center_length):
    """Draw tick interval based upon a central tick length."""
    if center_length>0:     # stop when length drops to 0
        draw_interval(center_length-1)  # recursively draw top ticks
        draw_line(center_length)  # draw center tick
        draw_interval(center_length-1) # recursively draw bottom ticks

def draw_ruler(num_inches, major_length):
    """Draw English ruler with given number of inches, major tick length."""
    draw_line(major_length, '0')  # draw the 0 line
    for j in range(1, 1+num_inches):
        draw_interval(major_length - 1)  # draw interior ticks
        draw_line(major_length, str(j))  # draw inch j and label

draw_ruler(4, 4)


def draw_cm_ruler(num_cm, major_length):
    def draw_small_ticks(tick):
        if tick == 4:
            return
        else:
            draw_line(1)
            draw_small_ticks(tick+1)

    for i in range(num_cm):
        draw_line(major_length, str(i))
        draw_small_ticks(0)
        draw_line(major_length-1)
        draw_small_ticks(0)
    draw_line(major_length, str(num_cm))

draw_cm_ruler(5, 3)