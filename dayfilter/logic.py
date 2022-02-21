def logic_daytime(inp):
    """
    Args:
        inp (tuple or list): (sr, ss, ds)

    Returns:
        bool: True or False
    """
    if inp[0] <= inp[2] < inp[1]:
        return True
    else:
        return False

def logic_nighttime(sr, ss, ds):
    """
    Args:
        inp (tuple or list): (sr, ss, ds)

    Returns:
        bool: True or False
    """
    if inp[0] <= inp[2] < inp[1]:
        return False
    else:
        return True
