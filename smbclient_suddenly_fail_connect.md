> https://support.microsoft.com/en-us/help/204279/direct-hosting-of-smb-over-tcp-ip


## Direct hosting of SMB over TCP/IP
### Summary
Windows supports file and printer sharing traffic by using the Server Message Block (SMB) protocol directly hosted on TCP. This differs from earlier operating systems, in which SMB traffic requires the NetBIOS over TCP (NBT) protocol to work on a TCP/IP transport. Removing the NetBIOS transport has several advantages, including:
- Simplifying the transport of SMB traffic.
- Removing WINS and NetBIOS broadcast as a means of name resolution.
- Standardizing name resolution on DNS for file and printer sharing.
If both the direct hosted and NBT interfaces are enabled, both methods are tried at the same time and the first to respond is used. This allows Windows to function properly with operating systems that do not support direct hosting of SMB traffic.


### More Information
NetBIOS over TCP traditionally uses the following ports:

   nbname            137/UDP
   nbname            137/TCP
   nbdatagram        138/UDP
   nbsession         139/TCP
 
Direct hosted "NetBIOS-less" SMB traffic uses port 445 (TCP and UDP). In this situation, a four-byte header precedes the SMB traffic. The first byte of this header is always 0x00, and the next three bytes are the length of the remaining data.

Use the following steps to disable NetBIOS over TCP/IP; this procedure forces all SMB traffic to be direct hosted. Take care in implementing this setting because it causes the Windows-based computer to be unable to communicate with earlier operating systems using SMB traffic:

1. Click Start, point to Settings, and then click Network and Dial-up Connection.
2. Right-click Local Area Connection, and then click Properties.
3. Click Internet Protocol (TCP/IP), and then click Properties.
4. Click Advanced.
5. Click the WINS tab, and then click Disable NetBIOS over TCP/IP.

You can also disable NetBIOS over TCP/IP by using a DHCP server with Microsoft vendor-specific option code 1, ("Disable NetBIOS over TCP/IP"). Setting this option to a value of 2 disables NBT. For more information about using this method, refer to the DHCP Server Help file in Windows.

To determine if NetBIOS over TCP/IP is enabled on a Windows-based computer, issue a net config redirector or net config server command at a command prompt. The output shows bindings for the NetbiosSmb device (which is the "NetBIOS-less" transport) and for the NetBT_Tcpip device (which is the NetBIOS over TCP transport). For example, the following sample output shows both the direct hosted and the NBT transport bound to the adapter:

```
Workstation active on
      NetbiosSmb (000000000000)
      NetBT_Tcpip_{610E2A3A-16C7-4E66-A11D-A483A5468C10} (02004C4F4F50)
      NetBT_Tcpip_{CAF8956D-99FB-46E3-B04B-D4BB1AE93982} (009027CED4C2)
```

NetBT_Tcpip is bound to each adapter individually; an instance of NetBT_Tcpip is shown for each network adapter that it is bound to. NetbiosSmb is a global device, and is not bound on a per-adapter basis. This means that direct-hosted SMB's cannot be disabled in Windows without disabling File and Printer Sharing for Microsoft Networks completely.

Last Updated: Apr 17, 2018



> http://www.nynaeve.net/?p=93


