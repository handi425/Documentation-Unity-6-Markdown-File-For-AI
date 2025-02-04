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

# LODFadeMode

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

The LOD (level of detail) fade modes. Modes other than
[LODFadeMode.None](LODFadeMode.None.html) will result in Unity calculating a
blend factor for blending/interpolating between two neighbouring LODs and pass
it to your shader.

### Properties

[None](LODFadeMode.None.html)| Indicates the LOD fading is turned off.  
---|---  
[CrossFade](LODFadeMode.CrossFade.html)| Perform cross-fade style blending
between the current LOD and the next LOD if the distance to camera falls in
the range specified by the LOD.fadeTransitionWidth of each LOD.  
[SpeedTree](LODFadeMode.SpeedTree.html)| By specifying this mode, your
LODGroup will perform a SpeedTree-style LOD fading scheme:For all the mesh
LODs other than the last (most crude) mesh LOD, the fade factor is calculated
as the percentage of the object's current screen height, compared to the whole
range of the LOD. It is 1, if the camera is right at the position where the
previous LOD switches out and 0, if the next LOD is just about to switch
in.For the last mesh LOD and the billboard LOD, the cross-fade mode is used.  
  
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

