import emoji 
print(emoji.emojize('Python is :thumbs_up:'))
print(emoji.emojize('Python is :thumbsup:', use_aliases=True))  # 使用别名
print(emoji.demojize('Python is :ridere_a_crepapelle:'))

# for k,v in emoji.EMOJI_UNICODE.items():
#     print(v,end=' ')