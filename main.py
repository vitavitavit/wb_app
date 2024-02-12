import requests

headers = {
    'accept': 'application/json',
    'Authorization': 'eyJhbGciOiJFUzI1NiIsImtpZCI6IjIwMjMxMjI1djEiLCJ0eXAiOiJKV1QifQ.eyJlbnQiOjEsImV4cCI6MTcyMzE0NTU5OCwiaWQiOiJiZWI1MTU2My1mZTgwLTRiOTUtODhkNi1kODc0OWI0ZjRkZDkiLCJpaWQiOjEwMDE0Mjg1LCJvaWQiOjEyOTg1NzEsInMiOjE2LCJzaWQiOiJiMmQ2ODY3OS1jNTJiLTQ2MmYtYTAyOS1kMzg3MGE4MjJhNWYiLCJ0IjpmYWxzZSwidWlkIjoxMDAxNDI4NX0.5rvPX97cT_sOdaDJfiCpG6zzACa0A0P4RH5xWh6T4Mfj5oFmAlgLbI5BVlhH6sheoNTVMJAsJuurjZtqS558iA',
}

response = requests.get('https://suppliers-api.wildberries.ru/api/v3/orders/new', headers=headers)

print (response)