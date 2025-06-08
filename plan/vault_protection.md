## Secrets
This is the way we will protect our vault information. we will have this
method of protecting ourselves from people reading our encrypted passcodes.

Since I am too lazy for SQL, we are going to have to make this work with reading
files. The vault key will be a SHA256 hash of salt + key. This key will be used to decrypt our values. This key should probably be rotated over time.

```
<salt>|<vault_key>
~<site>|<username>|<password>|<date>~
~<site>|<username>|<password>|<date>~
```

## Rules

Passwords should be rotated every 120 days.
Passwords cannot contain the following characters:
* |
* `
* ~
* ^
* /
* \

Vault keys must be 16-127 characters long, contain a lowercase letter, contain an uppercase letter, contain a number, contain a symbol.
Vault keys should be rotated every 6 months.
Vault keys will use a password salt to create a unique hash with the SHA256 algorithm.


## Functions
This is similar to a CRUD app, but our objects are vaults which contain rows of credentials.

Vaults shall do the following:
Create a vault with a username and key.
Delete a vault by using the key.

Credentials shall do the following:
Create a set of credentials with a site/app, username, password, and date to track expiration.
Read a password if the key is correct by decrpyting the vault.
Update a password.
Notify the user a password should be rotated after 120 days.
Delete a password.

The passwords will be stored in some basic file that is encrypted. We should probably pick a unique extension for this. We also don't want anyone to delete it, so it should have properties like the /shadow directory.
