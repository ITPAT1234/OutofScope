#!/usr/bin/env python 
import optparse
import time

def get_arguments():
   parser = optparse.OptionParser()
   parser.add_option("-s","--scope",dest="scope", help="Add List of Scope (xxx,xxxxx,xx)")
   parser.add_option("-f","--filePath",dest="filePath", help="Enter your SubDomain Filepath")
   parser.add_option("-o","--output",dest="output",help="Enter your Specific Path")
   (options,argument) = parser.parse_args()

   if not options.scope and not options.filePath :
      parser.error("[-] Please specify an Scope and FilePath, use --help for more info")
   elif not options.scope:
      parser.error("[-] Please specify an Scope , use --help for more info")
   elif not options.filePath:
      parser.error("[-] Please specify an FilePath , use --help for more info")
   return options


def get_SubDomain(filePath):
   subDomainList = []
   with open(filePath,"r") as file:
    for list in file:
        subDomainList.append(list.strip())
   return subDomainList

def check_OutofScope(OutofScopeList,subDomainList):
      outScope = 0
      index = 0
      while (outScope + 1) != len(OutofScopeList):
         if index == len(subDomainList):
            outScope = outScope + 1
            index = 0
         for i in subDomainList:
             index = index + 1
             if i == OutofScopeList[outScope]:
                subDomainList.pop(index - 1)
      else:
         return subDomainList

def create_File(file,outputPath,countSubDomain):
   createFile = open(outputPath,"w")
   sleep(0.5)
   print("Creating File......")
   for i in file:
      createFile.write(i + "\n")
   createFile.close()
   sleep(0.5)
   print("Completed File Creation ! ")
   sleep(0.2)
   print("File Location : " + outputPath)
   print("Out of Scope Detected : " + str(countSubDomain-len(file)))

def sleep(seconds):
   time.sleep(seconds)

options = get_arguments()
scope = options.scope
filePath = options.filePath
outputPath = options.output
OutofScopeList = [item for item in scope.split(',')]
subDomainList = get_SubDomain(options.filePath)
countSubDomain = len(subDomainList)
checkOutofscopeList = check_OutofScope(OutofScopeList,subDomainList)

if outputPath:
      create_File(checkOutofscopeList,outputPath,countSubDomain)
else:
   for checkOutofscopeList in checkOutofscopeList :
      print(checkOutofscopeList)
