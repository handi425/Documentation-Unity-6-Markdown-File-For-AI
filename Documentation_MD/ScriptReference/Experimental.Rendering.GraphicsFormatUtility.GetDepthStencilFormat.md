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

#
[GraphicsFormatUtility](Experimental.Rendering.GraphicsFormatUtility.html).GetDepthStencilFormat

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

## Declaration

public static
[Experimental.Rendering.GraphicsFormat](Experimental.Rendering.GraphicsFormat.html)
GetDepthStencilFormat(int minimumDepthBits, int minimumStencilBits);

### Parameters

minimumDepthBits | Minimum number of bits that the format should have for the depth component.  
---|---  
minimumStencilBits | Minimum number of bits that the format should have for the stencil component.  
  
### Returns

**GraphicsFormat** A GraphicsFormat that has a depth and/or stencil component.

### Description

Returns a supported depth stencil format that has 'minimumDepthBits' of bits
or higher per pixel for the depth component if a compatible format exists on
the current platform. If 'minimumStencilBits' is higher than 0, and a
compatible format exists on the current platform, Unity returns a depth
stencil format with 8 bits per pixel for the stencil component.

The minimum depth bits are rounded up to 16, 24 or 32 bits. If the minimum
stencil bits are zero then the returned format will not contain a stencil
component.  
  
Returns 'GraphicsFormat.None' if no formats are supported on the current
platform that have the minimum amount of bits for the components.  
  
Additional resources: [RenderTexture.depthStencilFormat](RenderTexture-
depthStencilFormat.html),
[RenderTextureDescriptor.depthStencilFormat](RenderTextureDescriptor-
depthStencilFormat.html).

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

