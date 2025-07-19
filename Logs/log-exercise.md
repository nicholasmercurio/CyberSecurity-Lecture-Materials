# 📝 Student Worksheet — Honeypot Log Analysis Exercise

### Objective:
Learn to analyze large log files to find signs of attacks and suspicious behavior using basic Linux commands.

### Logs Provided:
- `cowrie.log` — SSH honeypot  
- `http_honeypot.log` — Web honeypot  
- `dionaea_connections.log` — Malware honeypot  
- `canarytokens.log` — Fake token alert log  

---

## 1. SSH Honeypot (`cowrie.log`)

- How many login attempts were made in total?  
- How many of these attempts failed?  
- Which IP address made the most login attempts?  
- Did anyone successfully login? What commands did they run?  

---

## 2. Web Honeypot (`http_honeypot.log`)

- Find all HTTP requests that tried to access `/admin` or `/wp-login.php`.  
- How many times did the server respond with a 403 Forbidden status?  
- Are there any suspicious file upload attempts? Find them.  

---

## 3. Malware Honeypot (`dionaea_connections.log`)

- List all malware downloads detected. What URLs were used?  
- Identify any anonymous FTP login attempts.  
- Find connections to port 445 (SMB) and note the IP addresses.  

---

## 4. Canarytokens (`canarytokens.log`)

- How many token access alerts were triggered?  
- Which IP address triggered the most alerts?  
- What kinds of tokens were triggered? (Look for "TOKEN TYPE")  

---

## Bonus Challenge

- Use `grep`, `awk`, and other Linux tools to create a summary report showing:  
  - Top 3 attacking IPs across all logs.  
  - Most commonly used usernames for SSH attempts.  
  - Most frequent user-agent strings seen in the web and canarytoken logs.  

---

## Hints:

- Use `grep` to search for keywords.  
- Use `awk '{print $<field>}'` to extract specific columns.  
- Use `sort | uniq -c | sort -nr` to count and sort unique values.  
- Use `wc -l` to count lines matching your search.  

---
