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

**Experimental** : this API is experimental and might be changed or removed in
the future.

# ExternalGPUProfiler

class in UnityEngine.Experimental.Rendering

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

The ExternalGPUProfiler API allows developers to programatically take GPU
frame captures in conjunction with supported external GPU profilers.  
GPU frame captures can be used to both analyze performance and debug graphics
related issues.

GPU captures can be taken when running using the API both in Editor and in
standalone development builds.  
The ExternalGPUProfiler API supports both PIX and RenderDoc.  
  
  
**PIX Specific Support**  
Support for PIX is only available on Windows desktop when using the DirectX 12
rendering API.  
**NOTE:** The entire editor will be captured when capturing a frame in editor.  
  
**RenderDoc Specific Support**  
Support for RenderDoc is available when running on both Windows and Linux
desktop.  
Supported rendering APIs include DirectX 12, DirectX 11, and Vulkan.  
**NOTE:** Only the game view will be captured when capturing a frame in
editor.

### Static Methods

[BeginGPUCapture](Experimental.Rendering.ExternalGPUProfiler.BeginGPUCapture.html)|
Begins the current GPU frame capture in the external GPU profiler.  
---|---  
[EndGPUCapture](Experimental.Rendering.ExternalGPUProfiler.EndGPUCapture.html)|
Ends the current GPU frame capture in the external GPU profiler.  
[IsAttached](Experimental.Rendering.ExternalGPUProfiler.IsAttached.html)|
Returns true when a development build is launched by an external GPU profiler.  
  
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

