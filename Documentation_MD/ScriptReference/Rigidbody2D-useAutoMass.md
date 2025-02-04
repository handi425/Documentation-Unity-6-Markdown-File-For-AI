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

#  [Rigidbody2D](Rigidbody2D.html).useAutoMass

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

public bool useAutoMass;

### Description

Should the total rigid-body [mass](Rigidbody2D-mass.html) be automatically
calculated from the [[[Collider2D.density](Collider2D-density.html)]] of
attached colliders?

When false, the explicitly set [mass](Rigidbody2D-mass.html) is used for the
rigid-body mass. When true, the mass is automatically calculated from all
attached [Collider2D](Collider2D.html) as a product of their
[[[Collider2D.density](Collider2D-density.html)]] and area.  
  
When true, inside the Unity editor, the
[[[Collider2D.density](Collider2D-density.html)]] property will appear on any
attached [Collider2D](Collider2D.html) and the [mass](Rigidbody2D-mass.html)
property will become read-only.  
  
When false, the [mass](Rigidbody2D-mass.html) property can be written to and
the [[[Collider2D.density](Collider2D-density.html)]] property is not shown.  
  
Additional resources: [mass](Rigidbody2D-mass.html),
::[Collider2D.density](Collider2D-density.html).

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

