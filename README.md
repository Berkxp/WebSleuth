# Web Sleuth v1.0
Web Sleuth is a Hacker/Osint Tool that is made for scan sites, the functions is:

- 🔍 Osint

- 🔍 Subdomain Scanner

- 🌐 Nmap Scan

- 🔍 Whois Lookup

## Index

- [Osint Function](#osint-function)
- [Directories Scan function](#search-directories)
- [Nmap function](#nmap-scan)

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
This function make a whois lookup in the site's url, but in python, works in Windows, Linux, MacOS idk.

Usage: ```python websleuth.py -u 'site's url' -wL```
