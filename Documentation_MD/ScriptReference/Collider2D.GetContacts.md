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

#  [Collider2D](Collider2D.html).GetContacts

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

Retrieves all contact points for this Collider.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
You should pass an array that is large enough to contain all the contacts you
want returned. This array would typically be reused so it should be of a size
that can return a reasonable quantity of contacts. No allocations occur in
this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts(Collider2D[] colliders);

### Parameters

colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
---|---  
  
### Returns

**int** Returns the number of contacts placed in the `colliders` array.

### Description

Retrieves all colliders in contact with this Collider.

You should pass an array that is large enough to contain all the contacts you
want returned. This array would typically be reused so it should be of a size
that can return a reasonable quantity of contacts. No allocations occur in
this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts([ContactFilter2D](ContactFilter2D.html) contactFilter,
ContactPoint2D[] contacts);

### Parameters

contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
---|---  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points for this Collider, with the results filtered by
the `contactFilter`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
You should pass an array that is large enough to contain all the contacts you
want returned. This array would typically be reused so it should be of a size
that can return a reasonable quantity of contacts. No allocations occur in
this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts([ContactFilter2D](ContactFilter2D.html) contactFilter,
Collider2D[] colliders);

### Parameters

contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
---|---  
colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of colliders placed in the `colliders` array.

### Description

Retrieves all colliders in contact with this Collider, with the results
filtered by the `contactFilter`.

You should pass an array that is large enough to contain all the contacts you
want returned. This array would typically be reused so it should be of a size
that can return a reasonable quantity of contacts. No allocations occur in
this function which means no work is produced for the garbage collector.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts(List<ContactPoint2D> contacts);

### Parameters

contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
---|---  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points for this Collider.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
The results list will be resized if it doesn't contain enough elements to
report all the results. This prevents memory from being allocated for results
when the `results` list does not need to be resized, and improves garbage
collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts(List<Collider2D> colliders);

### Parameters

colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
---|---  
  
### Returns

**int** Returns the number of contacts placed in the `colliders` list.

### Description

Retrieves all colliders in contact with this Collider.

The results list will be resized if it doesn't contain enough elements to
report all the results.This prevents memory from being allocated for results
when the `results` list does not need to be resized, and improves garbage
collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts([ContactFilter2D](ContactFilter2D.html) contactFilter,
List<ContactPoint2D> contacts);

### Parameters

contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
---|---  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points for this Collider, with the results filtered by
the `contactFilter`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
The results list will be resized if it doesn't contain enough elements to
report all the results. This prevents memory from being allocated for results
when the `results` list does not need to be resized, and improves garbage
collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

* * *

## Declaration

public int GetContacts([ContactFilter2D](ContactFilter2D.html) contactFilter,
List<Collider2D> colliders);

### Parameters

contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
---|---  
colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `colliders` list.

### Description

Retrieves all colliders in contact with this Collider, with the results
filtered by the `contactFilter`.

The results list will be resized if it doesn't contain enough elements to
report all the results. This prevents memory from being allocated for results
when the `results` list does not need to be resized, and improves garbage
collection performance when the query is performed frequently.  
  
Additional resources: [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html)
and [Physics2D.GetContacts](Physics2D.GetContacts.html).

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

