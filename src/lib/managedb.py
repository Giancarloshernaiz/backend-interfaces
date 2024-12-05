import pathlib
import json

class ManageDB:
  __file_address = "{0}/src/db/colors.json".format(pathlib.Path().absolute())
  __file_address_2 = "{0}/src/db/media.json".format(pathlib.Path().absolute())
  
  def read_colors(self):
    with open(self.__file_address, "r") as file:
      return json.loads(file.read())
    
  def write_colors(self, color):
    with open(self.__file_address, "w") as file:
      file.write(json.dumps(color))
      
  def read_multimedia(self):
    with open(self.__file_address_2, "r") as file:
      return json.loads(file.read())
  
  def write_multimedia(self, media):
    with open(self.__file_address_2, "w") as file:
      file.write(json.dumps(media))