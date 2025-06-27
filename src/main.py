import os
import hashlib

from functions.vault import *

if __name__ == "__main__":
  # test some of the functions here 

  #create_vault("vault.valt", "password")

  val = check_password("vault", "password")

  delete_vault("vault", "password")

  print(val)