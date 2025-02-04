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

# UnityEngine.AMDModule

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

A module that contains API you can use to interact with AMD graphics cards.

To activate this module at runtime, call AMD.Plugins.LoadPlugin with the
AMD.Plugins.Plugin.AMDUnityPlugin value during application startup.

### Classes

[AMDUnityPlugin](AMD.AMDUnityPlugin.html)| Provides methods to manage loading
and unloading AMD module plugins.  
---|---  
[FSR2Context](AMD.FSR2Context.html)| Represents the state of FSR2.  
[GraphicsDevice](AMD.GraphicsDevice.html)| Provides the main entry point for
the AMD Module. Use this to interact with specific AMD graphics card features.  
  
### Structs

[FSR2CommandExecutionData](AMD.FSR2CommandExecutionData.html)| Represents the
state of a FSR2Context. If you call Device.ExecuteFSR2, Unity sends the values
in this struct to the runtime. After this, you can change the values in this
struct without any side effects.  
---|---  
[FSR2CommandInitializationData](AMD.FSR2CommandInitializationData.html)|
Represents the initialization state of a DLSSContext. You can only use and set
this when calling GraphicsDevice.CreateFeature.  
[FSR2TextureTable](AMD.FSR2TextureTable.html)| The set of texture slots
available for the FSR2Context. SA GraphicsDevice.ExecuteFSR2.  
  
### Enumerations

[FfxFsr2InitializationFlags](AMD.FfxFsr2InitializationFlags.html)| Options
that represent subfeatures of FSR2.  
---|---  
[FSR2Quality](AMD.FSR2Quality.html)| Options for FSR2 performance modes.  
  
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

