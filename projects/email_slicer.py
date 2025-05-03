def email_slicer(*emails):
    
    res = []
    
    for email in emails:            
        username, domain = email.split('@')
        # print("Username: ", username)
        # print("Domain: ", domain)
        res.append(("username",username))
        res.append(("domain",domain))
    # return username, domain
    return res
print("check execution")
def mask_email(*emails):
    # print("1st function")
    res = []
    for email in emails:
        username, domain = email.split('@')
        # print("Username:--- ", username)
        # print("Domain:-- ", domain)
        masked_username = username[0] + "*" * (len(username)-1)

        masked_email = masked_username + '@' + domain

        res.append(("masked_email", f"{masked_email}@{domain}"))

    return res

emails = ["priyankakharade9765@gmail.com", "priyankakharade3172@gmail.com", ]

ans=email_slicer(*emails)
mask=mask_email(*emails)
# print("Username : ", ans[0])
# print("Domain : ", ans[1]) 
# print(ans)

for label, value in ans:
    print(f"{label}:{value}")

# print("Masked Emails:", mask)
for label, value in mask:
    print(f"{label}:{value}")

