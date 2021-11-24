import speedtest

st = speedtest.Speedtest()

print('PLEASE SELECT WHAT DO YOU WANT TO DO....')
print("1. Check Download Speed")
print("2. Check Upload Speed")
print("3. Check ping")
choice = int(input("Please enter your choice (1,2,3) --> "))

if choice == 1:
    print("Checking your download speed...")
    print("Your download speed", st.download())
elif choice == 2:
    print("Checking your upload speed...")
    print("Your upload speed", st.upload())
elif choice == 3:
    print("Checking your ping...")
    servernames = []
    st.get_servers(servernames)
    print("Your ping", st.results.ping)
