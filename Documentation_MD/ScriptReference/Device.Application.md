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

class in UnityEngine.Device

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

Access to platform-specific application runtime data.

This class has the same functionality as [Application](Application.html) and
also mimics platform-specific behavior in the Unity Editor. Use it together
with the Device Simulator to test platform-specific behaviors inside the
Editor. Outside of the Editor, this class behaves exactly like the
[Application](Application.html) class. Unity strips all simulation
capabilities during the build process. Use the original
[Application](Application.html) class if you work directly with the Unity
Editor (for example, to create a custom Editor tool) and you don't need to use
any simulated values.

### Static Properties

[absoluteURL](Device.Application-absoluteURL.html)| This has the same
functionality as Application.absoluteURL. At the moment, the Device Simulator
doesn't support simulation of this property.  
---|---  
[backgroundLoadingPriority](Device.Application-
backgroundLoadingPriority.html)| This has the same functionality as
Application.backgroundLoadingPriority. At the moment, the Device Simulator
doesn't support simulation of this property.  
[buildGUID](Device.Application-buildGUID.html)| This has the same
functionality as Application.buildGUID. At the moment, the Device Simulator
doesn't support simulation of this property.  
[cloudProjectId](Device.Application-cloudProjectId.html)| This has the same
functionality as Application.cloudProjectId. At the moment, the Device
Simulator doesn't support simulation of this property.  
[companyName](Device.Application-companyName.html)| This has the same
functionality as Application.companyName. At the moment, the Device Simulator
doesn't support simulation of this property.  
[consoleLogPath](Device.Application-consoleLogPath.html)| This has the same
functionality as Application.consoleLogPath. At the moment, the Device
Simulator doesn't support simulation of this property.  
[dataPath](Device.Application-dataPath.html)| This has the same functionality
as Application.dataPath. At the moment, the Device Simulator doesn't support
simulation of this property.  
[exitCancellationToken](Device.Application-exitCancellationToken.html)|
Cancellation token raised on exiting play mode (editor) or on quitting the
application (Read Only).  
[genuine](Device.Application-genuine.html)| This has the same functionality as
Application.genuine. At the moment, the Device Simulator doesn't support
simulation of this property.  
[genuineCheckAvailable](Device.Application-genuineCheckAvailable.html)| This
has the same functionality as Application.genuineCheckAvailable. At the
moment, the Device Simulator doesn't support simulation of this property.  
[identifier](Device.Application-identifier.html)| This has the same
functionality as Application.identifier. At the moment, the Device Simulator
doesn't support simulation of this property.  
[installerName](Device.Application-installerName.html)| This has the same
functionality as Application.installerName. At the moment, the Device
Simulator doesn't support simulation of this property.  
[installMode](Device.Application-installMode.html)| This has the same
functionality as Application.installMode. At the moment, the Device Simulator
doesn't support simulation of this property.  
[internetReachability](Device.Application-internetReachability.html)| This has
the same functionality as Application.internetReachability and also mimics
platform-specific behavior in the Unity Editor.  
[isBatchMode](Device.Application-isBatchMode.html)| This has the same
functionality as Application.isBatchMode. At the moment, the Device Simulator
doesn't support simulation of this property.  
[isConsolePlatform](Device.Application-isConsolePlatform.html)| This has the
same functionality as Application.isConsolePlatform and also mimics platform-
specific behavior in the Unity Editor.  
[isEditor](Device.Application-isEditor.html)| This has the same functionality
as Application.isEditor and also mimics platform-specific behavior in the
Unity Editor.  
[isFocused](Device.Application-isFocused.html)| This has the same
functionality as Application.isFocused. At the moment, the Device Simulator
doesn't support simulation of this property.  
[isMobilePlatform](Device.Application-isMobilePlatform.html)| This has the
same functionality as Application.isMobilePlatform and also mimics platform-
specific behavior in the Unity Editor.  
[isPlaying](Device.Application-isPlaying.html)| This has the same
functionality as Application.isPlaying. At the moment, the Device Simulator
doesn't support simulation of this property.  
[persistentDataPath](Device.Application-persistentDataPath.html)| This has the
same functionality as Application.persistentDataPath. At the moment, the
Device Simulator doesn't support simulation of this property.  
[platform](Device.Application-platform.html)| This has the same functionality
as Application.platform and also mimics platform-specific behavior in the
Unity Editor.  
[productName](Device.Application-productName.html)| This has the same
functionality as Application.productName. At the moment, the Device Simulator
doesn't support simulation of this property.  
[runInBackground](Device.Application-runInBackground.html)| This has the same
functionality as Application.runInBackground. At the moment, the Device
Simulator doesn't support simulation of this property.  
[sandboxType](Device.Application-sandboxType.html)| This has the same
functionality as Application.sandboxType. At the moment, the Device Simulator
doesn't support simulation of this property.  
[streamingAssetsPath](Device.Application-streamingAssetsPath.html)| This has
the same functionality as Application.streamingAssetsPath. At the moment, the
Device Simulator doesn't support simulation of this property.  
[systemLanguage](Device.Application-systemLanguage.html)| This has the same
functionality as Application.systemLanguage and also mimics platform-specific
behavior in the Unity Editor.  
[targetFrameRate](Device.Application-targetFrameRate.html)| This has the same
functionality as Application.targetFrameRate. At the moment, the Device
Simulator doesn't support simulation of this property.  
[temporaryCachePath](Device.Application-temporaryCachePath.html)| This has the
same functionality as Application.temporaryCachePath. At the moment, the
Device Simulator doesn't support simulation of this property.  
[unityVersion](Device.Application-unityVersion.html)| This has the same
functionality as Application.unityVersion. At the moment, the Device Simulator
doesn't support simulation of this property.  
[version](Device.Application-version.html)| This has the same functionality as
Application.version. At the moment, the Device Simulator doesn't support
simulation of this property.  
  
