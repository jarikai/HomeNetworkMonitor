# Nmap xml to json convertter
This is the dotnet commandline app to convert Nmap xml output to json format. It was made for the Home Assistant custom integration Home Network Monitor.

## Installation
- Install the latest dotnet runtime version in your server
- Install the latest dotnet SDK in your development enviroment
- Build the application and test it in your development enviroment
- Publish the application and copy the output to your server

## Usage
- Application has test feature to build the valid json output file for testing. Test is created by executing command:
```
dotnet nmapxml2json.dll test test.json
```
- To generate real json data from Nmap xml output, use command:
```
dotnet nmapxml2json.dll path_to_nmap_output.xml path_to_result.json
```
