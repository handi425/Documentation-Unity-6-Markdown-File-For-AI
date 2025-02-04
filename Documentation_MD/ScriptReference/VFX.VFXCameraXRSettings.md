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

# VFXCameraXRSettings

struct in UnityEngine.VFX

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

Represents settings that specify how the Visual Effect Graph should handle an
XR Camera.

### Properties

[viewCount](VFX.VFXCameraXRSettings-viewCount.html)| The number of views to
render in the pass. In Unity, there are different methods of rendering a
Camera in XR. For multiple pass rendering, viewTotal is 2 and viewCount will
be 1. For other XR rendering methods, both viewTotal and viewCount are 2.  
---|---  
[viewOffset](VFX.VFXCameraXRSettings-viewOffset.html)| Indicates where to
start rendering views in this pass. Currently, the Visual Effect Graph uses
this for multiple pass XR rendering. In this case, the first pass value is 0
and the second pass is 1. For other XR rendering methods, this is 0.  
[viewTotal](VFX.VFXCameraXRSettings-viewTotal.html)| The number of views the
camera has in total. For a normal Camera, this is 1. For a Camera in XR, this
is 2.  
  
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

