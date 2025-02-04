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

# EventService

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

The EventService is a singleton implementation of a
[ChannelClient](MPE.ChannelClient.html) that runs on all instances of Unity.
It is connected to the "events" channel and allows a Unity instance to send
JSON messages to other [EventService](MPE.EventService.html)s in external
process, or other instances of Unity.

The [EventService](MPE.EventService.html) can send fire-and-forget messages
(see [EventService.Emit](MPE.EventService.Emit.html)), or request information
or from a single client (see
[EventService.Request](MPE.EventService.Request.html)).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEngine;
    using UnityEditor.MPE;
    using [System](Rendering.VirtualTexturing.System.html);  
      
    public static class EventServiceDocExample
    {
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_CustomLogEventDisconnect;
        static [Action](Unity.Android.Gradle.Manifest.Action.html) s_PingPongEventDisconnect;  
      
        [[MenuItem](MenuItem.html)("EventServiceDoc/Step 0")]
        static void StartChannelService()
        {
            if (![ChannelService.IsRunning](MPE.ChannelService.IsRunning.html)())
            {
                [ChannelService.Start](MPE.ChannelService.Start.html)();
            }
            [Debug.Log](Debug.Log.html)($"[Step 0] [ChannelService](MPE.ChannelService.html) Running: {[ChannelService.GetAddress](MPE.ChannelService.GetAddress.html)()}:{[ChannelService.GetPort](MPE.ChannelService.GetPort.html)()}");
        }  
      
        [[MenuItem](MenuItem.html)("EventServiceDoc/Step 1")]
        static void SetupEventServiceHandlers()
        {
            [Debug.Log](Debug.Log.html)("[Step 1] Setup handlers");
            s_CustomLogEventDisconnect = [EventService.RegisterEventHandler](MPE.EventService.RegisterEventHandler.html)("custom_log", (eventType, args) => {
                [Debug.Log](Debug.Log.html)($"Log a {eventType} {args[0]}");
            });  
      
            s_PingPongEventDisconnect = [EventService.RegisterEventHandler](MPE.EventService.RegisterEventHandler.html)("pingpong", (eventType, args) =>
            {
                [Debug.Log](Debug.Log.html)($"Receive a {eventType} {args[0]}");
                return "pong!";
            });
        }  
      
        [[MenuItem](MenuItem.html)("EventServiceDoc/Step 2")]
        static void EmitMessage()
        {
            [Debug.Log](Debug.Log.html)("[Step 2] Emitting a custom log");
            [EventService.Emit](MPE.EventService.Emit.html)("custom_log", "Hello world!", -1, [EventDataSerialization.JsonUtility](MPE.EventDataSerialization.JsonUtility.html));
        }  
      
        [[MenuItem](MenuItem.html)("EventServiceDoc/Step 3")]
        static void SendRequest()
        {
            [Debug.Log](Debug.Log.html)("[Step 3] Sending a request");
            [EventService.Request](MPE.EventService.Request.html)("pingpong", (err, data) =>
            {
                [Debug.Log](Debug.Log.html)($"[Request](PackageManager.Requests.Request.html) fulfilled: {data[0]}");
            },
                "ping", -1, [EventDataSerialization.JsonUtility](MPE.EventDataSerialization.JsonUtility.html));
        }  
      
        [[MenuItem](MenuItem.html)("EventServiceDoc/Step 4")]
        static void CloseHandlers()
        {
            [Debug.Log](Debug.Log.html)("[Step 4] Closing all [Event](Event.html) handlers");
            s_CustomLogEventDisconnect();
            s_PingPongEventDisconnect();
        }
    }  
      
    /*  
      
    When you execute the five menu items one after the other, Unity prints the following messages to the Console window:  
      
    [Step 0] [ChannelService](MPE.ChannelService.html) Running: 127.0.0.1:65000  
      
    [Step 1] Setup handlers  
      
    [Step 2] Emitting a custom log  
      
    Log a custom_log Hello world!  
      
    [Step 3] Sending a request  
      
    Receive a pingpong ping  
      
    [Request](PackageManager.Requests.Request.html) fulfilled: pong!  
      
    [Step 4] Closing all [Event](Event.html) handlers  
      
    */
    

### Static Properties

[isConnected](MPE.EventService-isConnected.html)| The EventService connected
to the ChannelService's "events" channel.  
---|---  
  
### Static Methods

[CancelRequest](MPE.EventService.CancelRequest.html)| Checks whether there is
a pending request for a specific event and, if there is, cancels it. See
EventService.Request for more details on Request.  
---|---  
[Clear](MPE.EventService.Clear.html)| Clear all pending Requests.  
[Close](MPE.EventService.Close.html)| Closes the EventService, terminates
connections to the ChannelService, and ensures that no more handlers are
processed.  
[Emit](MPE.EventService.Emit.html)| Sends a fire-and-forget message to all
ChannelClients connected to the "events" route.  
[IsRequestPending](MPE.EventService.IsRequestPending.html)| Checks whether a
request is pending on a specific event. For more information about Request,
see EventService.Request.  
[Log](MPE.EventService.Log.html)| Sends a log message to the ChannelService.
Log messages are printed to the Console window.  
[RegisterEventHandler](MPE.EventService.RegisterEventHandler.html)| Registers
a handler for a specific event type. The handler is called whenever a message
of the specified type is sent. Messages are sent using EventService.Emit or
EventService.Request.  
[Request](MPE.EventService.Request.html)| Sends a request to all connected
clients on the "events" channel.  
[Start](MPE.EventService.Start.html)| Starts the EventService so it listens to
new messages.  
[Tick](MPE.EventService.Tick.html)| Ticks the EventService. This processes all
incoming and outgoing messages. By default, the EventService is ticked on each
EditorApplication.update.  
[UnregisterEventHandler](MPE.EventService.UnregisterEventHandler.html)|
Unregisters a handler from a specific event.  
  
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

