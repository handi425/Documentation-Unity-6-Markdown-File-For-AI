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

#  [VideoPlayer](Video.VideoPlayer.html).targetTexture

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

public [RenderTexture](RenderTexture.html) targetTexture;

### Description

[RenderTexture](RenderTexture.html) to draw to when
[VideoPlayer.renderMode](Video.VideoPlayer-renderMode.html) is set to
Video.VideoTarget.RenderTexture.

If the [RenderTexture](RenderTexture.html) is of
[TextureDimension.Tex2D](Rendering.TextureDimension.Tex2D.html) the video
frames will be drawn directly into this target. For optimal performance,
[RenderTexture.width](RenderTexture-width.html) and
[RenderTexture.height](RenderTexture-height.html) should match those of the
video media exactly.  
  
If the [RenderTexture](RenderTexture.html) is of
[TextureDimension.Cube](Rendering.TextureDimension.Cube.html) the video frames
will be interpreted as a cubemap in one of the 4 supported layouts (horizontal
or vertical orientation of a cross or strip layout) based on video aspect
ratio. The cubemap faces of the video frame are drawn to the 6 faces of the
[RenderTexture](RenderTexture.html). For a one-to-one pixel mapping,
[RenderTexture.width](RenderTexture-width.html) and
[RenderTexture.height](RenderTexture-height.html) should match the size of the
individual faces contained within the video media's cubemap (eg. for a
2048x1536 horizontal cross cubemap video, the
[RenderTexture](RenderTexture.html) cube size should be set to 512x512).

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

