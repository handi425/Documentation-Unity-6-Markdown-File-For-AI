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

#  [Collider2D](Collider2D.html).compositeOperation

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

public [Collider2D.CompositeOperation](Collider2D.CompositeOperation.html)
compositeOperation;

### Description

The composite operation to be used by a
[CompositeCollider2D](CompositeCollider2D.html).

A [CompositeCollider2D](CompositeCollider2D.html) is used when the composite
operation is anything other than
[Collider2D.CompositeOperation.None](Collider2D.CompositeOperation.None.html).  
  
When a [CompositeCollider2D](CompositeCollider2D.html) is used, the Collider
geometry is merged together using this composite operation with any other
Colliders using the same [CompositeCollider2D](CompositeCollider2D.html). The
composite operation order is controlled with
[Collider2D.compositeOrder](Collider2D-compositeOrder.html).  
  
**NOTE:** When a [CompositeCollider2D](CompositeCollider2D.html) is used, the
Editor will ignore and not show the
[Collider2D.sharedMaterial](Collider2D-sharedMaterial.html),
[Collider2D.isTrigger](Collider2D-isTrigger.html) &
[Collider2D.usedByEffector](Collider2D-usedByEffector.html) properties. The
same properties on the [CompositeCollider2D](CompositeCollider2D.html) will be
used instead. You should set these properties on the
[CompositeCollider2D](CompositeCollider2D.html) instead. Also, this property
is only available with the [BoxCollider2D](BoxCollider2D.html),
[PolygonCollider2D](PolygonCollider2D.html),
[CircleCollider2D](CircleCollider2D.html) and
[CapsuleCollider2D](CapsuleCollider2D.html).  
  
Additional resources:
[Collider2D.compositeOperation](Collider2D-compositeOperation.html),
[Collider2D.compositeOrder](Collider2D-compositeOrder.html) and
[CompositeCollider2D](CompositeCollider2D.html).

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

