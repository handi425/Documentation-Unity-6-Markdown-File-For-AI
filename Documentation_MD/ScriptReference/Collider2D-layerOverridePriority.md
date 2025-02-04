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

#  [Collider2D](Collider2D.html).layerOverridePriority

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

public int layerOverridePriority;

### Description

A decision priority assigned to this [Collider2D](Collider2D.html) used when
there is a conflicting decision on whether a contact between itself and
another [Collision2D](Collision2D.html) should happen or not.

The Layer Collision Matrix defines which Layers can and cannot contact other
Layers. Addition Layer includes and excludes can be made per
[Collider2D](Collider2D.html) or all [Collider2D](Collider2D.html) attached to
a specific [Rigidbody2D](Rigidbody2D.html). Any contact involves two different
[Collider2D](Collider2D.html) instances. Unfortunately this can result in one
[Collider2D](Collider2D.html) deciding that it should contact the other
[Collider2D](Collider2D.html) but the other [Collider2D](Collider2D.html)
deciding it should not. There are rules however in determining and ultimately
arbitrating the final decision on whether a contact should be created or not.  
  
The rules for a making a decision for contact between two
[Collider2D](Collider2D.html), referred to here as A and B, are made in the
following order:

  1. If both A and B make the same decision then use that decision.
  2. If only A or B are using a Layer include or exclude then use the decision for A or B that has include or exclude specified.
  3. If both A and B are using a Layer include or exclude then use the decision from A or B that has the higher [Collider2D.layerOverridePriority](Collider2D-layerOverridePriority.html).
  4. If A and B have the same [Collider2D.layerOverridePriority](Collider2D-layerOverridePriority.html) then the decision will be to not create a contact.

Additional resources:
[Collider2D.includeLayers](Collider2D-includeLayers.html),
[Collider2D.excludeLayers](Collider2D-excludeLayers.html),
[Rigidbody2D.includeLayers](Rigidbody2D-includeLayers.html) &
[Rigidbody2D.excludeLayers](Rigidbody2D-excludeLayers.html).

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