### Static Methods

[CanStreamedLevelBeLoaded](Device.Application.CanStreamedLevelBeLoaded.html)|
This has the same functionality as Application.CanStreamedLevelBeLoaded. At
the moment, the Device Simulator doesn't support simulation of this method.  
---|---  
[GetStackTraceLogType](Device.Application.GetStackTraceLogType.html)| This has
the same functionality as Application.GetStackTraceLogType. At the moment, the
Device Simulator doesn't support simulation of this method.  
[HasProLicense](Device.Application.HasProLicense.html)| This has the same
functionality as Application.HasProLicense. At the moment, the Device
Simulator doesn't support simulation of this method.  
[HasUserAuthorization](Device.Application.HasUserAuthorization.html)| This has
the same functionality as Application.HasUserAuthorization. At the moment, the
Device Simulator doesn't support simulation of this method.  
[IsPlaying](Device.Application.IsPlaying.html)| This has the same
functionality as Application.IsPlaying. At the moment, the Device Simulator
doesn't support simulation of this method.  
[OpenURL](Device.Application.OpenURL.html)| This has the same functionality as
Application.OpenURL. At the moment, the Device Simulator doesn't support
simulation of this method.  
[Quit](Device.Application.Quit.html)| This has the same functionality as
Application.Quit. At the moment, the Device Simulator doesn't support
simulation of this method.  
[RequestAdvertisingIdentifierAsync](Device.Application.RequestAdvertisingIdentifierAsync.html)|
This has the same functionality as
Application.RequestAdvertisingIdentifierAsync. At the moment, the Device
Simulator doesn't support simulation of this method.  
[RequestUserAuthorization](Device.Application.RequestUserAuthorization.html)|
This has the same functionality as Application.RequestUserAuthorization. At
the moment, the Device Simulator doesn't support simulation of this method.  
[SetStackTraceLogType](Device.Application.SetStackTraceLogType.html)| This has
the same functionality as Application.SetStackTraceLogType. At the moment, the
Device Simulator doesn't support simulation of this method.  
[Unload](Device.Application.Unload.html)| This has the same functionality as
Application.Unload. At the moment, the Device Simulator doesn't support
simulation of this method.  
  
### Events

[deepLinkActivated](Device.Application-deepLinkActivated.html)| This has the
same functionality as Application.deepLinkActivated. At the moment, the Device
Simulator doesn't support simulation of this event.  
---|---  
[focusChanged](Device.Application-focusChanged.html)| This has the same
functionality as Application.focusChanged. At the moment, the Device Simulator
doesn't support simulation of this event.  
[logMessageReceived](Device.Application-logMessageReceived.html)| This has the
same functionality as Application.logMessageReceived. At the moment, the
Device Simulator doesn't support simulation of this event.  
[logMessageReceivedThreaded](Device.Application-
logMessageReceivedThreaded.html)| This has the same functionality as
Application.logMessageReceivedThreaded. At the moment, the Device Simulator
doesn't support simulation of this event.  
[lowMemory](Device.Application-lowMemory.html)| This has the same
functionality as Application.lowMemory and also mimics platform-specific
behavior in the Unity Editor.  
[memoryUsageChanged](Device.Application-memoryUsageChanged.html)| This has the
same functionality as Application.memoryUsageChanged.  
[onBeforeRender](Device.Application-onBeforeRender.html)| This has the same
functionality as Application.onBeforeRender. At the moment, the Device
Simulator doesn't support simulation of this event.  
[quitting](Device.Application-quitting.html)| This has the same functionality
as Application.quitting. At the moment, the Device Simulator doesn't support
simulation of this event.  
[unloading](Device.Application-unloading.html)| This has the same
functionality as Application.unloading. At the moment, the Device Simulator
doesn't support simulation of this event.  
[wantsToQuit](Device.Application-wantsToQuit.html)| This has the same
functionality as Application.wantsToQuit. At the moment, the Device Simulator
doesn't support simulation of this event.  
  
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

