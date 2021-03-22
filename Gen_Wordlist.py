import os
import sys
import string
import argparse
import itertools
from datetime import datetime
print (' CyberGhost Wordlist Generator')
def wordlist(chrs, min_length, max_length, output):
    if min_length > max_length:
        print("[+] min_length value Should be small or same as max_length")
        sys.exit()

    if os.path.exists(os.path.dirname(output)) == False:
        os.makedirs(os.path.dirname(output))

    print("\033[96m")
    print("[+] creating a wordist at %s " %output)
    start_time = datetime.now()
    print("\033[92m")
    print ('[+] Starting at : %s' % start_time)
    output = open(output,'w')

    for n in range(min_length, max_length+1):
        for xs in itertools.product(chrs, repeat=n):
            chars = ''.join(xs)
            output.write("%s\n" % chars)
            sys.stdout.write('\r[+] saving character `%s`' % chars)
            sys.stdout.flush()

    output.close()

    end_time = datetime.now()
    print("\033[93m")
    print ('\n[+] Ended at : %s' % end_time )	
    print ('\033[91m[+] Total Duration : {}\n'.format(end_time - start_time))            
    print("\033[36m Check your output on default location or on your entered location")    

    
        
    

def main():
    parser = argparse.ArgumentParser(description='CyberGhost Wordlist Generator')
    parser.add_argument('-chr','--chars',default=None, help='characters to iterate')
    parser.add_argument('-min','--min_length', type=int,default=1, help='minimum length of characters')
    parser.add_argument('-max','--max_length', type=int,default=2, help='maximum length of characters')
    parser.add_argument('-out','--output',default='output/wordlist.txt', help='output of wordlist file.')
    args = parser.parse_args()
    if args.chars is None:
        os.system('python Gen_Wordlist.py -h')
    else:
        wordlist(args.chars, args.min_length, args.max_length, args.output)




if __name__ == "__main__":
    main()


