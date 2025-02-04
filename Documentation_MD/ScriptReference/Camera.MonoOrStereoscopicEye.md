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

# MonoOrStereoscopicEye

enumeration

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

[Switch to Manual](../Manual/class-Camera.html "Go to Camera Component in the
Manual")

### Description

A Camera eye corresponding to the left or right human eye for stereoscopic
rendering, or neither for non-stereoscopic rendering.  
  
A single Camera can render both left and right views in a single frame.
Therefore, this enum describes which eye the Camera is currently rendering
when returned by [Camera.stereoActiveEye](Camera-stereoActiveEye.html) during
a rendering callback (such as
[Camera.OnRenderImage](Camera.OnRenderImage.html)), or which eye to act on
when passed into a function.  
  
The default value is
[Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html),
so [Camera.MonoOrStereoscopicEye.Left](Camera.MonoOrStereoscopicEye.Left.html)
may be returned by some methods or properties when called outside of rendering
if stereoscopic rendering is enabled.

### Properties

[Left](Camera.MonoOrStereoscopicEye.Left.html)| Camera eye corresponding to
stereoscopic rendering of the left eye.  
---|---  
[Right](Camera.MonoOrStereoscopicEye.Right.html)| Camera eye corresponding to
stereoscopic rendering of the right eye.  
[Mono](Camera.MonoOrStereoscopicEye.Mono.html)| Camera eye corresponding to
non-stereoscopic rendering.  
  
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