Analysis of a networking problem: The case of the mysterious SMB connection resets (or “How to not design a network protocol”)
Recently, I had the unpleasant task of troubleshooting a particularly strange problem at work, in which a particular SMB-based file server would disconnect users if more than one user attempted to simultaneously initiate a file transfer. This would typically result as a file transfer (i.e. drag and drop file copy) initiated by Explorer failing with a “The specified network name is no longer available.” (error #64) dialog box. As this particular problem involved SMB traffic going through a fair amount of custom code we had written, being a VPN/remote access company (this particular problem was seemingly only occuring when using our VPN software), we (naturally) assumed that the issue was caused by some sort of bug in our software that was doing something to upset either the Windows SMB client or SMB server.

So, first things first; after doing initial troubleshooting, we obtained some packet captures of the problematic SMB server (and SMB clients), detailing just what was happening on the network when the problem occured.

Unfortunately, in this particular case, the packet captures did not really end up providing a whole lot of useful information; they did, however, succeed in raising more questions. What we observed is that in the middle of an SMB datastream, the SMB server would just mysteriously send a TCP RST packet, thereby forcibly closing the TCP connection on which SMB was running. This corresponded exactly with one of the file share clients getting the dreaded error #64 dialog, but there was no clue as to what the problem was. In this particular case, there was no packet loss to speak of, and nothing else to indicate some kind of connectivity problem; the SMB server just simply sent an RST seemingly out of the blue to one of the SMB clients shortly after a different SMB client attempted to initiate a file transfer.

To make matters worse, there was no correlation at all as to what the SMB client whose connection got killed was doing when the connection got reset. The client could be either submitting a read request for more data, waiting for a previously sent read request to finish processing, or doing any other operation; the SMB server would just mysteriously close the connection.

In this particular case, the problem would also only occur when SMB was used in conjunction with our VPN software. When the SMB server was accessed over the LAN, the SMB connection would operate fine in the presence of multiple concurrent users. Additionally, when the SMB server was used in conjunction with alternative remote access methods other than our standard VPN system, the problem would mysteriously vanish.

By this time, this problem was starting to look like a real nightmare. The information we had said that there was some kind of problem that was preventing SMB from being used with our VPN software (which obviously would need to be fixed, and quickly), and yet gave no actual leads as to what might cause the problem to occur. According to logs and packet captures, the SMB server would just arbitrarily reset connections of users connecting to SMB servers when used in conjunction with our VPN software.

Fortunately, we did eventually manage to duplicate the problem in-house with our own internal test network. This eventually turned out to be key to solving the problem, but did not (at least initially) provide any immediate new information. While it did prevent us from having to bother the customer this problem was originally impacting while troubleshooting, it did not immediately get us closer to understanding the problem. In the mean time, our industrious quality assurance group had engaged Microsoft in an attempt to see if there was any sort of known issue with SMB that might possibly explain this problem.

After spending a significant amount of time doing exhaustive code reviews of all of our code in the affected network path, and banging our collective heads on the wall while trying to understand just what might be causing the SMB server to kill off users of our VPN software, we eventually ended up hooking up a kernel debugger to an SMB server machine exhibiting this problem in order to see if I could find anything useful by debugging the SMB server (which is a kernel mode driver known as srv.sys). After not getting anywhere with that initially, I decided to try and trace the problem from the root of its observable effects; the reset TCP connection. Through the contact that our quality assurance group had made with Microsoft Product Support Services (PSS), Microsoft had supplied us with a couple of hotfixes for tcpip.sys (the Windows TCP stack) for various issues that ultimately turned out to be unrelated to the underlying trouble with SMB (and did not end up alleviating our problem). Although the hotfixes we received didn’t end up resolving our problem, we decided to take a closer look at what was happening inside the TCP state machine when the SMB connections were being reset.

This turned out to hit the metaphorical jackpot. I had set a breakpoint on every function in tcpip.sys that is responsible for flagging TCP connections for reset, and the call stack caught the SMB server (srv.sys) red-handed:

```
kd> k
ChildEBP RetAddr  
f4a4fa98 f4cad286 tcpip!SendRSTFromTCB
f4a4fac0 f4cb0ee3 tcpip!CloseTCB+0xbc
f4a4fad0 f4cb0ec7 tcpip!TryToCloseTCB+0x38
f4a4faf4 f4cace69 tcpip!TdiDisconnect+0x205
f4a4fb40 f4cabbed tcpip!TCPDisconnect+0xfd
f4a4fb5c 804e37f7 tcpip!TCPDispatchInternalDeviceControl+0x14d
f4a4fb6c f4c7d132 nt!IopfCallDriver+0x31
f4a4fb84 f4c7cd93 netbt!TdiDisconnect+0x10a
f4a4fbb4 f4c7d0b8 netbt!TcpDisconnect+0x40
f4a4fbd4 f4c7d017 netbt!DisconnectLower+0x42
f4a4fc14 f4c7d11f netbt!NbtDisconnect+0x339
f4a4fc44 f4c7ba5a netbt!NTDisconnect+0x4b
f4a4fc60 804e37f7 netbt!NbtDispatchInternalCtrl+0xb4
f4a4fc70 f43fb9c1 nt!IopfCallDriver+0x31
f4a4fc7c f441e8db srv!StartIoAndWait+0x1b
f4a4fcb0 f441f13e srv!SrvIssueDisconnectRequest+0x4d
f4a4fccc f43eed3e srv!SrvDoDisconnect+0x18
f4a4fce4 f440d3b5 srv!SrvCloseConnection+0xec
f4a4fd18 f44007ae srv!SrvCloseConnectionsFromClient+0x163
f4a4fd88 f43fba98 srv!BlockingSessionSetupAndX+0x274
```

As it turns out, the SMB server was explicitly disconnecting the pre-existing SMB client when the second SMB client tried to setup a session with the SMB server. This explains why even though the pre-existing SMB client was operating normally, not breaking the SMB protocol and running with no packet loss, it would mysteriously have its connection reset for apparently no good reason.

Further analysis on packet captures revealed that there was always a correlation to one client sending an SMB_SESSION_SETUP_ANDX command to the SMB server and all other clients on the SMB server being abortively disconnected. After digging around a bit more in srv.sys, it became clear that what was happening is that the SMB server would explicitly kill all SMB connections from an IPv4 address that was opening a new SMB session (via SMB_SESSION_SETUP_ANDX), except for the new SMB TCP connection. It turns out that this behavior is engaged if the SMB client sets the “VcNumber” field of the SMB_SESSION_SETUP_ANDX request to a zero value (which the Windows SMB redirector, mrxsmb.sys, does), and the client enables extended security on the connection (this is typically true for modern Windows versions, say Windows XP and Windows Server 2003).

This explains the problem that we were seeing. In one of the configurations, this customer was setup to have remote clients NAT’d behind a single LAN IP address. This, when combined with the SMB redirector sending a zero VcNumber field, resulted in the SMB server killing everyone else’s SMB connections (behind the NAT) when a new remote client opened an SMB connection through the NAT. Additionally, this also fit with an additional piece of information that we eventually uncovered from running into this trouble with customers; one customer in particular had an old Windows NT 4.0 fileserver which always worked perfectly over the VPN, but their newer Windows Server 2003 boxes would tend to experience these random disconnects. This was because NT4 doesn’t support the extended security options in the SMB protocol that Windows Server 2003 does, further lending credence to this particular theory. (It turns out that the code path that disconnects users for having a zero VcNumber is only active when extended security is being negotiated on an SMB session.)

Additionally, someone else at work managed to dig up knowledge base article 301673, otherwise titled “You cannot make more than one client connection over a NAT device”. Evidently, the problem is actually documented (and has been so since Windows 2000), though the listed workaround of using NetBIOS over TCP doesn’t seem to actually work. (Aside, it’s pretty silly that of all things, Microsoft is recommending that people fall back to NetBIOS. Haven’t we been trying to get rid of NetBIOS for years and years now…?).

Looking around a bit on Google for documentation about this particular problem, I ran into this article about SMB/CIFS which documented the shortcoming relating to SMB and NAT. Specifically:

```
Whenever a new transport-layer connection is created, the client is supposed to assign a new VC number. Note that the VcNumber on the initial connection is expected to be zero to indicate that the client is starting from scratch and is creating a new logical session. If an additional VC is given a VcNumber of zero, the server may assume that any existing connections with that same client are now bogus, and shut them down.

Why do such a thing?

The explanation given in the LANMAN documentation, the Leach/Naik IETF draft, and the SNIA doc is that clients may crash and reboot without first closing their connections. The zero VcNumber is the client’s signal to the server to clean up old connections. Reasonable or not, that’s the logic behind it. Unfortunately, it turns out that there are some annoying side-effects that result from this behavior. It is possible, for example, for one rogue application to completely disrupt SMB filesharing on a system simply by sending Session Setup requests with a zero VcNumber. Connecting to a server through a NAT (Network Address Translation) gateway is also problematic, since the NAT makes multiple clients appear to be a single client by placing them all behind the same IP address.
```


So, at least we (finally) found out just what was causing the mysterious resets. Apparently, from a protocol design standpoint, SMB is deliberately incompatible with NAT.

As someone who has designed network protocols before, this just completely blows my mind. I cannot think of any good reason to possibly justify breaking NAT, especially with the incredible proliferation of NAT devices in every day life (it seems like practically everyone has a cable/DSL/wireless router type device that does NAT today, not to mention the increased pressure to reuse IP addresses as pressure on the limited IPv4 address space grows). Not to mention that the Windows file sharing protocol has to be one of the most widely used networking protocols in the world. Breaking NAT for that (evidently just for the sake of breaking NAT!) just seems like such an incredibly horrible, not-well-thought-out design decision. Normally, I am usually fairly impressed by how well Microsoft designs their software (particularly their kernel software), but this particular little part of the SMB protocol design is just uncharacteristically completely wrong.

Even more unbelievably, the stated reason that Microsoft gave for this behavior is an optimization to handle the case where the user’s computer has crashed, rebooted, and reconnected to the server before the SMB server’s TCP stack has noticed that the crashed SMB client’s TCP connection has gone away. Evidently, conserving server resources in the case of a client crash is more important than being compatible with NAT. One has to wonder how unstable the Microsoft SMB redirector must have been at the time that this “feature” was added to the SMB protocol to make anyone in their right mind consider such an absolutely ridiculous, mind-bogglingly bad tradeoff.

To date, we haven’t had a whole lot of luck in trying to get Microsoft to fix this “minor” problem in SMB. I’ll post an update if we ever succeed, but as of now, things are unfortunately not looking very promising on that front.
