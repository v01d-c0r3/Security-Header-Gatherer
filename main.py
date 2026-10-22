import requests

SECURITY_HEADERS = [ 
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Content-Type-Options",
    "X-Frame-Options",
    "Referrer-Policy",
    "Permissions-Policy",
    "Cross-Origin-Opener-Policy",
    "Cross-Origin-Embedder-Policy",
    "Cross-Origin-Resource-Policy",
    ]

website = input("please enter URL of website: ")

response = requests.get(website, timeout=10)

for name in SECURITY_HEADERS:
    value = response.headers.get(name)
    if value:
        print(f"{name}: {value}")
    else:
        print(f"{name}: MISSING")