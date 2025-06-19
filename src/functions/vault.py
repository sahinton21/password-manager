# This is the module responsible for creating a vault
import os
import hashlib

def check_filename(filename):
  '''
  Make sure the file name input does not have any periods since that is illegal.
  We also have to make sure this file is not already in use
  return False if things are not allowed
  '''

  # Prevent a semicolon, |, or & since those can be used to mess with file edits

  # If we hit a file then error out
  return not os.path.isfile(filename)
  
def generate_salt():
  salt = os.urandom(16)
  salt = salt.hex()
  if salt[-1] == ":":
    salt = salt[0:-1] + "b"
  
  return salt


def create_vault(vault_name, key):
  '''
  Create a new password vault with a SHA256 hash prefix.
  We restrict the following characters 
  * |
  * `
  * ~
  * ^
  * /
  * \
  '''
  
  # attempt to create a new file. If we fail then return an error message. People could attempt to use this function to do something evil since we are using os commands
  if not check_filename(vault_name):
    raise Exception("Invalid character in name or file already in use")

  # Create a vault now
  vault = open(vault_name, "w")

  if not vault:
    raise Exception("Unable to create a vault")
  
  # Generate a salt and hash with the password
  salt = generate_salt()

  salted_key = salt + key


  hash = hashlib.sha256(salted_key.encode())

  vault.write(f"{salt}:{hash.hexdigest()}")


  vault.close()

  # Close up the vault and hide it
  os.system(f'attrib +h "{vault_name}"')


def edit_vault_key(vault_name, key):
  '''
  Swap out the vault key.
  '''

def delete_vault(vault_name, key):
  '''
  Use the key and confirm the user wants to delete the vault
  '''