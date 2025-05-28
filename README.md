# Web Sleuth v1.0
Web Sleuth is a Hacker/Osint Tool that is made for scan sites, the functions is:

- 🔍 Osint

- 🔍 Search directories

- 🌐 Nmap Scan

- 🔍 Whois Lookup

## Osint Function 🔍
This Funtion is a little very simple, this function will send requests to a lot of sites with the nick that the user placed, if the status code = 200 then the function will return that the account exists, else, he pass.

this have a little problems, like:
- The account not exists but the status code is 200
- The tool don't verify the content in response, making the previous error

But soon i will fix these problems

## Search Directories 🔍
This function searches for directories like: "/robots.txt", "/headers.txt", "/login.php" and others in url that you placed, if directory exists he returns, else, he pass, this work good!

## Nmap Scan 🌐
This Function pick the IP of the site that you placed and make a short scan in this IP, is simple, no much things.

## Whois Lookup 🔍
This will show to you the info of the domain of the site that you placed, again, no much things.
