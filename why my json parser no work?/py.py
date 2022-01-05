def test():
    print("test")
    
def parseJson(json, key):
    # algorithm that parses json based on key
    if(json == None):
        return None
    if(key == None):
        return None
    if(json.find(key) == -1):
        return None
    return json.split(key)[1].split(',')[0].split(':')[1].strip()
    
    
testJson = '{"name":"test","age":10},{"name":"test2","age":20},{"name":"test3","age":30}'