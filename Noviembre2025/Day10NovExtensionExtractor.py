def get_extension(filename):
    file = filename.split('.')
    if len(file) > 1:
        extension = ''.join(file[-1:])
        if extension == '':
            return "none"
        print(extension)
    return "none"
get_extension("final.draft.")