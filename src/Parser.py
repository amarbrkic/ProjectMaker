def parse(*args):
    validArguments = ['-file', '-output']
    validFlags = ['--help', '--version', '--verbose',
                  '--quiet', '--debug']
    validatingArguments(args, validArguments, validFlags)


def validatingArguments(*args, validArguments, validFlags):
    pass

def infoBox():
    pass