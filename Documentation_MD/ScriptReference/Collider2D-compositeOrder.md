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

#  [Collider2D](Collider2D.html).compositeOrder

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

public int compositeOrder;

### Description

The composite operation order to be used when a
[CompositeCollider2D](CompositeCollider2D.html) is used.

When this [Collider2D](Collider2D.html) is using any composite operation other
than
[Collider2D.CompositeOperation.None](Collider2D.CompositeOperation.None.html),
the composite operation uses the previous composite operation results on the
[CompositeCollider2D](CompositeCollider2D.html) as the input and applies this
[Collider2D](Collider2D.html) geometry using its selected
[Collider2D.compositeOperation](Collider2D-compositeOperation.html).  
  
The composite order is a simple integer value that is first sorted into
ascending order by the [CompositeCollider2D](CompositeCollider2D.html) before
it applies the composite operations with the lowest value being executed first
in order up to the highest values. When the composite order values are
identical, the order is undefined. When using only
[Collider2D.CompositeOperation.Merge](Collider2D.CompositeOperation.Merge.html)
operations, this order is irrelevant to the final result.  
  
Using this order, it is possible to control which previous
[Collider2D](Collider2D.html) that are also using the
[CompositeCollider2D](CompositeCollider2D.html) are affected by this composite
operation.  
  
**NOTE:** After sorting the composite order for all
[Collider2D](Collider2D.html), the first composite operation of
[Collider2D.CompositeOperation.Merge](Collider2D.CompositeOperation.Merge.html)
will always used, independent of that
[Collider2D.compositeOperation](Collider2D-compositeOperation.html) property
setting. This is due to the fact that the first operation has no input
geometry for the operation to complete and only the merge (OR) composite
operation results in any geometry!  
  
Additional resources:
[CompositeOperation](Collider2D.CompositeOperation.html),
[Collider2D.compositeOperation](Collider2D-compositeOperation.html) and
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

