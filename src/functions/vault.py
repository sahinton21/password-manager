# This is the module responsible for creating a vault
import os
import hashlib

BANNED_FILENAME_CHARS = [";", "|", "&"]


def check_valid_filename(filename):
  '''
  Make sure the file name input does not have any periods since that is illegal.
  We also have to make sure this file is not already in use
  return False if things are not allowed
  '''

  # Prevent a semicolon, |, or & since those can be used to mess with file edits

  #Also prevent any spaces since those mess with function calls
  if " " in filename:
    return False
  
  for char in BANNED_FILENAME_CHARS:
    if char in filename:
      return False

  # This is a good file
  return True

def check_vault_exists(filename):
  '''
  Check if the vault by filename exists
  '''
  return os.path.isfile(f"./{filename}.valt")


def check_password( vault_name, password_attempt):
  # read the vault to check if the hashes match and salt match
  vault_creds = ""

  file = open(f"./{vault_name}.valt", "r") 

  if not file:
    raise FileNotFoundError(f"Vault {vault_name} does not exist")


  # Read out the salt and check if the hashes match
  
  
  vault_creds += file.readline()

  file.close()


  salt = vault_creds.split(":")[0]
  hash_password = vault_creds.split(":")[1].strip()

  # Check the password attempt against the truth
  hash_attempt = hash_password_and_salt(password_attempt, salt)

  print(hash_attempt)
  print(hash_password)

  if hash_password == hash_attempt:
    return True
  return False





def hash_password_and_salt(password, salt):
  salted_password = password + salt 

  hash = hashlib.sha256(salted_password.encode())
  return hash.hexdigest()

def generate_salt():
  salt = os.urandom(16)
  salt = salt.hex()
  if salt[-1] == ":":
    salt = salt[0:-1] + "b"
  
  return salt


def create_vault(vault_name, password):
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
  if not check_valid_filename(vault_name) or check_vault_exists(vault_name):
    error_message= f"Invalid character in name or name already in use"
    raise Exception()

  # Create a vault now
  vault = open(vault_name, "w")

  if not vault:
    raise Exception("Unable to create a vault")
  
  # Generate a salt and hash with the password
  salt = generate_salt()

  #salted_key = salt + key

  

  hash = hash_password_and_salt(password, salt)

  vault.write(f"{salt}:{hash}\n")


  vault.close()

  # Close up the vault and hide it
  os.system(f'attrib +h "{vault_name}"')


def edit_vault_key(vault_name, password):
  '''
  Swap out the vault key.
  '''

def delete_vault(vault_name, password):
  '''
  Use the key and confirm the user wants to delete the vault
  '''

  # check if the file exists
  if  not check_valid_filename(vault_name):
    error_message= f"No vault with the name {vault_name} was found"
    raise FileNotFoundError(error_message)
  
  # Make sure the password matches what is found in the vault. Delete if the keys match
  if check_password(vault_name, password):
    os.remove(f"./{vault_name}.valt")
