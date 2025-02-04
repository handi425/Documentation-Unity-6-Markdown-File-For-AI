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

# ScalableBufferManager

class in UnityEngine

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

Scales render textures to support dynamic resolution if the target
platform/graphics API supports it.

The `ScalableBufferManager` class handles the scaling of any render textures
that you have marked as `DynamicallyScalable` when `ResizeBuffers` is called.
All render textures marked as `DynamicallyScalable` are scaled by a width and
height scale factor. The scale is controlled through a scale factor and not
with a specific width and height value because even though render textures are
of different sizes, they need to be scaled by a common factor.  
  
The current implementation only supports discrete scale factors in the range
of 0.05 and 1.0 in steps of 0.05 to be consistent across all platforms. Unity
automatically selects the closest supported scale factors. You can access the
selected scale factors using
[ScalableBufferManager.widthScaleFactor](ScalableBufferManager-
widthScaleFactor.html) and
[ScalableBufferManager.heightScaleFactor](ScalableBufferManager-
heightScaleFactor.html).  
  
The scaled dimensions are calculated as follows:  
  
width = ceil(renderTexture.width * ScalableBufferManager.widthScaleFactor)
height = ceil(renderTexture.height * ScalableBufferManager.heightScaleFactor)  
  
The render textures that you have marked as `DynamicallyScalableExplicit` are
not scaled by a call to `ResizeBuffers` but by a call to
`RenderTexture.ApplyDynamicScale`. Scaling is subject to the exact same
process as `ResizeBuffers`.

### Static Properties

[heightScaleFactor](ScalableBufferManager-heightScaleFactor.html)| Height
scale factor to control dynamic resolution.  
---|---  
[widthScaleFactor](ScalableBufferManager-widthScaleFactor.html)| Width scale
factor to control dynamic resolution.  
  
### Static Methods

[ResizeBuffers](ScalableBufferManager.ResizeBuffers.html)| Function to resize
all buffers marked as DynamicallyScalable.  
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

