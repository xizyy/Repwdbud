import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(epilog='\tExample: \r\npython ' + sys.argv[0] + " -d jd -c jingdong -o out.txt")
    #parser.add_argument("-d", "--domain",  help="The domain...example: jd")
    parser.add_argument("-c", "--company", help="The company...example: jingdong")
    #parser.add_argument("-e", "--element", help="Anyother element ,Add common name + top/birth...") 
    parser.add_argument("-o", "--outfile", default="result.txt",help="Output file name")
    parser.add_argument("-l", "--level", type=int,default=1,help="The num of password...1(7k)/2(2w)/3(4w)")
    return parser.parse_args()

