import json

userName = 'Max'
year = '2024'
topSize = 3
totalMessages = 0
chatMessagesCount = 0
chats = []

with open('result.json', encoding='utf-8') as file:
  data = json.load(file)

for chat in data['chats']['list']:
  if chat['type'] == 'personal_chat':
    chatMessagesCount = 0
    chatName = chat['name']
    chatId = chat['id']
    for msg in chat['messages']:
      if 'from' in msg and msg['from'] == userName and msg['date'].startswith(year):
        totalMessages += 1
        chatMessagesCount += 1
    chats.append({'name': chatName, 'messages_count': chatMessagesCount})
chats.sort(key=lambda item: item['messages_count'], reverse=True)

print('************************************')
print(f'Personal stats of user {userName} for {year}')
print('************************************\n')
print(f'Total number of messages in all chats: {totalMessages}')
print(f'Top-{topSize} chats:')

top = range(0, topSize)
for i in top:
  print(f' {i+1}. {chats[i]["name"]}: {chats[i]["messages_count"]}')
