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

#  [Collision2D](Collision2D.html).GetContacts

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

public int GetContacts(ContactPoint2D[] contacts);

### Parameters

contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
---|---  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points for contacts between
[collider](Collision2D-collider.html) and
[otherCollider](Collision2D-otherCollider.html).

When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. The array is usually
reused, so it should be large enough to return a reasonable quantity of
contacts. This function also means that no allocations occur, which means no
work is produced for the garbage collector.  
  
You can check how many contacts are available using
[contactCount](Collision2D-contactCount.html).  
  
Additional resources: [Physics2D.GetContacts](Physics2D.GetContacts.html),
[Collider2D.GetContacts](Collider2D.GetContacts.html) and
[Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public int GetContacts(List<ContactPoint2D> contacts);

### Parameters

contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
---|---  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points for contacts between
[collider](Collision2D-collider.html) and
[otherCollider](Collision2D-otherCollider.html).

When retrieving contacts, try to make the provided list large enough to
contain all the contacts you need. If the list is not large enough, Unity will
automatically increase its size so that it can contain all the contacts. The
list is usually reused, so it should be large enough to return a reasonable
quantity of contacts. If the list does not have to be increased in size then
this function will not allocate any memory, which means no work is produced
for the garbage collector.  
  
You can check how many contacts are available using
[contactCount](Collision2D-contactCount.html).  
  
Additional resources: [Physics2D.GetContacts](Physics2D.GetContacts.html),
[Collider2D.GetContacts](Collider2D.GetContacts.html) and
[Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

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

