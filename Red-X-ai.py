# By : @REDX_64     |      Enjoy
import requests
while True:
    req = input("☠️ ＭＡＤＥ ＢＹ >> \033[36mR E D - X H A C K I N G \n\n SEND YOUR QUESTION ❓ ")
    language = req.split(" : ")[0]
    cookies = {
    'sessionId': 'fa4f4581-5b1c-4731-a0a1-9fa5ae22a41b',
    'intercom-id-jlmqxicb': 'ea96d2b6-d7d9-44ad-b84e-ed256ad9ebd3',
    'intercom-device-id-jlmqxicb': 'ae3c3535-e385-490f-963e-27d0b99f6f6f',
    '__Host-authjs.csrf-token': '0bd961600a8991e833d7d441aec8a66450332d668242dd7dc8eb3fb0d2eb94d4%7C27287a370964dcd1a57d5010fff569be9f5c1c2f81347af3267dfebf799bc1f2',
    '__Secure-authjs.callback-url': 'https%3A%2F%2Fwww.blackbox.ai',
}

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.blackbox.ai',
        'priority': 'u=1, i',
        'referer': f'https://www.blackbox.ai/chat/expert-{language}',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
    }

    json_data = {
        'messages': [
            {
                'id': 'wZAiJzP',
                'content': req,
                'role': 'user',
            },
        ],
        'previewToken': None,
        'userId': None,
        'codeModelMode': True,
        'agentMode': {},
        'trendingAgentMode': {
            'mode': True,
            'id': language,
        },
        'isMicMode': False,
        'userSystemPrompt': None,
        'maxTokens': 1024,
        'playgroundTopP': None,
        'playgroundTemperature': None,
        'isChromeExt': False,
        'githubToken': '',
        'clickedAnswer2': False,
        'clickedAnswer3': False,
        'clickedForceWebSearch': False,
        'visitFromDelta': False,
        'mobileClient': False,
        'userSelectedModel': None,
        'validated': '00f37b34-a166-4efb-bce5-1312d87f2f94',
        'imageGenerationMode': False,
        'webSearchModePrompt': False,
    }

    response = requests.post('https://www.blackbox.ai/api/chat', cookies=cookies, headers=headers, json=json_data)
    print(response.text)








