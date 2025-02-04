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

#  [WheelCollider](WheelCollider.html).sprungMass

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

[Switch to Manual](../Manual/class-WheelCollider.html "Go to WheelCollider
Component in the Manual")

public float sprungMass;

### Description

The mass supported by this WheelCollider.

Vehicle simulation uses the sprung mass model that assumes each wheel supports
a particular portion of the vehicle's total mass at rest. By default, the
sprung mass distribution is computed automatically based on the positions of
the wheels relative to the vehicle's center of mass. However, it's also
possible to set the masses explicitly. In this case, the whole vehicle is
marked as having an explicit mass distribution and no sprung masses will ever
be computed for it until the explicit flag is reset by calling
[WheelCollider.ResetSprungMasses](WheelCollider.ResetSprungMasses.html). Note
that the sum of all the sprung masses should be equivalent to the total mass
of the vehicle. Because of that, adjusting a wheel's sprung mass will
naturally require updating the sprung masses for the other wheels of the
vehicle in order to match the vehicle's mass.

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

