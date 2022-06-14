# DoesMyPasswordSuck
Tells you if a password has been seen in a data breach (using Have I Been Pwned's API)

## Usage
Three ways to use:
- Simply call the script and it will prompt you for the password: `./doesmypwsuck.py`
- Use the `-p` or `--password` flag when calling: `./doesmypwsuck.py --password password1`
- Pass in the password via stdin pipe: `echo -n password1 | ./doesmypwsuck.py`

## Example

```text
$ echo -n 'password1' | ./doesmypwsuck.py 
That password sucks! It has been seen 3,249,873 times
$ echo -n 'abunchofrandomcharsdsfwcr324refdfcwcer' | ./doesmypwsuck.py 
Your password does not suck!
```
