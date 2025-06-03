# Web Sleuth v1.0
Web Sleuth is a Hacker/Osint Tool that is made for scan sites, the functions is:

- 🔍 Osint

- 🔍 Subdomain Scanner

- 🌐 Nmap Scan

- 🔍 Whois Lookup

## Functions

- [Osint 🔍](#osint-function)
- [Subdomain Scan 🔍](#search-directories)
- [Nmap 🌐](#nmap-scan)
- [Sql Injection Scan 💉](#sql-injection-scan-)
- [Help](#help)

## Osint Function 🔍
This Funtion is a little very simple, this function will send requests to a lot of sites with the nick that the user placed, if the status code = 200 then the function will return that the account exists, else, he pass, need a lot of upgrades, these upgrades will be added in future.

this little problems, like:
- The account not exists but the status code is 200
- The tool don't verify the content in response, making the previous error

But soon i will fix these problems.

Usage: ```python websleuth.py -o 'nickname'```

## Subdomain Scanner 🔍
This functions will search by subdomains in the url, if the subdomain exists the script returns that he exists, else, he don't make anything, this is good to search for vulnerable url's in the site.

Usage: ```python websleuth.py -u 'site's url' -dS```

## Nmap Scan 🌐
This Function pick the IP of the site that you placed and make a scan in the ip's network, automatizing the process, the usage is bellow:

Example: ```python websleuth.py -u "site's url" -nS```
.

## Whois Lookup 🔍
This function make a whois lookup in the site's url returning the info bellow:

- Domain
- Registrator
- Creation Date
- Expiration Date
- Owner's Name
- Owner's Email
- Phone

but in python, works in Windows, Linux, MacOS idk.

- Usage: ```python websleuth.py "site's url" -wL```

## Sql Injection Scan 💉
This function is a lot helpful to wlack Hat and white hat Hackers, because he scans a site to found probably Sql Injection vulnerable Subdomain, the subdomains that he scans is a little, but i will increase in future.

- Usage: ```python websleuth.py -u "site's url" -S```

## Help
Bellow is the options resumed's, you can find these info's typing "python websleuth.py -h" in Terminal, Help:


Usage: websleuth.py [-h] [-u URL] [-S] [-nS] [-s] [-o] [-wL]


[+] Tool for Web Scan


Options:

  -h, --help            show this help message and exit

  -u, --url URL         Url that will be scanned.
  
  -S, --sqli-scan       Scan for known vulnerabilities on the target URL.
  
  -nS, --nmap           Make a Nmap Scan in Site's IP.
  
  -s, --subdomain-scan  Search for interesting dir's in url.
  
  -o, --osint           Osint the Nickname.
  
  -wL, --whois-lookup   Make a Whois Lookup on url.
