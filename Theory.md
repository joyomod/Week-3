# CFG ASSESSMENT

**Section 1: Theory Questions \[31 marks\]**

| 1.1 What does SDLC stand for? | 1 mark |
| ----------------------------- | ------ |
> **Answer:**
Software Development LifeCycle, which is a process that ensures the production of high-quality software in the most cost-effective and timely manner.
---

| 1.2 What exception is thrown when you divide a number by 0? | 1 mark |
| ----------------------------------------------------------- | ------ |
> **Answer:**
ZeroDivisionError
---

| 1.3 What is the git command that moves code from the local repository to the remote repository? | 1 mark |
| ----------------------------------------------------------------------------------------------- | ------ |
> **Answer:**
`git push`
---

| 1.4 What does NULL represent in a database? | 1 mark |
| ------------------------------------------- | ------ |
> **Answer:**
The value of a column is missing or empty
---

| 1.5 Name 2 responsibilities of the Scrum Master | 2 marks |
| ----------------------------------------------- | ------- |
> **Answer:**
**Facilitate the Scrum process:** The Scrum Master supports and enforces the Scrum process and other rules that the team has agreed, thereby keeping the team on track.
>
**Remove impediments:** The Scrum Master is responsible for managing any obstacles that arise for the team, and helping to clear them and protect the team from distractions.

---

| 1.6 Name 2 debugging methods, and when you would use them. | 4 marks |
| ---------------------------------------------------------- | ------- |
> **Answer:**

---

| 1.7 Looking at the following code, describe a case where this function would throw an error when called. Describe this case and talk about what exception handling you’ll need. | 5 marks |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |

```
def can_pay(price, cash_given):
    if cash_given >= price:
        return True
    else:
        return False
```
> **Answer:**
If the values of the parameter’s ‘price’ or ‘cash_given’ are not integers or floats, but a different data type like a string it would result in an error. So, we would need to include exception handling such as try and except. The modified code below has exception handling, here, I have told the program to run the code within the try block and if it runs into an error or has code that might cause an exception, it should skip and jump to the except block and if no exception occurs the exception block is skipped.

```def can_pay(price, cash_given):
    try:
        if cash_given >= price:
            return True
        else:
            return False
    except TypeError:
        print("The price and cash_given can only be an integer or a float, please try again")
```
---

| 1.8 What is git branching? Explain how it is used in Git. | 6 marks |
| --------------------------------------------------------- | ------- |
> **Answer:**
Git branching is a feature within git that allows one to diverge from the main repository, thereby creating independent lines within one repository. This is useful for developers when they need to diverge from production based code to make code changes such as adding a feature or fixing a bug, so they are able to work on a copy of the code without altering the original code and are also able to merge the branch to the main code repo if needed.
---

| 1.9 Design a restaurant ordering system. | 10 marks |
| ---------------------------------------- | -------- |

| **You do not need to write code, but describe a high-level approach:**
| - **Draw a list of key requirements**
| - **What are your main considerations and problems?**
| - **What components or tools would you potentially use?**
