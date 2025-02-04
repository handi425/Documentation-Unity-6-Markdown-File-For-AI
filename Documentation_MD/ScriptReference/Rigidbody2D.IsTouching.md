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

#  [Rigidbody2D](Rigidbody2D.html).IsTouching

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

public bool IsTouching([Collider2D](Collider2D.html) collider);

### Parameters

collider | The collider to check if it is touching any of the collider(s) attached to this rigidbody.  
---|---  
  
### Returns

**bool** Whether the `collider` is touching any of the collider(s) attached to
this rigidbody or not.

### Description

Checks whether the `collider` is touching any of the collider(s) attached to
this rigidbody or not.

It is important to understand that checking whether colliders are touching or
not is performed against the last physics system update; that is the state of
touching colliders at that time. If you have just added a new
[Collider2D](Collider2D.html) or have moved a [Collider2D](Collider2D.html)
but a physics update has not yet taken place then the colliders will not be
shown as touching. This function returns the same collision results as the
physics collision or trigger callbacks.

* * *

## Declaration

public bool IsTouching([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter);

### Parameters

collider | The collider to check if it is touching any of the collider(s) attached to this rigidbody.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
  
### Returns

**bool** Whether the `collider` is touching any of the collider(s) attached to
this rigidbody or not.

### Description

Checks whether the `collider` is touching any of the collider(s) attached to
this rigidbody or not with the results filtered by the `ContactFilter2D`.

It is important to understand that checking whether colliders are touching or
not is performed against the last physics system update; that is the state of
touching colliders at that time. If you have just added a new
[Collider2D](Collider2D.html) or have moved a [Collider2D](Collider2D.html)
but a physics update has not yet taken place then the colliders will not be
shown as touching. This function returns the same collision results as the
physics collision or trigger callbacks.

* * *

## Declaration

public bool IsTouching([ContactFilter2D](ContactFilter2D.html) contactFilter);

### Parameters

contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
---|---  
  
### Returns

**bool** Whether any collider is touching any of the collider(s) attached to
this rigidbody or not.

### Description

Checks whether any collider is touching any of the collider(s) attached to
this rigidbody or not with the results filtered by the `ContactFilter2D`.

It is important to understand that checking whether colliders are touching or
not is performed against the last physics system update; that is the state of
touching colliders at that time. If you have just added a new
[Collider2D](Collider2D.html) or have moved a [Collider2D](Collider2D.html)
but a physics update has not yet taken place then the colliders will not be
shown as touching. This function returns the same collision results as the
physics collision or trigger callbacks.

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

