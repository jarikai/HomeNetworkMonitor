
// NOTE: Generated code may require at least .NET Framework 4.5 or .NET Core/Standard 2.0.
/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
[System.Xml.Serialization.XmlRootAttribute(Namespace = "", IsNullable = false)]
public partial class nmaprun
{

    private nmaprunScaninfo scaninfoField;

    private nmaprunVerbose verboseField;

    private nmaprunDebugging debuggingField;

    private nmaprunHosthint[] hosthintField;

    private nmaprunHost[] hostField;

    private nmaprunScript[] postscriptField;

    private nmaprunRunstats runstatsField;

    private string scannerField;

    private string argsField;

    private uint startField;

    private string startstrField;

    private decimal versionField;

    private decimal xmloutputversionField;

    /// <remarks/>
    public nmaprunScaninfo scaninfo
    {
        get
        {
            return this.scaninfoField;
        }
        set
        {
            this.scaninfoField = value;
        }
    }

    /// <remarks/>
    public nmaprunVerbose verbose
    {
        get
        {
            return this.verboseField;
        }
        set
        {
            this.verboseField = value;
        }
    }

    /// <remarks/>
    public nmaprunDebugging debugging
    {
        get
        {
            return this.debuggingField;
        }
        set
        {
            this.debuggingField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("hosthint")]
    public nmaprunHosthint[] hosthint
    {
        get
        {
            return this.hosthintField;
        }
        set
        {
            this.hosthintField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("host")]
    public nmaprunHost[] host
    {
        get
        {
            return this.hostField;
        }
        set
        {
            this.hostField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("script", IsNullable = false)]
    public nmaprunScript[] postscript
    {
        get
        {
            return this.postscriptField;
        }
        set
        {
            this.postscriptField = value;
        }
    }

    /// <remarks/>
    public nmaprunRunstats runstats
    {
        get
        {
            return this.runstatsField;
        }
        set
        {
            this.runstatsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string scanner
    {
        get
        {
            return this.scannerField;
        }
        set
        {
            this.scannerField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string args
    {
        get
        {
            return this.argsField;
        }
        set
        {
            this.argsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint start
    {
        get
        {
            return this.startField;
        }
        set
        {
            this.startField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string startstr
    {
        get
        {
            return this.startstrField;
        }
        set
        {
            this.startstrField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public decimal version
    {
        get
        {
            return this.versionField;
        }
        set
        {
            this.versionField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public decimal xmloutputversion
    {
        get
        {
            return this.xmloutputversionField;
        }
        set
        {
            this.xmloutputversionField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunScaninfo
{

    private string typeField;

    private string protocolField;

    private ushort numservicesField;

    private string servicesField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type
    {
        get
        {
            return this.typeField;
        }
        set
        {
            this.typeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string protocol
    {
        get
        {
            return this.protocolField;
        }
        set
        {
            this.protocolField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort numservices
    {
        get
        {
            return this.numservicesField;
        }
        set
        {
            this.numservicesField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string services
    {
        get
        {
            return this.servicesField;
        }
        set
        {
            this.servicesField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunVerbose
{

    private byte levelField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte level
    {
        get
        {
            return this.levelField;
        }
        set
        {
            this.levelField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunDebugging
{

    private byte levelField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte level
    {
        get
        {
            return this.levelField;
        }
        set
        {
            this.levelField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHosthint
{

    private nmaprunHosthintStatus statusField;

    private nmaprunHosthintAddress[] addressField;

    private object hostnamesField;

    /// <remarks/>
    public nmaprunHosthintStatus status
    {
        get
        {
            return this.statusField;
        }
        set
        {
            this.statusField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("address")]
    public nmaprunHosthintAddress[] address
    {
        get
        {
            return this.addressField;
        }
        set
        {
            this.addressField = value;
        }
    }

    /// <remarks/>
    public object hostnames
    {
        get
        {
            return this.hostnamesField;
        }
        set
        {
            this.hostnamesField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHosthintStatus
{

    private string stateField;

    private string reasonField;

    private byte reason_ttlField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string reason
    {
        get
        {
            return this.reasonField;
        }
        set
        {
            this.reasonField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte reason_ttl
    {
        get
        {
            return this.reason_ttlField;
        }
        set
        {
            this.reason_ttlField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHosthintAddress
{

    private string addrField;

    private string addrtypeField;

    private string vendorField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string addr
    {
        get
        {
            return this.addrField;
        }
        set
        {
            this.addrField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string addrtype
    {
        get
        {
            return this.addrtypeField;
        }
        set
        {
            this.addrtypeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string vendor
    {
        get
        {
            return this.vendorField;
        }
        set
        {
            this.vendorField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHost
{

    private nmaprunHostStatus statusField;

    private nmaprunHostAddress[] addressField;

    private object hostnamesField;

    private nmaprunHostPorts portsField;

    private nmaprunHostOS osField;

    private nmaprunHostUptime uptimeField;

    private nmaprunHostDistance distanceField;

    private nmaprunHostTcpsequence tcpsequenceField;

    private nmaprunHostIpidsequence ipidsequenceField;

    private nmaprunHostTcptssequence tcptssequenceField;

    private nmaprunHostScript[] hostscriptField;

    private nmaprunHostTrace traceField;

    private nmaprunHostTimes timesField;

    private uint starttimeField;

    private uint endtimeField;

    /// <remarks/>
    public nmaprunHostStatus status
    {
        get
        {
            return this.statusField;
        }
        set
        {
            this.statusField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("address")]
    public nmaprunHostAddress[] address
    {
        get
        {
            return this.addressField;
        }
        set
        {
            this.addressField = value;
        }
    }

    /// <remarks/>
    public object hostnames
    {
        get
        {
            return this.hostnamesField;
        }
        set
        {
            this.hostnamesField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostPorts ports
    {
        get
        {
            return this.portsField;
        }
        set
        {
            this.portsField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostOS os
    {
        get
        {
            return this.osField;
        }
        set
        {
            this.osField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostUptime uptime
    {
        get
        {
            return this.uptimeField;
        }
        set
        {
            this.uptimeField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostDistance distance
    {
        get
        {
            return this.distanceField;
        }
        set
        {
            this.distanceField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostTcpsequence tcpsequence
    {
        get
        {
            return this.tcpsequenceField;
        }
        set
        {
            this.tcpsequenceField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostIpidsequence ipidsequence
    {
        get
        {
            return this.ipidsequenceField;
        }
        set
        {
            this.ipidsequenceField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostTcptssequence tcptssequence
    {
        get
        {
            return this.tcptssequenceField;
        }
        set
        {
            this.tcptssequenceField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlArrayItemAttribute("script", IsNullable = false)]
    public nmaprunHostScript[] hostscript
    {
        get
        {
            return this.hostscriptField;
        }
        set
        {
            this.hostscriptField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostTrace trace
    {
        get
        {
            return this.traceField;
        }
        set
        {
            this.traceField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostTimes times
    {
        get
        {
            return this.timesField;
        }
        set
        {
            this.timesField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint starttime
    {
        get
        {
            return this.starttimeField;
        }
        set
        {
            this.starttimeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint endtime
    {
        get
        {
            return this.endtimeField;
        }
        set
        {
            this.endtimeField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostStatus
{

    private string stateField;

    private string reasonField;

    private byte reason_ttlField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string reason
    {
        get
        {
            return this.reasonField;
        }
        set
        {
            this.reasonField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte reason_ttl
    {
        get
        {
            return this.reason_ttlField;
        }
        set
        {
            this.reason_ttlField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostAddress
{

    private string addrField;

    private string addrtypeField;

    private string vendorField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string addr
    {
        get
        {
            return this.addrField;
        }
        set
        {
            this.addrField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string addrtype
    {
        get
        {
            return this.addrtypeField;
        }
        set
        {
            this.addrtypeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string vendor
    {
        get
        {
            return this.vendorField;
        }
        set
        {
            this.vendorField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPorts
{

    private nmaprunHostPortsExtraports[] extraportsField;

    private nmaprunHostPortsPort[] portField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("extraports")]
    public nmaprunHostPortsExtraports[] extraports
    {
        get
        {
            return this.extraportsField;
        }
        set
        {
            this.extraportsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("port")]
    public nmaprunHostPortsPort[] port
    {
        get
        {
            return this.portField;
        }
        set
        {
            this.portField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsExtraports
{

    private nmaprunHostPortsExtraportsExtrareasons extrareasonsField;

    private string stateField;

    private ushort countField;

    /// <remarks/>
    public nmaprunHostPortsExtraportsExtrareasons extrareasons
    {
        get
        {
            return this.extrareasonsField;
        }
        set
        {
            this.extrareasonsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort count
    {
        get
        {
            return this.countField;
        }
        set
        {
            this.countField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsExtraportsExtrareasons
{

    private string reasonField;

    private ushort countField;

    private string protoField;

    private string portsField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string reason
    {
        get
        {
            return this.reasonField;
        }
        set
        {
            this.reasonField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort count
    {
        get
        {
            return this.countField;
        }
        set
        {
            this.countField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string proto
    {
        get
        {
            return this.protoField;
        }
        set
        {
            this.protoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string ports
    {
        get
        {
            return this.portsField;
        }
        set
        {
            this.portsField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPort
{

    private nmaprunHostPortsPortState stateField;

    private nmaprunHostPortsPortService serviceField;

    private nmaprunHostPortsPortScript[] scriptField;

    private string protocolField;

    private ushort portidField;

    /// <remarks/>
    public nmaprunHostPortsPortState state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostPortsPortService service
    {
        get
        {
            return this.serviceField;
        }
        set
        {
            this.serviceField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("script")]
    public nmaprunHostPortsPortScript[] script
    {
        get
        {
            return this.scriptField;
        }
        set
        {
            this.scriptField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string protocol
    {
        get
        {
            return this.protocolField;
        }
        set
        {
            this.protocolField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort portid
    {
        get
        {
            return this.portidField;
        }
        set
        {
            this.portidField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortState
{

    private string stateField;

    private string reasonField;

    private byte reason_ttlField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string reason
    {
        get
        {
            return this.reasonField;
        }
        set
        {
            this.reasonField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte reason_ttl
    {
        get
        {
            return this.reason_ttlField;
        }
        set
        {
            this.reason_ttlField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortService
{

    private string[] cpeField;

    private string nameField;

    private string methodField;

    private byte confField;

    private string productField;

    private string servicefpField;

    private string tunnelField;

    private string versionField;

    private string extrainfoField;

    private string ostypeField;

    private string hostnameField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("cpe")]
    public string[] cpe
    {
        get
        {
            return this.cpeField;
        }
        set
        {
            this.cpeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name
    {
        get
        {
            return this.nameField;
        }
        set
        {
            this.nameField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string method
    {
        get
        {
            return this.methodField;
        }
        set
        {
            this.methodField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte conf
    {
        get
        {
            return this.confField;
        }
        set
        {
            this.confField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string product
    {
        get
        {
            return this.productField;
        }
        set
        {
            this.productField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string servicefp
    {
        get
        {
            return this.servicefpField;
        }
        set
        {
            this.servicefpField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string tunnel
    {
        get
        {
            return this.tunnelField;
        }
        set
        {
            this.tunnelField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string version
    {
        get
        {
            return this.versionField;
        }
        set
        {
            this.versionField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string extrainfo
    {
        get
        {
            return this.extrainfoField;
        }
        set
        {
            this.extrainfoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string ostype
    {
        get
        {
            return this.ostypeField;
        }
        set
        {
            this.ostypeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string hostname
    {
        get
        {
            return this.hostnameField;
        }
        set
        {
            this.hostnameField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScript
{

    private object[] itemsField;

    private string idField;

    private string outputField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem", typeof(nmaprunHostPortsPortScriptElem))]
    [System.Xml.Serialization.XmlElementAttribute("table", typeof(nmaprunHostPortsPortScriptTable))]
    public object[] Items
    {
        get
        {
            return this.itemsField;
        }
        set
        {
            this.itemsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id
    {
        get
        {
            return this.idField;
        }
        set
        {
            this.idField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string output
    {
        get
        {
            return this.outputField;
        }
        set
        {
            this.outputField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTable
{

    private object[] itemsField;

    private string keyField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem", typeof(nmaprunHostPortsPortScriptTableElem))]
    [System.Xml.Serialization.XmlElementAttribute("table", typeof(nmaprunHostPortsPortScriptTableTable))]
    public object[] Items
    {
        get
        {
            return this.itemsField;
        }
        set
        {
            this.itemsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTableElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTableTable
{

    private object[] itemsField;

    private string keyField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem", typeof(nmaprunHostPortsPortScriptTableTableElem))]
    [System.Xml.Serialization.XmlElementAttribute("table", typeof(nmaprunHostPortsPortScriptTableTableTable))]
    public object[] Items
    {
        get
        {
            return this.itemsField;
        }
        set
        {
            this.itemsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTableTableElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTableTableTable
{

    private nmaprunHostPortsPortScriptTableTableTableElem[] elemField;

    private string keyField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem")]
    public nmaprunHostPortsPortScriptTableTableTableElem[] elem
    {
        get
        {
            return this.elemField;
        }
        set
        {
            this.elemField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostPortsPortScriptTableTableTableElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostOS
{

    private nmaprunHostOSPortused[] portusedField;

    private nmaprunHostOSOsmatch[] osmatchField;

    private nmaprunHostOSOsfingerprint osfingerprintField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("portused")]
    public nmaprunHostOSPortused[] portused
    {
        get
        {
            return this.portusedField;
        }
        set
        {
            this.portusedField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("osmatch")]
    public nmaprunHostOSOsmatch[] osmatch
    {
        get
        {
            return this.osmatchField;
        }
        set
        {
            this.osmatchField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostOSOsfingerprint osfingerprint
    {
        get
        {
            return this.osfingerprintField;
        }
        set
        {
            this.osfingerprintField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostOSPortused
{

    private string stateField;

    private string protoField;

    private ushort portidField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string state
    {
        get
        {
            return this.stateField;
        }
        set
        {
            this.stateField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string proto
    {
        get
        {
            return this.protoField;
        }
        set
        {
            this.protoField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort portid
    {
        get
        {
            return this.portidField;
        }
        set
        {
            this.portidField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostOSOsmatch
{

    private nmaprunHostOSOsmatchOsclass[] osclassField;

    private string nameField;

    private byte accuracyField;

    private uint lineField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("osclass")]
    public nmaprunHostOSOsmatchOsclass[] osclass
    {
        get
        {
            return this.osclassField;
        }
        set
        {
            this.osclassField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string name
    {
        get
        {
            return this.nameField;
        }
        set
        {
            this.nameField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte accuracy
    {
        get
        {
            return this.accuracyField;
        }
        set
        {
            this.accuracyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint line
    {
        get
        {
            return this.lineField;
        }
        set
        {
            this.lineField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostOSOsmatchOsclass
{

    private string[] cpeField;

    private string typeField;

    private string vendorField;

    private string osfamilyField;

    private byte accuracyField;

    private string osgenField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("cpe")]
    public string[] cpe
    {
        get
        {
            return this.cpeField;
        }
        set
        {
            this.cpeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string type
    {
        get
        {
            return this.typeField;
        }
        set
        {
            this.typeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string vendor
    {
        get
        {
            return this.vendorField;
        }
        set
        {
            this.vendorField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string osfamily
    {
        get
        {
            return this.osfamilyField;
        }
        set
        {
            this.osfamilyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte accuracy
    {
        get
        {
            return this.accuracyField;
        }
        set
        {
            this.accuracyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string osgen
    {
        get
        {
            return this.osgenField;
        }
        set
        {
            this.osgenField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostOSOsfingerprint
{

    private string fingerprintField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string fingerprint
    {
        get
        {
            return this.fingerprintField;
        }
        set
        {
            this.fingerprintField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostUptime
{

    private uint secondsField;

    private string lastbootField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint seconds
    {
        get
        {
            return this.secondsField;
        }
        set
        {
            this.secondsField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string lastboot
    {
        get
        {
            return this.lastbootField;
        }
        set
        {
            this.lastbootField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostDistance
{

    private byte valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostTcpsequence
{

    private ushort indexField;

    private string difficultyField;

    private string valuesField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort index
    {
        get
        {
            return this.indexField;
        }
        set
        {
            this.indexField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string difficulty
    {
        get
        {
            return this.difficultyField;
        }
        set
        {
            this.difficultyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string values
    {
        get
        {
            return this.valuesField;
        }
        set
        {
            this.valuesField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostIpidsequence
{

    private string classField;

    private string valuesField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string @class
    {
        get
        {
            return this.classField;
        }
        set
        {
            this.classField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string values
    {
        get
        {
            return this.valuesField;
        }
        set
        {
            this.valuesField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostTcptssequence
{

    private string classField;

    private string valuesField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string @class
    {
        get
        {
            return this.classField;
        }
        set
        {
            this.classField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string values
    {
        get
        {
            return this.valuesField;
        }
        set
        {
            this.valuesField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostScript
{

    private nmaprunHostScriptElem[] elemField;

    private nmaprunHostScriptTable tableField;

    private string[] textField;

    private string idField;

    private string outputField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem")]
    public nmaprunHostScriptElem[] elem
    {
        get
        {
            return this.elemField;
        }
        set
        {
            this.elemField = value;
        }
    }

    /// <remarks/>
    public nmaprunHostScriptTable table
    {
        get
        {
            return this.tableField;
        }
        set
        {
            this.tableField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string[] Text
    {
        get
        {
            return this.textField;
        }
        set
        {
            this.textField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id
    {
        get
        {
            return this.idField;
        }
        set
        {
            this.idField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string output
    {
        get
        {
            return this.outputField;
        }
        set
        {
            this.outputField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostScriptElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostScriptTable
{

    private string elemField;

    private ushort keyField;

    /// <remarks/>
    public string elem
    {
        get
        {
            return this.elemField;
        }
        set
        {
            this.elemField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostTrace
{

    private nmaprunHostTraceHop hopField;

    /// <remarks/>
    public nmaprunHostTraceHop hop
    {
        get
        {
            return this.hopField;
        }
        set
        {
            this.hopField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostTraceHop
{

    private byte ttlField;

    private string ipaddrField;

    private decimal rttField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte ttl
    {
        get
        {
            return this.ttlField;
        }
        set
        {
            this.ttlField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string ipaddr
    {
        get
        {
            return this.ipaddrField;
        }
        set
        {
            this.ipaddrField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public decimal rtt
    {
        get
        {
            return this.rttField;
        }
        set
        {
            this.rttField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunHostTimes
{

    private uint srttField;

    private uint rttvarField;

    private uint toField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint srtt
    {
        get
        {
            return this.srttField;
        }
        set
        {
            this.srttField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint rttvar
    {
        get
        {
            return this.rttvarField;
        }
        set
        {
            this.rttvarField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint to
    {
        get
        {
            return this.toField;
        }
        set
        {
            this.toField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunScript
{

    private nmaprunScriptTable[] tableField;

    private string idField;

    private string outputField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("table")]
    public nmaprunScriptTable[] table
    {
        get
        {
            return this.tableField;
        }
        set
        {
            this.tableField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string id
    {
        get
        {
            return this.idField;
        }
        set
        {
            this.idField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string output
    {
        get
        {
            return this.outputField;
        }
        set
        {
            this.outputField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunScriptTable
{

    private string[] elemField;

    private nmaprunScriptTableTable[] tableField;

    private string keyField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem")]
    public string[] elem
    {
        get
        {
            return this.elemField;
        }
        set
        {
            this.elemField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("table")]
    public nmaprunScriptTableTable[] table
    {
        get
        {
            return this.tableField;
        }
        set
        {
            this.tableField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunScriptTableTable
{

    private nmaprunScriptTableTableElem[] elemField;

    private string keyField;

    /// <remarks/>
    [System.Xml.Serialization.XmlElementAttribute("elem")]
    public nmaprunScriptTableTableElem[] elem
    {
        get
        {
            return this.elemField;
        }
        set
        {
            this.elemField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunScriptTableTableElem
{

    private string keyField;

    private string valueField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string key
    {
        get
        {
            return this.keyField;
        }
        set
        {
            this.keyField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlTextAttribute()]
    public string Value
    {
        get
        {
            return this.valueField;
        }
        set
        {
            this.valueField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunRunstats
{

    private nmaprunRunstatsFinished finishedField;

    private nmaprunRunstatsHosts hostsField;

    /// <remarks/>
    public nmaprunRunstatsFinished finished
    {
        get
        {
            return this.finishedField;
        }
        set
        {
            this.finishedField = value;
        }
    }

    /// <remarks/>
    public nmaprunRunstatsHosts hosts
    {
        get
        {
            return this.hostsField;
        }
        set
        {
            this.hostsField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunRunstatsFinished
{

    private uint timeField;

    private string timestrField;

    private string summaryField;

    private decimal elapsedField;

    private string exitField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public uint time
    {
        get
        {
            return this.timeField;
        }
        set
        {
            this.timeField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string timestr
    {
        get
        {
            return this.timestrField;
        }
        set
        {
            this.timestrField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string summary
    {
        get
        {
            return this.summaryField;
        }
        set
        {
            this.summaryField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public decimal elapsed
    {
        get
        {
            return this.elapsedField;
        }
        set
        {
            this.elapsedField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public string exit
    {
        get
        {
            return this.exitField;
        }
        set
        {
            this.exitField = value;
        }
    }
}

/// <remarks/>
[System.SerializableAttribute()]
[System.ComponentModel.DesignerCategoryAttribute("code")]
[System.Xml.Serialization.XmlTypeAttribute(AnonymousType = true)]
public partial class nmaprunRunstatsHosts
{

    private byte upField;

    private byte downField;

    private ushort totalField;

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte up
    {
        get
        {
            return this.upField;
        }
        set
        {
            this.upField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public byte down
    {
        get
        {
            return this.downField;
        }
        set
        {
            this.downField = value;
        }
    }

    /// <remarks/>
    [System.Xml.Serialization.XmlAttributeAttribute()]
    public ushort total
    {
        get
        {
            return this.totalField;
        }
        set
        {
            this.totalField = value;
        }
    }
}

