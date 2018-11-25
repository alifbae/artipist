from bs4 import BeautifulSoup
import json

def getScriptData(soup):
  for tag in soup.findAll('script'):
    if "window._sharedData" in tag.text:
      return tag.text.split('</script>')[0] # get first elem which is window._sharedData json


def sanitizeScriptData(scriptData):
  remove_function_name = scriptData[20:]
  last_semicolon_removed = remove_function_name[:-1]
  return last_semicolon_removed


def makeJSON(sanitzedOutput):
  return json.loads(sanitzedOutput)


def makeJSONFile(jsonData, outputFilePath):
  with file(outputFilePath, 'w+') as jsonFileOut:
    jsonFileOut.write(json.dumps(jsonData, indent=4, sort_keys=True))


def main(HTMLFilePath):
  with file(HTMLFilePath) as HTMLFile:
    soup = BeautifulSoup(HTMLFile, features="html.parser")
    scriptData = getScriptData(soup)
    sanitizedOutput = sanitizeScriptData(scriptData)
    jsonData = makeJSON(sanitizedOutput)
    makeJSONFile(jsonData, HTMLFilePath[:-4]+'json')


main('../html/artidote_singapore.html')
