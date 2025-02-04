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

#  [ScalableBufferManager](ScalableBufferManager.html).ResizeBuffers

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

public static void ResizeBuffers(float widthScale, float heightScale);

### Parameters

widthScale | New scale factor for the width that the ScalableBufferManager uses to resize all render textures that are marked as `DynamicallyScalable`. The value should be greater than 0.0, and less than or equal to 1.0  
---|---  
heightScale | New scale factor for the height that the ScalableBufferManager uses to resize all render textures that are marked as `DynamicallyScalable`. The value should be greater than 0.0, and less than or equal to 1.0.  
  
### Description

Function to resize all buffers marked as DynamicallyScalable.

Takes in new width and height scale and stores and applies it to all render
textures marked as DynamicallyScalable. Note that the scale is applied to the
render textures original dimensions so a scale factor of 1.0 will always be
the full dimensions for the specified render target, etc.  
  
Vulkan and DirectX 12 only allow uniform scaling through the utilization of
widthScale.

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

