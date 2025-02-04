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

#  [VFXManager](VFX.VFXManager.html).SetCameraBuffer

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

public static void SetCameraBuffer([Camera](Camera.html) cam,
[VFX.VFXCameraBufferTypes](VFX.VFXCameraBufferTypes.html) type,
[Texture](Texture.html) buffer, int x, int y, int width, int height);

### Parameters

cam | The Camera to set the buffer for.  
---|---  
type | The type of buffer to set.  
buffer | The buffer to set.  
x | X offset of the viewport in the buffer.  
y | Y offset of the viewport in the buffer.  
width | Width of the viewport in the buffer.  
height | Height of the viewport in the buffer.  
  
### Description

Use this method to set the buffer of a given type for this Camera. This allows
the VFX Manager to use the buffer.

In custom Scriptable Render Pipelines, this buffer allows the VFXManager to
use buffer behaviors for the Camera, for example depth collisions. The buffer
must be available during the VFX update of the next frame. To query the need
for a buffer, call
[VFXManager.IsCameraBufferNeeded](VFX.VFXManager.IsCameraBufferNeeded.html).

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

