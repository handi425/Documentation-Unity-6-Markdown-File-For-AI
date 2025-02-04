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

# GraphicsDevice

class in UnityEngine.AMD

/

Implemented in:[UnityEngine.AMDModule](UnityEngine.AMDModule.html)

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

Provides the main entry point for the AMD Module. Use this to interact with
specific AMD graphics card features.

### Static Properties

[device](AMD.GraphicsDevice-device.html)| Gets the device created by
GraphicsDevice.CreateGraphicsDevice. If the device hasn't been created this
property evaluates to null.  
---|---  
[version](AMD.GraphicsDevice-version.html)| Gets the version that corresponds
to Unity's host plugin that manages the AMD.AMDUnityPlugin official library.  
  
### Public Methods

[CreateFeature](AMD.GraphicsDevice.CreateFeature.html)| Creates a specific AMD
feature.  
---|---  
[DestroyFeature](AMD.GraphicsDevice.DestroyFeature.html)| Destroys a specific
feature created with GraphicsDevice.CreateFeature.  
[ExecuteFSR2](AMD.GraphicsDevice.ExecuteFSR2.html)| Records the execution of
FSR 2.0 into a rendering command buffer. This call does not execute the
command buffer, it only appends custom commands into it.  
[GetRenderResolutionFromQualityMode](AMD.GraphicsDevice.GetRenderResolutionFromQualityMode.html)|
Queries the resolution configuration from a specified quality mode preset.  
[GetUpscaleRatioFromQualityMode](AMD.GraphicsDevice.GetUpscaleRatioFromQualityMode.html)|
Gets a precomputed upscaling ratio based on a preset quality setting.  
  
### Static Methods

[CreateGraphicsDevice](AMD.GraphicsDevice.CreateGraphicsDevice.html)| Creates
the main API object. Call this method only once in your application.  
---|---  
  
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

