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

#  [Physics2D](Physics2D.html).ClosestPoint

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

public static [Vector2](Vector2.html) ClosestPoint([Vector2](Vector2.html)
position, [Collider2D](Collider2D.html) collider);

### Parameters

position | The position from which to find the closest point on the specified `Collider`.  
---|---  
Collider | The Collider on which to find the closest specified `position`.  
  
### Returns

**Vector2** A point on the perimeter of the `Collider` that is closest to the
specified `position`.

### Description

Returns a point on the perimeter of the `Collider` that is closest to the
specified `position`.

This function provides the ability to calculate the closest point of a
specified `position` to the perimeter of any [Collider2D](Collider2D.html)
type.  
  
In the case where the `position` is inside the `Collider` or the `Collider` is
disabled, then the input `position` is returned instead.

* * *

## Declaration

public static [Vector2](Vector2.html) ClosestPoint([Vector2](Vector2.html)
position, [Rigidbody2D](Rigidbody2D.html) rigidbody);

### Parameters

position | The position from which to find the closest point on the specified `rigidbody`.  
---|---  
rigidbody | The Rigidbody on which to find the closest specified `position`.  
  
### Returns

**Vector2** A point on the perimeter of a Collider attached to the `rigidbody`
that is closest to the specified `position`.

### Description

Returns a point on the perimeter of all enabled Colliders attached to the
`rigidbody` that is closest to the specified `position`.

This function provides the ability to calculate the closest point of a
specified `position` to the perimeter of any enabled
[Collider2D](Collider2D.html) type attached to the specified
[Rigidbody2D](Rigidbody2D.html).  
  
In the case where the `position` is inside any of the enabled
[Collider2D](Collider2D.html) attached to the `rigidbody`, the input
`position` is returned instead.

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

