from core.sleuth import *
from core.banner import banner
import argparse
import platform
import os

sys = platform.system()

parse = argparse.ArgumentParser(description="[+] Tool for Web Scan")

parse.add_argument("-u", "--url", type=str, help="Url that will be scanned.")
parse.add_argument("-sS", "--subdomain-scan", action="store_true", help="Search for interesting dir's in url.")
parse.add_argument("-wL", "--whois-lookup", action="store_true", help="Make a Whois Lookup on url.")
parse.add_argument("-nS", "--nmap", action="store_true", help="Make a Nmap Scan in Site's IP.")
parse.add_argument("-o", "--osint", action="store_true", help="Osint the Nickname.")
parse.add_argument("-sS", "--sqli-scan", action="store_true", help="Scan for known vulnerabilities on the target URL.")
args = parse.parse_args()

def start():
    banner()
    if args.url:
        if args.whois_lookup:
            whoislookup(args.url)
        if args.nmap:
            nmapscan(args.url)
        if args.subdomain_scan:
            searchdirectories(args.url)
        if args.sqli_scan:
            sqliscan(args.url)
    if args.osint:
        osint(args.osint)
