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

# WebCamKind

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

[ ]()

### Description

Enum representing the different types of web camera device.

On iOS devices, the [WebCamDevice.kind](WebCamDevice-kind.html) is reported
directly by the hardware. On Android devices, the hardware does not report
this value, so Unity determines the [WebCamDevice.kind](WebCamDevice-
kind.html) by calculating the [Equivalent Focal
Length](https://en.wikipedia.org/wiki/35_mm_equivalent_focal_length) from a
calculation based on the reported focal length and matrix size. Therefore, on
some Android devices, the default camera may be detected as
[WebCamKind.UltraWideAngle](WebCamKind.UltraWideAngle.html) or
[WebCamKind.Telephoto](WebCamKind.Telephoto.html). As there is currently no
web API that returns the focal length of a webcam device, the WebGL
applications always return [WebCamDevice.kind](WebCamDevice-kind.html) as
WideAngle.  
  
Additional resources: [WebCamDevice.kind](WebCamDevice-kind.html).

### Properties

[Unknown](WebCamKind.Unknown.html)| The camera type is unknown.  
---|---  
[WideAngle](WebCamKind.WideAngle.html)| Wide angle (default) camera.  
[Telephoto](WebCamKind.Telephoto.html)| A Telephoto camera device. These
devices have a longer focal length than a wide-angle camera.  
[ColorAndDepth](WebCamKind.ColorAndDepth.html)| Camera which supports
synchronized color and depth data (currently these are only dual back and true
depth cameras on latest iOS devices).  
[UltraWideAngle](WebCamKind.UltraWideAngle.html)| Ultra wide angle camera.
These devices have a shorter focal length than a wide-angle camera.  
  
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

