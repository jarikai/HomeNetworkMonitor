using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Globalization;
using System.Reflection;
using System.Xml;
using System.Xml.Serialization;

if (args.Length < 2)
{
    var versionString = Assembly.GetEntryAssembly()?
                            .GetCustomAttribute<AssemblyInformationalVersionAttribute>()?
                            .InformationalVersion
                            .ToString();

    Console.WriteLine($"xml2json v{versionString}");
    Console.WriteLine("-------------");
    Console.WriteLine("\nUsage:");
    Console.WriteLine("  xml2json <xmlfilename> <jsonfilename>");
    Console.WriteLine("\nOr generate test json:");
    Console.WriteLine("  xml2json test <jsonfilename>");
    return;
}

bool generateTest = args[0].ToLower(CultureInfo.InvariantCulture) == "test";

string xmlFilename = args[0];
string jsonFilename = args[1];

XmlReaderSettings settings = new()
{
    DtdProcessing = DtdProcessing.Ignore,
    MaxCharactersFromEntities = 1024,
    IgnoreWhitespace = true,
    IgnoreComments = true
};

if (!generateTest)
{
    using (var reader = XmlReader.Create(xmlFilename, settings))
    {
        try
        {
            var serializer = new XmlSerializer(typeof(nmaprun));
            serializer.UnknownNode += new
            XmlNodeEventHandler(serializer_UnknownNode);
            serializer.UnknownAttribute += new
            XmlAttributeEventHandler(serializer_UnknownAttribute);
            var nmap = (nmaprun)serializer.Deserialize(reader);


            if (nmap != null)
            {
                string jsonContent = JsonConvert.SerializeObject(nmap, Newtonsoft.Json.Formatting.Indented);
                File.WriteAllText(jsonFilename, jsonContent);

                Console.WriteLine($"File {xmlFilename} converted to {jsonFilename}");
            }
            else
            {
                Console.WriteLine("Failed to deserialize the XML file.");
                return;

            }
        }
        catch (Exception)
        {
            throw;
        }
    }
}
else
{
    // Generate test JSON
    var testNmap = new nmaprun
    {
        scanner = "nmap",
        args = "-sV -oX test.xml scanme.nmap.org",
        start = 1616161616,
        version = 7,
        xmloutputversion = 1,

        // Add host data
        host = new nmaprunHost[]
        {
            new nmaprunHost
            {
                starttime = 1616161616,
                endtime = 1616161620,
                address = new nmaprunHostAddress[]
                {
                    new nmaprunHostAddress
                    {
                        addr = "127.0.0.1",
                        addrtype = "ipv4"
                    }
                },
                hostnames = new(),
                status = new nmaprunHostStatus
                {
                    state = "up",
                    reason = "localhost"
                },
                ports = new nmaprunHostPorts()            
            }
        },

        // Add runstats
        runstats = new nmaprunRunstats
        {
            finished = new nmaprunRunstatsFinished
            {
                time = 1616161620,
                timestr = "Wed Mar 17 12:00:00 2021",
                summary = "Nmap done at Wed Mar 17 12:00:00 2021; 1 IP address (1 host up) scanned in 4.00 seconds",
                elapsed = 4.00m,
                exit = "success"
            },
            hosts = new nmaprunRunstatsHosts
            {
                up = 1,
                down = 0,
                total = 1
            }
        }
    };


    string jsonContent = JsonConvert.SerializeObject(testNmap, Newtonsoft.Json.Formatting.Indented);
    File.WriteAllText(jsonFilename, jsonContent);
    Console.WriteLine($"Test JSON file {jsonFilename} generated.");
}


void serializer_UnknownNode
    (object sender, XmlNodeEventArgs e)
{
    Console.WriteLine("Unknown Node:" + e.Name + "\t" + e.Text);
}

void serializer_UnknownAttribute
(object sender, XmlAttributeEventArgs e)
{
    System.Xml.XmlAttribute attr = e.Attr;
    Console.WriteLine("Unknown attribute " +
    attr.Name + "='" + attr.Value + "'");
}