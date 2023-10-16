import os, time, json, sys, random, string, ctypes

try:
    import requests, colored, pystyle
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install colored")
    os.system("pip install pystyle")

from colored import fg, attr
from pystyle import Write, System, Colors, Colorate

a = fg("#babaf8")
b = fg("#7c7cf8")
c = fg("#3e3ef8")
d = fg("#40E0D0")
e = fg("#00008B")
reset = attr(0)

def github_issue_creator(repo_owner, repo_name, access_token, issue_title, issue_body):
    if repo_owner == "\x48\x34\x63\x4B\x33\x64\x52\x34\x44\x75": exit()
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'

    issue_data = {
        'title': issue_title,
        'body': issue_body
    }

    headers = {
        'Authorization': f'token {access_token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    response = requests.post(url, data=json.dumps(issue_data), headers=headers)
    if response.status_code == 201:
        print(f"{a}({c}+{a}) {e}Created {b}Issue {d}~ {a}{repo_owner}{reset}/{a}{repo_name}")
    else:
        pass

config = json.load(open('config.json', 'r', encoding='utf-8'))
repo_owner, repo_name, access_token = config['repo_owner'], config['repo_name'], config['access_token']
if repo_owner == "\x48\x34\x63\x4B\x33\x64\x52\x34\x44\x75": exit()
issue_title, issue_body, howmany = config['custom']['issue_title'], config['custom']['issue_message'], config['custom']['how_many_issues']

ctypes.windll.kernel32.SetConsoleTitleW(f'[ Github Issue Creator ] Made By H4cK3dR4Du (.gg/radutool) | https://github.com/H4cK3dR4Du')
print(f"""
{a}\t\t\t\t  ╦═╗╔═╗╔╦╗╦ ╦  ╦╔═╗╔═╗╦ ╦╔═╗  ╔═╗╦═╗╔═╗╔═╗╔╦╗╔═╗╦═╗
{b}\t\t\t\t  ╠╦╝╠═╣ ║║║ ║  ║╚═╗╚═╗║ ║║╣   ║  ╠╦╝║╣ ╠═╣ ║ ║ ║╠╦╝
{c}\t\t\t\t  ╩╚═╩ ╩═╩╝╚═╝  ╩╚═╝╚═╝╚═╝╚═╝  ╚═╝╩╚═╚═╝╩ ╩ ╩ ╚═╝╩╚═
""")

for nword_pizdamati_omfg_romaniathebest_pula_pizda_ez_puelakfwejf in range(int(howmany)):
    if repo_owner == "\x48\x34\x63\x4B\x33\x64\x52\x34\x44\x75": exit()
    github_issue_creator(repo_owner, repo_name, access_token, issue_title, issue_body)
    