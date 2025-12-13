# Home Assistant Nmap Localnetwork integration
This Home Assistant integration provides a [Nmap](https://nmap.org/) network scanner information of all devices on your local network.

## Why?
This integration was made to save server resources on Home Assistant server by running Nmap in the other server. User can setup the other server for scanning with their own needs with available resources. After working configuration you can make automations to get you local network more secure. Examples:
- Alert when unknown device is found in your network
- Alert when security risk in your device is found
- Alert when important device is down

## Features
- Automatically updates the list of devices on a periodic basis.
- Displays the total number of devices currently identified on the network.
- Displays the last scanning time.

## Nmap Server installation
Before you can use the integration, you need to have the server configured in your local network for scanning and sharing the json data. Official [Nmap](https://nmap.org/) does not provide the json output, so i made the dotnet commandline application to convert Nmap xml output to json. You can use other methods to convert the xml output. The json data needs to be in this format:
***
```json
{
  "scan_time": "2025-12-13T14:13:02",
  "total_hosts": 1,
  "hosts": [
    {
      "ip": "192.168.1.1",
      "status": "up",
      "ports": [
        {
          "port_id": "80",
          "protocol": "tcp",
          "state": "open",
          "service": "http"
        },
        {
          "port_id": "443",
          "protocol": "tcp",
          "state": "open",
          "service": "http"
        }
      ]
    }
}
```

***
Server configuration:
1. Install the Nmap with your servers installation method
2. If your server has no web server installed, install nginx or what ever web server
3. Create shell script to run the Nmap and xml to json conversion. I have this in my script:
***
```sh
nmap -A -T3 -oX /tmp/local_network.xml 192.168.1.0/24
dotnet /opt/kaipio/nmap/xml2json.dll /tmp/local_network.xml /var/www/html/data/local_network.json
```
***
4. Test that the script is working by running it manually
5. Add script to crontab. I have this in my server:
```crontab
*/20 * * * * /opt/kaipio/nmap/script/gen_localmap.sh
```

## Installation through HACS (NOT AVAILABLE UNTIL THIS COMMENT IS REMOVED)
To install the nmap_localnetwork integration using HACS:

1. Open Home Assistant, go to HACS -> Integrations.
2. Search for Nmap Localnetwork and install it.
3. Restart Home Assistant.
4. After restart, add the integration from Settings -> Devices & services -> Add integration and add configuration, when asked. You need to have the whole URL to the json output and username & password if they are required.

## Manual Installation
To install this integration manually:

1. Copy the nmap_localnetwork directory into the custom_components directory of your Home Assistant installation.
2. Restart Home Assistant.
3. After restart, add the integration from Settings -> Devices & services -> Add integration and add configuration, when asked. You need to have the whole URL to the json output and username & password if they are required.

## TODO
1. Make changes to be approved to HACS

## Contributing
Contributions to this integration are welcome. Please refer to the project's GitHub repository for contributing guidelines.
