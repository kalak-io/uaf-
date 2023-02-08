

def validate_filepath(filepath):
    try:
        open(filepath,'r')
        return True
    except IOError:
        try:
            open(filepath, 'w')
            return True
        except IOError:
            return False
