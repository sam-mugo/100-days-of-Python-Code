#supply default parameter value
# However, if the name is missing, return the string:

# ```text
# One for you, one for me.
# ```

# Here are some examples:

# |Name    |String to return
# |:-------|:------------------
# |Alice   |One for Alice, one for me.
# |Bob     |One for Bob, one for me.
# |        |One for you, one for me.
# |Zaphod  |One for Zaphod, one for me.
def two_fer(name = "you"):
    return f"One for {name}, one for me."

two_fer("mugo")
    
 
