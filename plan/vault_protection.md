## Secrets
This is the way we will protect our vault information. we will have this
method of protecting ourselves from people reading our encrypted passcodes.

Since I am too lazy for SQL, we are going to have to make this work with reading
files. The vault key will be a SHA256 hash of salt + key. This key will be used to decrypt our values. This key should probably be rotated over time.

```
<salt>|<vault_key>
~
/<site>|<username>|<password>|<date>/
/<site>|<username>|<password>|<date>/
```

## Rules

Passwords cannot contain the following characters
* |
* `
* ~
* ^
* /
* \
