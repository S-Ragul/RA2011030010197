import requests

def Number(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            numbers = data.get("numbers", [])  
            return numbers
        else:
            print("API request failed:", response.status_code)
            return []
    except Exception as e:
        print("An error occurred:", str(e))
        return []

def sort_num(numbers):
    return sorted(numbers)

if __name__ == "__main__":
    api_urls = [
        
        "http://20.244.56.144/numbers/primes",
        "http://20.244.56.144/numbers/fibo",
        "http://20.244.56.144/numbers/odd",
    ]
    
    all_numbers = []

    for api_url in api_urls:
        numbers = Number(api_url)
        all_numbers.extend(numbers)
    
    if all_numbers:
        duplicate_num = sort_num(all_numbers)
        sorted_numbers = set(duplicate_num)
        ListA=[]
        for i in sorted_numbers:
            var=i
            ListA.append(var)
            
        print("{")
        print('      "numbers:"', ListA)
        print("}")
    else:
        print("No numbers retrieved from any of the APIs.")
