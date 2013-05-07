""" A script that recenters a worldwide ASCII grid from [0,360] to [-180,180] """
from sys import argv

if __name__ == '__main__':
    if len(argv) != 3:
        print 'Usage: python recenter.py <infile> <outfile>'
        exit(1)
    lines = open(argv[1], 'r').read().split('\n')
    output = lines[:6]
    data = lines[6:]
    for row in data:
        values = filter(len, row.split(' '))
        results = values[72:] + values[0:72]
        out_row = ' '.join(results)
        output.append(out_row)
    out_string = '\n'.join(output)
    open(argv[2], 'w').write(out_string)
        
