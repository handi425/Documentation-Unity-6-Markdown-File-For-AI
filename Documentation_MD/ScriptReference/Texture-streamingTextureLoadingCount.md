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

#  [Texture](Texture.html).streamingTextureLoadingCount

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

public static ulong streamingTextureLoadingCount;

### Description

Number of streaming Textures with mipmaps currently loading.

When adding a new camera it can take a few frames to detect which new Textures
need to be loaded. Therefore this value can't be relied upon immediately. If
any objects move or the camera moves then this value will change so it's not
guaranteed to drop to zero. When implementing camera cuts it is recommended
you have a minimum time to allow mipmap levels to be calculated and maximum
time to wait before doing the cut. This property can be used with a value
between the min and max time in order to cut earlier if the mipmaps are loaded
in time.  
  
The minimum time is dependent on the number of renderers in the Scene and the
number that are processed each frame. A minimum frame delay can be calculated
as ([Texture.streamingRendererCount](Texture-streamingRendererCount.html) \+
([QualitySettings.streamingMipmapsRenderersPerFrame](QualitySettings-
streamingMipmapsRenderersPerFrame.html)-1)) /
[QualitySettings.streamingMipmapsRenderersPerFrame](QualitySettings-
streamingMipmapsRenderersPerFrame.html). The maximum time should be an
acceptable delay to a user. E.g. 0.5 seconds (or 30 frames at 60Hz).  
  
Generally streamingTexturePendingLoadCount is a better choice for camera cut
delay as it includes both pending and active loading.  
  
Additional resources: [Texture.streamingTexturePendingLoadCount](Texture-
streamingTexturePendingLoadCount.html)

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

