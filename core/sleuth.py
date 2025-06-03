import requests
import socket
import whois
from colorama import *
from urllib.parse import urlparse
import os

def nmapscan(site):
    site = urlparse(site)
    siten = f"{site.netloc}"
    site = socket.gethostbyname(siten)
    print(Fore.LIGHTCYAN_EX + "\n=========== NMAP SCAN ===========" + Fore.RESET)
    os.system(f"nmap -sV -T5 {site}")
    print(Fore.LIGHTCYAN_EX + "\n=================================" + Fore.RESET)

def whoislookup(domain):
    urlp = urlparse(domain)
    urlf = f"{urlp.netloc}"
    try:
        w = whois.whois(domain)
        print(Fore.LIGHTRED_EX + "\n========== WHOIS LOOKUP =========\n" + Fore.RESET)
        print(f"[+] Domain: {w.domain_name}")
        print(f"[+] Registrator: {w.registrar}")
        print(f"[+] Creation Date: {w.creation_date}")
        print(f"[+] Expiration date: {w.expiration_date}")
        print(f"[+] Owner's Name: {w.name}")
        print(f"[+] Owner's Email: {w.email}")
        print(f"[+] Phone: {w.phone}")
        print(Fore.LIGHTRED_EX + "\n=================================" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}" + Fore.RESET)

def subscan(url):
    dirs = [
        "/index.php",
        "/admin/index.php",
        "/admin/login.php",
        "/login.php",
        "/passwords/index.php",
        "/password/index.php",
        "/pass/index.php",
        "/headers.txt",
        "/robots.txt",
        "/cart.php",
        "/home.php"
]
    for d in dirs:        
        urlf = urlparse(url)
        urls = f"{urlf.scheme}://{urlf.netloc}"
        urld = f"{urls}{d}"
        try:
            req = requests.get(urld)
            if req.status_code == 200:
                print(Fore.LIGHTGREEN_EX + f"\n[+] A interesting url in: {urld}" + Fore.RESET)
            else:
                pass
        except requests.RequestException as e:
            print(Fore.RED + f"\n[+] Error: {e}" + Fore.RESET)

