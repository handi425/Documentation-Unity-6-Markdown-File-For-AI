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

# Screen

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

Access platform-specific display information.

This class has the same functionality as [Screen](Screen.html) and also mimics
platform-specific behavior in the Unity Editor. Use it together with the
Device Simulator to test platform-specific behaviors inside the Editor.
Outside of the Editor, this class behaves exactly like the
[Screen](Screen.html) class. Unity strips all simulation capabilities during
the build process. Use the original [Screen](Screen.html) class if you work
directly with the Unity Editor (for example, to create a custom Editor tool)
and you don't need to use any simulated values.

### Static Properties

[autorotateToLandscapeLeft](Device.Screen-autorotateToLandscapeLeft.html)|
This has the same functionality as Screen.autorotateToLandscapeLeft and also
mimics platform-specific behavior in the Unity Editor.  
---|---  
[autorotateToLandscapeRight](Device.Screen-autorotateToLandscapeRight.html)|
This has the same functionality as Screen.autorotateToLandscapeRight and also
mimics platform-specific behavior in the Unity Editor.  
[autorotateToPortrait](Device.Screen-autorotateToPortrait.html)| This has the
same functionality as Screen.autorotateToPortrait and also mimics platform-
specific behavior in the Unity Editor.  
[autorotateToPortraitUpsideDown](Device.Screen-
autorotateToPortraitUpsideDown.html)| This has the same functionality as
Screen.autorotateToPortraitUpsideDown and also mimics platform-specific
behavior in the Unity Editor.  
[brightness](Device.Screen-brightness.html)| This has the same functionality
as Screen.brightness. At the moment, the Device Simulator doesn't support
simulation of this property.  
[currentResolution](Device.Screen-currentResolution.html)| This has the same
functionality as Screen.currentResolution and also mimics platform-specific
behavior in the Unity Editor.  
[cutouts](Device.Screen-cutouts.html)| This has the same functionality as
Screen.cutouts and also mimics platform-specific behavior in the Unity Editor.  
[dpi](Device.Screen-dpi.html)| This has the same functionality as Screen.dpi
and also mimics platform-specific behavior in the Unity Editor.  
[fullScreen](Device.Screen-fullScreen.html)| This has the same functionality
as Screen.fullScreen and also mimics platform-specific behavior in the Unity
Editor.  
[fullScreenMode](Device.Screen-fullScreenMode.html)| This has the same
functionality as Screen.fullScreenMode and also mimics platform-specific
behavior in the Unity Editor.  
[height](Device.Screen-height.html)| This has the same functionality as
Screen.height and also mimics platform-specific behavior in the Unity Editor.  
[mainWindowDisplayInfo](Device.Screen-mainWindowDisplayInfo.html)| The Device
Simulator doesn't simulate this property.  
[mainWindowPosition](Device.Screen-mainWindowPosition.html)| The Device
Simulator doesn't simulate this property.  
[msaaSamples](Device.Screen-msaaSamples.html)| This has the same functionality
as Screen.msaaSamples and also mimics platform-specific behavior in the Unity
Editor.  
[orientation](Device.Screen-orientation.html)| This has the same functionality
as Screen.orientation and also mimics platform-specific behavior in the Unity
Editor.  
[resolutions](Device.Screen-resolutions.html)| This has the same functionality
as Screen.resolutions and also mimics platform-specific behavior in the Unity
Editor.  
[safeArea](Device.Screen-safeArea.html)| This has the same functionality as
Screen.safeArea and also mimics platform-specific behavior in the Unity
Editor.  
[sleepTimeout](Device.Screen-sleepTimeout.html)| This has the same
functionality as Screen.sleepTimeout. At the moment, the Device Simulator
doesn't support simulation of this property.  
[width](Device.Screen-width.html)| This has the same functionality as
Screen.width and also mimics platform-specific behavior in the Unity Editor.  
  
### Static Methods

[GetDisplayLayout](Device.Screen.GetDisplayLayout.html)| The Device Simulator
doesn't simulate this property.  
---|---  
[MoveMainWindowTo](Device.Screen.MoveMainWindowTo.html)| The Device Simulator
doesn't simulate this method.  
[SetMSAASamples](Device.Screen.SetMSAASamples.html)| This has the same
functionality as Screen.SetMSAASamples and also mimics platform-specific
behavior in the Unity Editor.  
[SetResolution](Device.Screen.SetResolution.html)| This has the same
functionality as Screen.SetResolution and also mimics platform-specific
behavior in the Unity Editor.  
  
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

