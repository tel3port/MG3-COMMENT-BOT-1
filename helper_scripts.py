
with open("generated/x.txt") as urls_file:
    global urls
    urls = [line.strip() for line in urls_file]


for single_url in urls:
    s_url = single_url.split('/')
    l = len(s_url)

    month = s_url[l - 2]
    print(len(month))

    if len(month) > 2:
        with open("generated/static_url_list.txt", "a") as new_urls_file:
            print(single_url.strip(), file=new_urls_file)




