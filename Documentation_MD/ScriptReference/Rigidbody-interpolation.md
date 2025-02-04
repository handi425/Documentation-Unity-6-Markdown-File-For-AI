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

#  [Rigidbody](Rigidbody.html).interpolation

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

[Switch to Manual](../Manual/class-Rigidbody.html "Go to Rigidbody Component
in the Manual")

public [RigidbodyInterpolation](RigidbodyInterpolation.html) interpolation;

### Description

Interpolation provides a way to manage the appearance of jitter in the
movement of your Rigidbody GameObjects at run time.

Interpolation calculates the pose of a Rigidbody in frames that fall between
physics timestep updates, to reduce the appearance of visible jitter. It is
particularly useful for player character GameObjects, and any other GameObject
that the camera follows. By default, interpolation is disabled. When
interpolation or extrapolation is enabled, the physics system takes control of
the Rigidbody's transform. For this reason, you should follow any direct (non-
physics) change to the transform with a
[Physics.SyncTransforms](Physics.SyncTransforms.html) call. Otherwise, Unity
ignores any transform change that does not originate from the physics system.
Physics simulation runs at discrete timesteps, while graphics are rendered at
variable frame rates. This can lead to visual jitter on some GameObjects,
because the physics and graphics updates are not synchronized. The visual
effect is particularly noticeable on GameObjects that the camera follows (such
as player characters and vehicles). It is recommended to turn on interpolation
for the main character but disable it for everything else.

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

