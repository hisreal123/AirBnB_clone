
''' 
    FileStorage  class
'''
class FileStorage:
    __file__path = "file.json"
    __objects= {}

    '
    def all(self):
        # returns the object (dictionary)
        return self.__objects
    

    def new(self, object):
        if self.__
        key = str(object.__class__.name) + "." + str(object.id)
        dictionary_value = object
        FileStorage.__objects[key] = dictionary_value



