import os
import sys
from colorama import Fore
import src.factor2 as fa2
import src.parseArgs as pa

banner = '''
      ___         ___                                       ___                   
     /\  \       /\  \         _____         _____         /\  \         _____    
    /::\  \     _\:\  \       /::\  \       /::\  \        \:\  \       /::\  \   
   /:/\:\__\   /\ \:\  \     /:/\:\  \     /:/\:\  \        \:\  \     /:/\:\  \  
  /:/ /:/  /  _\:\ \:\  \   /:/  \:\__\   /:/ /::\__\   ___  \:\  \   /:/  \:\__\ 
 /:/_/:/  /  /\ \:\ \:\__\ /:/__/ \:|__| /:/_/:/\:|__| /\  \  \:\__\ /:/__/ \:|__|
 \:\/:/  /   \:\ \:\/:/  / \:\  \ /:/  / \:\/:/ /:/  / \:\  \ /:/  / \:\  \ /:/  /
  \::/__/     \:\ \::/  /   \:\  /:/  /   \::/_/:/  /   \:\  /:/  /   \:\  /:/  / 
   \:\  \      \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /     \:\/:/  /  
    \:\__\      \::/  /       \::/  /       \::/  /       \::/  /       \::/  /   
     \/__/       \/__/         \/__/         \/__/         \/__/         \/__/    
'''
print(Fore.RED + banner)


# 通过stdout方式重定向输出，大幅度减少写入时间
def stdSave():
    f = open(str(pa.parse_args().outfile), "w+")
    sys.stdout = f
    seq = []
    if pa.parse_args().company != None:
        seq4 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence4()
        seq5 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence5()
        seq6 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence6()
        seq7 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence7()
        seq8 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence8()
        seq9 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence9()
        seq10 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence10()
        seq11 = fa2.Factor2(pa.parse_args().company,pa.parse_args().level).sequence11()
        seq = seq + seq4 + seq5 + seq6 +seq7 +seq8 +seq9 +seq10 +seq11
        seq = list(set(seq))
    for i in seq:
        print(i)


if __name__ == '__main__':
    print(Fore.WHITE)
    print('[-] Saving...')

    stdSave()
