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

#  [HDROutputSettings](HDROutputSettings.html).automaticHDRTonemapping

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

public bool automaticHDRTonemapping;

### Description

Describes whether Unity performs HDR tonemapping automatically.

Set automaticHDRTonemapping to be true to instruct Unity to perform an
automatic tonemapping of your final image onto the HDR display buffer
immediately before it is presented to screen. Set automaticHDRTonemapping to
be false to perform your own custom HDR tonemapping onto the display buffer of
the active HDR display. This could be achieved as a custom post processing
stage or by using [Camera.OnRenderImage](Camera.OnRenderImage.html) to blit
the cameras output to the HDR display buffer using your own tonemapping
shader.  
  
Performing your own tonemapping gives greater flexibility over the final
image, whereas using Unity's automatic tonemapping provides a simple route to
achieving HDR output.  
  
Some platforms don't support automatic HDR Tonemapping (see
[SystemInfo.hdrDisplaySupportFlags](SystemInfo-hdrDisplaySupportFlags.html)).
In this case, the default value of automaticHDRTonemapping is false and can't
be changed. If automatic tonemapping is available, it's enabled by default.  
  
The value of automaticHDRTonemapping is ignored if HDR output is not active on
the display.

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

