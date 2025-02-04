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

# Application

class in UnityEngine

/

Implemented in:[UnityEngine.CoreModule](UnityEngine.CoreModule.html)

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

Provides access to application runtime data.

This class contains static methods for looking up information about and
controlling the runtime data.

### Static Properties

[absoluteURL](Application-absoluteURL.html)| The URL of the document. For
WebGL, this is a web URL. For Android, iOS, or Universal Windows Platform
(UWP) this is a deep link URL (Read Only).  
---|---  
[backgroundLoadingPriority](Application-backgroundLoadingPriority.html)|
Priority of background loading thread.  
[buildGUID](Application-buildGUID.html)| Returns a GUID for this build (Read
Only).  
[cloudProjectId](Application-cloudProjectId.html)| A unique cloud project
identifier. It is unique for every project (Read Only).  
[companyName](Application-companyName.html)| Returns application company name
(Read Only).  
[consoleLogPath](Application-consoleLogPath.html)| Returns the path to the
console log file, or an empty string if the current platform does not support
log files.  
[dataPath](Application-dataPath.html)| Contains the path to the game data
folder on the target device (Read Only).  
[exitCancellationToken](Application-exitCancellationToken.html)| Cancellation
token raised on exiting Play mode (Editor) or on quitting the application
(Read Only).  
[genuine](Application-genuine.html)| Returns false if application is altered
in any way after it was built.  
[genuineCheckAvailable](Application-genuineCheckAvailable.html)| Returns true
if application integrity can be confirmed.  
[identifier](Application-identifier.html)| Returns the application identifier
at runtime.  
[installerName](Application-installerName.html)| Returns the name of the store
or package that installed the application (Read Only).  
[installMode](Application-installMode.html)| Returns application install mode
(Read Only).  
[internetReachability](Application-internetReachability.html)| Returns the
type of internet reachability currently possible on the device.  
[isBatchMode](Application-isBatchMode.html)| Returns true when Unity is
launched with the -batchmode flag from the command line (Read Only).  
[isConsolePlatform](Application-isConsolePlatform.html)| Is the current
Runtime platform a known console platform.  
[isEditor](Application-isEditor.html)| Whether the game is running inside the
Unity Editor (Read Only).  
[isFocused](Application-isFocused.html)| Whether the Player currently has
focus (Read Only).  
[isMobilePlatform](Application-isMobilePlatform.html)| Identifies whether the
current Runtime platform is a known mobile platform.  
[isPlaying](Application-isPlaying.html)| Returns true when called in any kind
of built Player, or when called in the Editor in Play mode (Read Only).  
[persistentDataPath](Application-persistentDataPath.html)| Contains the path
to a persistent data directory (Read-only).  
[platform](Application-platform.html)| Returns the platform the game is
running on (Read Only).  
[productName](Application-productName.html)| Returns application product name
(Read Only).  
[runInBackground](Application-runInBackground.html)| Determines whether the
Player should run when the application is in the background  
[sandboxType](Application-sandboxType.html)| Returns application running in a
sandbox environment (Read-only).  
[streamingAssetsPath](Application-streamingAssetsPath.html)| The path to the
StreamingAssets folder (Read Only).  
[systemLanguage](Application-systemLanguage.html)| The language in which the
user's operating system is running in.  
[targetFrameRate](Application-targetFrameRate.html)| Specifies the target
frame rate at which Unity tries to render your game.  
[temporaryCachePath](Application-temporaryCachePath.html)| Contains the path
to a temporary data / cache directory (Read Only).  
[unityVersion](Application-unityVersion.html)| The version of the Unity
runtime used to play the content.  
[version](Application-version.html)| Returns application version number (Read
Only).  
  
### Static Methods

[CanStreamedLevelBeLoaded](Application.CanStreamedLevelBeLoaded.html)| Checks
if the streamed level can be loaded.  
---|---  
[GetStackTraceLogType](Application.GetStackTraceLogType.html)| Get stack trace
logging options. The default value is StackTraceLogType.ScriptOnly.  
[HasProLicense](Application.HasProLicense.html)| Is Unity activated with the
Pro license?  
[HasUserAuthorization](Application.HasUserAuthorization.html)| Check if the
user has authorized use of the webcam or microphone on iOS and WebGL.  
[IsPlaying](Application.IsPlaying.html)| Returns true if the given object is
part of the playing world either in any kind of built Player or in Play Mode.  
[OpenURL](Application.OpenURL.html)| Opens the URL specified, subject to the
permissions and limitations of your app’s current platform and environment.  
[Quit](Application.Quit.html)| Quits the player application.  
[RequestAdvertisingIdentifierAsync](Application.RequestAdvertisingIdentifierAsync.html)|
Request an advertising ID for iOS and UWP.  
[RequestUserAuthorization](Application.RequestUserAuthorization.html)| Request
authorization to use the webcam or microphone on iOS, and the webcam only on
WebGL.  
[SetStackTraceLogType](Application.SetStackTraceLogType.html)| Set stack trace
logging options. The default value is StackTraceLogType.ScriptOnly.  
[Unload](Application.Unload.html)| Unloads the Unity Player.  
  
### Events

[deepLinkActivated](Application-deepLinkActivated.html)| This event is raised
when an application running on Android, iOS, or the Universal Windows Platform
(UWP) is activated using a deep link URL.  
---|---  
[focusChanged](Application-focusChanged.html)| Defines the delegate to use to
register for events in which the focus gained or lost.  
[logMessageReceived](Application-logMessageReceived.html)| Event that is fired
if a log message is received.  
[logMessageReceivedThreaded](Application-logMessageReceivedThreaded.html)|
Event that is fired if a log message is received.  
[lowMemory](Application-lowMemory.html)| The Application._lowMemory event
occurs when your application receives a low-memory notification from the
device it is running on.  
[memoryUsageChanged](Application-memoryUsageChanged.html)| Informs about
significant changes in the application's memory usage.  
[onBeforeRender](Application-onBeforeRender.html)| A delegate method used to
register for Just Before Render input updates for VR devices.  
[quitting](Application-quitting.html)| Unity raises this event when the Player
application is quitting.  
[unloading](Application-unloading.html)| Unity raises this event when the
Player is unloading.  
[wantsToQuit](Application-wantsToQuit.html)| Unity raises this event when the
Player application wants to quit.  
  
### Delegates

[AdvertisingIdentifierCallback](Application.AdvertisingIdentifierCallback.html)|
Delegate method for fetching advertising ID.  
---|---  
[LogCallback](Application.LogCallback.html)| Use this delegate type with
Application.logMessageReceived or Application.logMessageReceivedThreaded to
monitor what gets logged.  
[LowMemoryCallback](Application.LowMemoryCallback.html)| This is the delegate
function when a mobile device notifies of low memory.  
[MemoryUsageChangedCallback](Application.MemoryUsageChangedCallback.html)| A
delegate for the Application.memoryUsageChanged vent.  
  
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

