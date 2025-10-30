# https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md
# https://github.com/anuraghazra/github-readme-stats/blob/master/themes/index.js
# https://github.com/vuvannghiaCV

data = [

    ("tokyonight", "einvoice-system"),
    ("highcontrast", "user-manager"),
    ("dark", "api-gateway"),
    ("radical", "vuvannghiaCV"),





    # (" ", "cv-contact-manager"),
    # # (" ", "nghia-oop-adapter-round-square"),
    # ("", "nghia-contact-manager"),
    # ("merko", "nghia-crawl-data-scrapy-topcv-crawler"),


    # TODO rảnh thì xóa github sau
    # ("synthwave", "fis-mini-project-test-first"),
    # ("cobalt2", "fis-mini-project-dns-sinkhole-demo"),
    # ("transparent", "fis-mini-project-kong-api-gateway"),
    # ("highcontrast", "fis-mini-project-microservices"),
    # ("gruvbox", "fis-bao-cao-thuc-tap"),



    # ("onedark", "xxxxxxxxxxxxxxxxxxxx")
    # ("prussian", "xxxxxxxxxxxxxxxxxxxx")
    # ("monokai", "xxxxxxxxxxxxxxxxxxxx")
    # ("vue", "xxxxxxxxxxxxxxxxxxxx")
    # ("vue-dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("shades-of-purple", "xxxxxxxxxxxxxxxxxxxx")
    # ("nightowl", "xxxxxxxxxxxxxxxxxxxx")
    # ("buefy", "xxxxxxxxxxxxxxxxxxxx")
    # ("blue-green", "xxxxxxxxxxxxxxxxxxxx")
    # ("algolia", "xxxxxxxxxxxxxxxxxxxx")
    # ("great-gatsby", "xxxxxxxxxxxxxxxxxxxx")
    # ("darcula", "xxxxxxxxxxxxxxxxxxxx")
    # ("bear", "xxxxxxxxxxxxxxxxxxxx")
    # ("solarized-dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("solarized-light", "xxxxxxxxxxxxxxxxxxxx")
    # ("chartreuse-dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("nord", "xxxxxxxxxxxxxxxxxxxx")
    # ("gotham", "xxxxxxxxxxxxxxxxxxxx")
    # ("material-palenight", "xxxxxxxxxxxxxxxxxxxx")
    # ("graywhite", "xxxxxxxxxxxxxxxxxxxx")
    # ("vision-friendly-dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("ayu-mirage", "xxxxxxxxxxxxxxxxxxxx")
    # ("midnight-purple", "xxxxxxxxxxxxxxxxxxxx")
    # ("calm", "xxxxxxxxxxxxxxxxxxxx")
    # ("flag-india", "xxxxxxxxxxxxxxxxxxxx")
    # ("omni", "xxxxxxxxxxxxxxxxxxxx")
    # ("react", "xxxxxxxxxxxxxxxxxxxx")
    # ("jolly", "xxxxxxxxxxxxxxxxxxxx")
    # ("maroongold", "xxxxxxxxxxxxxxxxxxxx")
    # ("yeblu", "xxxxxxxxxxxxxxxxxxxx")
    # ("blueberry", "xxxxxxxxxxxxxxxxxxxx")
    # ("slateorange", "xxxxxxxxxxxxxxxxxxxx")
    # ("kacho_ga", "xxxxxxxxxxxxxxxxxxxx")
    # ("outrun", "xxxxxxxxxxxxxxxxxxxx")
    # ("ocean_dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("city_lights", "xxxxxxxxxxxxxxxxxxxx")
    # ("github_dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("github_dark_dimmed", "xxxxxxxxxxxxxxxxxxxx")
    # ("discord_old_blurple", "xxxxxxxxxxxxxxxxxxxx")
    # ("aura_dark", "xxxxxxxxxxxxxxxxxxxx")
    # ("panda", "xxxxxxxxxxxxxxxxxxxx")
    # ("noctis_minimus", "xxxxxxxxxxxxxxxxxxxx")
    # ("swift", "xxxxxxxxxxxxxxxxxxxx")
    # ("aura", "xxxxxxxxxxxxxxxxxxxx")
    # ("apprentice", "xxxxxxxxxxxxxxxxxxxx")
    # ("moltack", "xxxxxxxxxxxxxxxxxxxx")
    # ("codeSTACKr", "xxxxxxxxxxxxxxxxxxxx")
    # ("rose_pine", "xxxxxxxxxxxxxxxxxxxx")
    # ("catppuccin_latte", "xxxxxxxxxxxxxxxxxxxx")
    # ("catppuccin_mocha", "xxxxxxxxxxxxxxxxxxxx")
    # ("date_night", "xxxxxxxxxxxxxxxxxxxx")
    # ("one_dark_pro", "xxxxxxxxxxxxxxxxxxxx")
    # ("rose", "xxxxxxxxxxxxxxxxxxxx")
    # ("holi", "xxxxxxxxxxxxxxxxxxxx")
    # ("neon", "xxxxxxxxxxxxxxxxxxxx")
    # ("blue_navy", "xxxxxxxxxxxxxxxxxxxx")
    # ("calm_pink", "xxxxxxxxxxxxxxxxxxxx")
    # ("ambient_gradient", "xxxxxxxxxxxxxxxxxxxx")
]

with open("README.md", "w", encoding="utf-8") as file:
    file.write("<hr>\n\n")
    for theme, repo in data:
        file.write(f"""
<!-- -->

<a href="https://github.com/vuvannghiaCV/{repo}" target="_blank">
<img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=vuvannghiaCV&repo={repo}&theme={theme}" alt="{repo}" />
</a>

<!-- -->

""")
