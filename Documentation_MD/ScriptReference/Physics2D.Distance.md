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

#  [Physics2D](Physics2D.html).Distance

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

public static [ColliderDistance2D](ColliderDistance2D.html)
Distance([Collider2D](Collider2D.html) colliderA,
[Collider2D](Collider2D.html) colliderB);

### Parameters

colliderA | A Collider used to calculate the minimum distance against `colliderB`.  
---|---  
colliderB | A Collider used to calculate the minimum distance against `colliderA`.  
  
### Returns

**ColliderDistance2D** The minimum distance between `colliderA` and
`colliderB`.

### Description

Calculates the minimum distance between two Colliders.

A valid `colliderA` and `colliderB` must be provided for the returned
[ColliderDistance2D](ColliderDistance2D.html) to be valid i.e. both
`colliderA` or `colliderB` should not be NULL, should not be disabled and must
contain collision shapes. You can check if the returned value is valid by
checking [ColliderDistance2D.isValid](ColliderDistance2D-isValid.html).  
  
Additional resources: [Collider2D.Distance](Collider2D.Distance.html) and
[Rigidbody2D.Distance](Rigidbody2D.Distance.html).

* * *

## Declaration

public static [ColliderDistance2D](ColliderDistance2D.html)
Distance([Collider2D](Collider2D.html) colliderA, [Vector2](Vector2.html)
positionA, float angleA, [Collider2D](Collider2D.html) colliderB,
[Vector2](Vector2.html) positionB, float angleB);

### Parameters

colliderA | A Collider used to calculate the minimum distance against `colliderB`.  
---|---  
positionA | The position to use for `colliderA`.  
angleA | The rotation to use for `colliderA`.  
colliderB | A Collider used to calculate the minimum distance against `colliderA`.  
positionB | The position to use for `colliderB`.  
angleB | The rotation to use for `colliderB`.  
  
### Returns

**ColliderDistance2D** The minimum distance between `colliderA` and
`colliderB`.

### Description

Calculates the minimum distance between two Colliders.

A valid `colliderA` and `colliderB` must be provided for the returned
[ColliderDistance2D](ColliderDistance2D.html) to be valid i.e. both
`colliderA` or `colliderB` should not be NULL, should not be disabled and must
contain collision shapes. You can check if the returned value is valid by
checking [ColliderDistance2D.isValid](ColliderDistance2D-isValid.html).  
  
**NOTE** : The positions and angles used here represent the position of the
[Rigidbody2D](Rigidbody2D.html) the respective [Collider2D](Collider2D.html)
is attached to. If the [Collider2D](Collider2D.html) is offset from the center
of mass then the [Collider2D](Collider2D.html) will use the same offset. This
can be confusing so it is recommened that only [Collider2D](Collider2D.html)
that align with the center of mass are used. If not then you must take this
into account. If the [Collider2D](Collider2D.html) is not attached to a
[Rigidbody2D](Rigidbody2D.html), this call cannot be used and will result in a
warning.  
  
Additional resources: [Collider2D.Distance](Collider2D.Distance.html) and
[Rigidbody2D.Distance](Rigidbody2D.Distance.html).

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

