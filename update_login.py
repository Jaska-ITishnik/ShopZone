import os
import glob

html_files = glob.glob('*.html')

login_str_1 = '<a href="login.html" class="login-btn">Kirish</a>'
login_str_2 = '<a href="account.html" class="login-btn">Kabinet</a>'

user_icon_str = '''<a href="account.html" class="header-icon user-icon" aria-label="Shaxsiy kabinet">
        <svg xmlns="http://www.w3.org/2000/svg" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>
      </a>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if login_str_1 in content or login_str_2 in content:
        content = content.replace(login_str_1, user_icon_str)
        content = content.replace(login_str_2, user_icon_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
