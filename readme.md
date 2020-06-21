## API Reference diagram for Banking Transactions


| Function  | URL  | PARAMS  | METHOD | STATUS CODE |
|-----------|------|---------|---|---|
| Register  | /register | username, password | POST  | 200, 301, 302   |
| Add       | /add | username,password,amount | POST   | 200, 301, 302, 304   |
| Transfer | /transfer | username, password, amount, toAccountNumber | POST   | 200, 301, 302, 304  |
| Check Balance| /checkbalance| username, password | POST   | 200, 301, 302   |
| Take Loan | /takeloan| username, password, amount| POST   | 200, 301, 302  |
| Pay Loan  | /payloan| username, password, amount| POST   | 200, 301, 302   |


## Legend for Status Codes

- 200 = Success 
- 301 = Invalid Username
- 302 = Invalid Password
- 303 = Not enough money
- 304 = Amount less than 0
