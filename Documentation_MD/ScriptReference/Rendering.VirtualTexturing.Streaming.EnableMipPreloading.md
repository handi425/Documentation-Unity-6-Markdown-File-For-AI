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

Virtual Texturing is experimental and not ready for production use. The
feature and documentation might be changed or removed in the future.

#  [Streaming](Rendering.VirtualTexturing.Streaming.html).EnableMipPreloading

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

public static void EnableMipPreloading(int texturesPerFrame, int mipCount);

### Parameters

texturesPerFrame | Number of textures per frame to process. The range is `0` through `1024`. The default is `0`. A number of `0` disables preloading. The higher this number, the more CPU resource will be used on the render thread.  
---|---  
mipCount | The number of mipmap levels to preload. The range is `1` through `9`. The default is `1`, which preloads only the highest mipmap level with the smallest size of 128 by 128 pixels. This is the size of the Streaming Virtual Texturing tile.  
  
### Description

Enables mipmap level preloading used by Streaming Virtual Texturing.

Use this method to avoid texture pop-in by preloading the smallest-sized
mipmap levels into GPU memory. If there are many more virtual textures in
materials and `texturesPerFrame` is too low, you might still see black
textures pop in. For more targeted texture preload requests, refer to
Rendering.VirtualTexturing.Streaming.RequestRegion.html.

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

