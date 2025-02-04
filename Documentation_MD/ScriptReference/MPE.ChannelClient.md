[ ]()

  * [Manual](../Manual/index.html)
  * [Scripting API](../ScriptReference/index.html)

  * [unity.com](https://unity.com/)

Version: **Unity 6** (6000.0)

  * Supported
  * Legacy

LanguageEnglish

  * [English]()

  * C#

[ ](https://docs.unity3d.com)

## Scripting API

Version: Unity 6 Select a different version

LanguageEnglish

  * [English]()

# ChannelClient

class in UnityEditor.MPE

Leave feedback

Suggest a change

## Success!

Thank you for helping us improve the quality of Unity Documentation. Although
we cannot accept all submissions, we do read each suggested change from our
users and will make updates where applicable.

Close

## Submission failed

For some reason your suggested change could not be submitted. Please <a>try
again</a> in a few minutes. And thank you for taking the time to help us
improve the quality of Unity Documentation.

Close

Your name Your email Suggestion* Submit suggestion

Cancel

[ ]()

### Description

ChannelClient is a WebSocket client that connects to Unity's
[ChannelService](MPE.ChannelService.html), which is a WebSocket server.

A ChannelClient is created on a specific channel. A channel name matches the
last part of a WebSocket URL. For example: 127.0.0.1:9090/<channelName>.  
  
The [EventService](MPE.EventService.html) is a ChannelClient connected to the
"events" channel.  
  
You can create custom channels using the
[ChannelService](MPE.ChannelService.html), and connect to them using a
ChannelClient. For information about creating channels, see
[ChannelService.GetOrCreateChannel](MPE.ChannelService.GetOrCreateChannel.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Text;
    using UnityEditor.MPE;
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;  
      
    public static class ChannelCommunicationDocExample
    {
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 1")]
        static void StartChannelService()
        {
            if (![ChannelService.IsRunning](MPE.ChannelService.IsRunning.html)())
            {
                [ChannelService.Start](MPE.ChannelService.Start.html)();
            }
            [Debug.Log](Debug.Log.html)($"[Step1] [ChannelService](MPE.ChannelService.html) Running: {[ChannelService.GetAddress](MPE.ChannelService.GetAddress.html)()}:{[ChannelService.GetPort](MPE.ChannelService.GetPort.html)()}");
        }  
      
        static int s_BinaryChannelId;
        static int s_StringChannelId;
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_DisconnectBinaryChannel;
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_DisconnectStringChannel;  
      
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 2")]
        static void SetupChannelService()
        {
            if (s_DisconnectBinaryChannel == null)
            {
                s_DisconnectBinaryChannel = [ChannelService.GetOrCreateChannel](MPE.ChannelService.GetOrCreateChannel.html)("custom_binary_ping_pong", HandleChannelBinaryMessage);
                s_BinaryChannelId = [ChannelService.ChannelNameToId](MPE.ChannelService.ChannelNameToId.html)("custom_binary_ping_pong");
            }
            [Debug.Log](Debug.Log.html)($"[Step2] Setup channel_custom_binary id: {s_BinaryChannelId}");  
      
            if (s_DisconnectStringChannel == null)
            {
                s_DisconnectStringChannel = [ChannelService.GetOrCreateChannel](MPE.ChannelService.GetOrCreateChannel.html)("custom_ascii_ping_pong", HandleChannelStringMessage);
                s_StringChannelId = [ChannelService.ChannelNameToId](MPE.ChannelService.ChannelNameToId.html)("custom_ascii_ping_pong");
            }
            [Debug.Log](Debug.Log.html)($"[Step2] Setup channel_custom_ascii id: {s_StringChannelId}");
        }  
      
        static void HandleChannelBinaryMessage(int connectionId, byte[] data)
        {
            var msg = "";
            for (var i = 0; i < Math.Min(10, data.Length); ++i)
            {
                msg += data[i].ToString();
            }
            [Debug.Log](Debug.Log.html)($"Channel Handling binary from connection {connectionId} - {data.Length} bytes - {msg}");  
      
            // [Client](PackageManager.Client.html) has sent a message (this is a ping)
            // Lets send back the same message (as a pong)
            [ChannelService.Send](MPE.ChannelService.Send.html)(connectionId, data);
        }  
      
        static void HandleChannelStringMessage(int connectionId, byte[] data)
        {
            // A new message is received.
            // Since our clients expects string data. Encode the data and send it back as a string:  
      
            var msgStr = Encoding.UTF8.GetString(data);
            [Debug.Log](Debug.Log.html)($"Channel Handling string from connection {connectionId} - {msgStr}");  
      
            // [Client](PackageManager.Client.html) has sent a message (this is a ping)
            // Lets send back the same message (as a pong)
            [ChannelService.Send](MPE.ChannelService.Send.html)(connectionId, msgStr);
        }  
      
        static [ChannelClient](MPE.ChannelClient.html) s_BinaryClient;
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_DisconnectBinaryClient;
        static [ChannelClient](MPE.ChannelClient.html) s_StringClient;
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_DisconnectStringClient;
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 3")]
        static void SetupChannelClient()
        {
            const bool autoTick = true;  
      
            if (s_BinaryClient == null)
            {
                s_BinaryClient = [ChannelClient.GetOrCreateClient](MPE.ChannelClient.GetOrCreateClient.html)("custom_binary_ping_pong");
                s_BinaryClient.Start(autoTick);
                s_DisconnectBinaryClient = s_BinaryClient.RegisterMessageHandler(HandleClientBinaryMessage);
            }
            [Debug.Log](Debug.Log.html)($"[Step3] Setup client for channel custom_binary_ping_pong. ClientId: {s_BinaryClient.clientId}");  
      
            if (s_StringClient == null)
            {
                s_StringClient = [ChannelClient.GetOrCreateClient](MPE.ChannelClient.GetOrCreateClient.html)("custom_ascii_ping_pong");
                s_StringClient.Start(autoTick);
                s_DisconnectStringClient = s_StringClient.RegisterMessageHandler(HandleClientStringMessage);
            }
            [Debug.Log](Debug.Log.html)($"[Step3] Setup client for channel custom_ascii_ping_pong. ClientId: {s_StringClient.clientId}");
        }  
      
        static void HandleClientBinaryMessage(byte[] data)
        {
            [Debug.Log](Debug.Log.html)($"Receiving pong binary data: {data} for clientId: {s_BinaryClient.clientId} with channelName: {s_BinaryClient.channelName}");
        }  
      
        static void HandleClientStringMessage(string data)
        {
            [Debug.Log](Debug.Log.html)($"Receiving pong data: {data} for clientId: {s_StringClient.clientId} with channelName: {s_StringClient.channelName}");
        }  
      
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 4")]
        static void ClientSendMessageToServer()
        {
            [Debug.Log](Debug.Log.html)("[Step 4]: Clients are sending data!");
            s_BinaryClient.Send(new byte[] { 0, 1, 2, 3, 4, 5, 6, 7 });
            s_StringClient.Send("Hello world!");
        }  
      
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 5")]
        static void CloseClients()
        {
            [Debug.Log](Debug.Log.html)("[Step 5]: Closing clients");
            s_DisconnectBinaryClient();
            s_BinaryClient.Close();  
      
            s_DisconnectStringClient();
            s_StringClient.Close();
        }  
      
        [[MenuItem](MenuItem.html)("ChannelDoc/Step 6")]
        static void CloseService()
        {
            [Debug.Log](Debug.Log.html)("[Step 6]: Closing clients");  
      
            s_DisconnectBinaryChannel();
            s_DisconnectStringChannel();  
      
            [ChannelService.Stop](MPE.ChannelService.Stop.html)();
        }
    }  
      
    /*
    When you execute the menu items one after the other, Unity prints the following messages to the Console window.  
      
    [Step1] [ChannelService](MPE.ChannelService.html) Running: 127.0.0.1:64647  
      
    [Step2] Setup channel_custom_binary id: -1698345965  
      
    [Step2] Setup channel_custom_ascii id: -930064725  
      
    [Step3] Setup client for channel custom_binary_ping_pong. ClientId: -1698345965  
      
    [Step3] Setup client for channel custom_ascii_ping_pong. ClientId: -930064725  
      
    [Step 4]: Clients are sending data!  
      
    Channel Handling binary from connection 1 - 8 bytes - 01234567  
      
    Channel Handling string from connection 2 - Hello world!  
      
    Receiving pong binary data: System.Byte[] for clientId: -1698345965 with channelName: custom_binary_ping_pong  
      
    Receiving pong data: Hello world! for clientId: -930064725 with channelName: custom_ascii_ping_pong  
      
    [Step 5]: Closing clients  
      
    [Step 6]: Closing clients  
      
    */
    

### Properties

[channelName](MPE.ChannelClient-channelName.html)| The name of the channel
this ChannelClient is connected to. The name matches the route of the URL used
to connect to Unity's ChannelService. For example, 127.0.0.1:8928/<my Channel
Name>.  
---|---  
[clientId](MPE.ChannelClient-clientId.html)| The channel ID, which essentially
a hash of the channel name. See ChannelService.ChannelNameToId.  
[isAutoTick](MPE.ChannelClient-isAutoTick.html)| Specifies whether Unity
processes (ticks) this ChannelClient's incoming and outgoing messages
automatically, or the user processes (ticks) them manually, either in the main
thread or a dedicated thread.  
  
### Public Methods

[Close](MPE.ChannelClient.Close.html)| Closes the ChannelClient. This closes
the WebSocket client but not the Channel in the ChannelService. Other
ChannelClients can still connect on the same Channel.  
---|---  
[GetChannelClientInfo](MPE.ChannelClient.GetChannelClientInfo.html)| Gets the
ChannelClientInfo for a specific channel.  
[IsConnected](MPE.ChannelClient.IsConnected.html)| Checks whether the
ChannelClient connected to a ChannelService.  
[NewRequestId](MPE.ChannelClient.NewRequestId.html)| Creates a unique request
ID for this ChannelClient in this instance of Unity. For more information
about requests, see ChannelClient.Request.  
[RegisterMessageHandler](MPE.ChannelClient.RegisterMessageHandler.html)|
Registers a new handler on a specific channel. The new handler is called
whenever a message is sent to the ChannelClient.  
[Send](MPE.ChannelClient.Send.html)| Sends an ASCII or binary message to the
ChannelService. Depending on how the channel's handler processes the message,
it may also be sent to other connections.  
[Start](MPE.ChannelClient.Start.html)| Starts an existing ChannelClient so it
listens to incoming and outgoing messages.  
[Stop](MPE.ChannelClient.Stop.html)| Stops a specific ChannelClient from
listening for new messages. This is different than ChannelClient.Close because
you can restart the channel client using ChannelClient.Start.  
[Tick](MPE.ChannelClient.Tick.html)| Ticks the ChannelClient. When you call
this method, it checks whether any incoming messages from the server need to
be processed, and whether any outgoing messages need to be sent to the server.  
[UnregisterMessageHandler](MPE.ChannelClient.UnregisterMessageHandler.html)|
Unregisters a specific channel handler from a ChannelClient.  
  
### Static Methods

[GetChannelClientList](MPE.ChannelClient.GetChannelClientList.html)| Gets
information for all ChannelClients running on a single instance of Unity.  
---|---  
[GetOrCreateClient](MPE.ChannelClient.GetOrCreateClient.html)| Creates a new
ChannelClient on a specific channel. If a client already exists, this method
gets the client.  
[Shutdown](MPE.ChannelClient.Shutdown.html)| Closes all ChannelClients in this
instance of Unity.  
  
Is something described here not working as you expect it to? It might be a
**Known Issue**. Please check with the Issue Tracker at
[issuetracker.unity3d.com](https://issuetracker.unity3d.com).

Copyright ©2005-2025 Unity Technologies. All rights reserved. Built from:
6000.0.36f1 (02b661dc617c). Built on: 2025-01-14.

[Tutorials](https://unity3d.com/learn) [Community
Answers](https://answers.unity3d.com) [Knowledge
Base](https://support.unity3d.com/hc/en-us)
[Forums](https://forum.unity3d.com) [Asset Store](https://unity3d.com/asset-
store) [Terms of use](https://docs.unity3d.com/Manual/TermsOfUse.html)
[Legal](https://unity.com/legal) [Privacy
Policy](https://unity.com/legal/privacy-policy)
[Cookies](https://unity.com/legal/cookie-policy) [Do Not Sell or Share My
Personal Information](https://unity.com/legal/do-not-sell-my-personal-
information)

[Your Privacy Choices (Cookie Settings)](javascript:void\(0\);)

