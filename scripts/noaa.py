""" A script that splits bands in noaa file to individual files and 
recenters a worldwide ASCII grid from [0,360] to [-180,180] """
from sys import argv

import gdal
import osgeo
from subprocess import call

def do_bands(inFile,outDir,count):
    for i in range(1,count+1):
        cmd = "gdal_translate -b %d -of AAIGrid" % i
        cmd += " " + inFile + " "
        out = outDir + "/band%d" % i
        cmd += out
        print cmd
        call(cmd, shell=True)
        recenter(out)

def recenter(file):
    lines = open(file, 'r').read().split('\n')
    output = lines[:2]
    # shift xllcorner -180
    output.append("xllcorner    -180.000000000000")
    output.extend(lines[4:6])
    data = lines[6:]
    for row in data:
        values = filter(len, row.split(' '))
        results = values[72:] + values[0:72]
        out_row = ' '.join(results)
        output.append(out_row)
    out_string = '\n'.join(output)
    open(file, 'w').write(out_string)

if __name__ == '__main__':
    if len(argv) != 3:
        print 'Usage: python noaa.py <infile> <outdir>'
        exit(1)
    inFile = argv[1]
    outDir = argv[2]
    netcdf = osgeo.gdal.Open(inFile)
    count = netcdf.RasterCount
    do_bands(inFile,outDir,count)
