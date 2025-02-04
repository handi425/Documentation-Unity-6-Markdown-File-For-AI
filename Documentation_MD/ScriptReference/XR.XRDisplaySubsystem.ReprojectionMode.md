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

# ReprojectionMode

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

The kind of reprojection the app requests to stabilize its holographic
rendering relative to the user's head motion.

### Properties

[Unspecified](XR.XRDisplaySubsystem.ReprojectionMode.Unspecified.html)| Does
not specify the type of reprojection mode to use.  
---|---  
[PositionAndOrientation](XR.XRDisplaySubsystem.ReprojectionMode.PositionAndOrientation.html)|
Stabilizes the image for changes to both the user's head position and
orientation. This is best for world-locked content that you want to remain
stationary as the user walks around.  
[OrientationOnly](XR.XRDisplaySubsystem.ReprojectionMode.OrientationOnly.html)|
Stabilizes the image only for changes to the user's head orientation, ignores
changes in position. This is best for body-locked content that you want to
move with the user as they walk around, such as a 360-degree video.  
[None](XR.XRDisplaySubsystem.ReprojectionMode.None.html)| Does not stabilize
the image for the user's head motion and instead fixes it in the display. Note
that this is only comfortable for users when you use it sparingly, for example
when the only visible content is a small cursor.  
  
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