def osint(nick):
    sites = [
    f"https://www.facebook.com/{nick}",
    f"https://www.twitter.com/{nick}",
    f"https://www.instagram.com/{nick}",
    f"https://www.linkedin.com/in/{nick}",
    f"https://www.snapchat.com/add/{nick}",
    f"https://www.tiktok.com/@{nick}",
    f"https://www.pinterest.com/{nick}",
    f"https://www.reddit.com/user/{nick}",
    f"https://www.tumblr.com/blog/{nick}",
    f"https://www.youtube.com/c/{nick}",
    f"https://www.whatsapp.com/{nick}",
    f"https://www.wechat.com/{nick}",
    f"https://www.viber.com/{nick}",
    f"https://telegram.me/{nick}",
    f"https://www.flickr.com/people/{nick}",
    f"https://www.quora.com/profile/{nick}",
    f"https://discord.com/users/{nick}",
    f"https://www.meetup.com/members/{nick}",
    f"https://myspace.com/{nick}",
    f"https://www.badoo.com/{nick}",
    f"https://www.twitch.tv/{nick}",
    f"https://foursquare.com/{nick}",
    f"https://www.pscp.tv/{nick}",
    f"https://www.joinclubhouse.com/{nick}",
    f"https://vk.com/id{nick}",
    f"https://www.xing.com/profile/{nick}",
    f"https://line.me/ti/p/@{nick}",
    f"https://www.kik.com/{nick}",
    f"https://www.stumbleupon.com/stumbler/{nick}",
    f"https://ello.co/{nick}",
    f"https://gab.com/{nick}",
    f"https://mastodon.social/@{nick}",
    f"https://rumble.com/user/{nick}",
    f"https://dlive.tv/{nick}",
    f"https://www.vero.co/{nick}",
    f"https://nextdoor.com/profile/{nick}",
    f"https://www.caffeine.tv/{nick}",
    f"https://www.couchsurfing.com/people/{nick}",
    f"https://www.goodreads.com/user/show/{nick}",
    f"https://www.deviantart.com/{nick}",
    f"https://www.behance.net/{nick}",
    f"https://dribbble.com/{nick}",
    f"https://500px.com/{nick}",
    f"https://soundcloud.com/{nick}",
    f"https://www.mixcloud.com/{nick}",
    f"https://www.last.fm/user/{nick}",
    f"https://bandcamp.com/{nick}",
    f"https://www.meetme.com/{nick}",
    f"https://www.hi5.com/{nick}",
    f"https://www.tagged.com/{nick}",
    f"https://www.friendster.com/{nick}",
    f"https://www.orkut.com/{nick}",
    f"https://www.classmates.com/{nick}",
    f"https://www.blogger.com/profile/{nick}",
    f"https://wordpress.com/{nick}",
    f"https://www.wattpad.com/user/{nick}",
    f"https://www.fandom.com/user/{nick}",
    f"https://www.ravelry.com/people/{nick}",
    f"https://letterboxd.com/{nick}",
    f"https://untappd.com/user/{nick}",
    f"https://www.strava.com/athletes/{nick}",
    f"https://runkeeper.com/user/{nick}",
    f"https://www.fitbit.com/user/{nick}",
    f"https://www.myfitnesspal.com/profile/{nick}",
    f"https://www.mapmyrun.com/profile/{nick}",
    f"https://www.zomato.com/{nick}",
    f"https://www.yelp.com/user_details?userid={nick}",
    f"https://www.tripadvisor.com/Profile/{nick}",
    f"https://www.airbnb.com/users/show/{nick}",
    f"https://www.spoonflower.com/profiles/{nick}",
    f"https://www.craftster.org/forum/index.php?action=profile;u={nick}",
    f"https://www.instructables.com/member/{nick}/",
    f"https://www.skillshare.com/user/{nick}",
    f"https://www.udemy.com/user/{nick}",
    f"https://www.coursera.org/user/{nick}",
    f"https://www.khanacademy.org/profile/{nick}",
    f"https://www.codecademy.com/profiles/{nick}",
    f"https://www.edx.org/user/{nick}",
    f"https://www.linkedin.com/learning/instructors/{nick}",
]
    for s in sites:
        try:
            req = requests.get(s)
            if req.status_code == 200:
                print(Fore.LIGHTGREEN_EX + f"\n[!] Account found in: {s}" + Fore.RESET)
            else:
                pass
        except requests.RequestException as e:
            print(Fore.RED + f"[!] Error: {e}" + Fore.RESET)


def sqliscan(u):
    u = urlparse(u)
    s = [
        "cart.php",
        "cart.php?id=1",
        "cart.php?cat=1",
        "shop.php",
        "shop.php?id=1",
        "shop.php?cat=1",
        "gallery.php",
        "gallery.php?id-1",
        "gallery.php?cat=1",
        "index.php",
        "index.php?id=1", 
        "index.php?cat=1",
        "login.php",
        "login.php?id=1",
        "login.php?cat=1",
        "add_cart.php",
        "add_cart.php?id=1",
        "add_cart.php?cat=1",
        "signup.php",
        "signup.php?id=1",
        "signup.php?cat=1",
    ]
    print(Fore.RED + "\n============= SQLI SCAN =============\n")
    for su in s:
        ur = f"{u.scheme}://{u.netloc}/{su}"
        try:
            r = requests.get(ur)
            if r.status_code == 200:
                if "mysql" in r.text.lower():
                    print(Fore.LIGHTGREEN_EX + f"\n[+] SqlI found on: {ur}\n" + Fore.RESET)
        except requests.RequestException as e:
            print(Fore.LIGHTRED_EX + f"\n[!] Error: {e}\n" + Fore.RESET)
    print(Fore.RED + "=====================================")
