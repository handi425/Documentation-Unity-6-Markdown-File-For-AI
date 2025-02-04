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

#  [RenderTexture](RenderTexture.html).depth

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

[Switch to Manual](../Manual/class-RenderTexture.html "Go to RenderTexture
Component in the Manual")

public int depth;

### Description

The precision of the render texture's depth buffer in bits (0, 16, 24 and 32
are supported).

Set the format of the Depth/Stencil buffer. The selected format depends on the
available formats on the platform and the desired format for 24bit depth. See
[GraphicsFormatUtility.GetDepthStencilFormat](Experimental.Rendering.GraphicsFormatUtility.GetDepthStencilFormat.html)
for more information on how the format is selected.  
  
The property returns the actual number of bits for depth in the selected
format. This can be different than the number of bits that was set if no
format with that exact number of depth bits is available on the platform.
[RenderTexture.depthStencilFormat](RenderTexture-depthStencilFormat.html)
returns the actual format that was selected.  
  
Set the format directly using
[RenderTexture.depthStencilFormat](RenderTexture-depthStencilFormat.html) if
you need to control exactly what format is used.  
  
Additional resources: [format](RenderTexture-graphicsFormat.html),
[width](RenderTexture-width.html), [height](RenderTexture-height.html).

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

