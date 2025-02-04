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

#  [Physics2D](Physics2D.html).GetContacts

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

public static int GetContacts([Collider2D](Collider2D.html) collider,
Collider2D[] colliders);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
Colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` array.

### Description

Retrieves all Colliders in contact with the `Collider`.

When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
ContactPoint2D[] contacts);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points in contact with the `Collider`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, ContactPoint2D[]
contacts);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points in contact with the `Collider`, with the results
filtered by the `ContactFilter2D`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, Collider2D[]
colliders);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
Colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` array.

### Description

Retrieves all Colliders in contact with the `Collider`, with the results
filtered by the `ContactFilter2D`.

When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider1,
[Collider2D](Collider2D.html) collider2,
[ContactFilter2D](ContactFilter2D.html) contactFilter, ContactPoint2D[]
contacts);

### Parameters

collider1 | The Collider to check if it has contacts against `collider2`.  
---|---  
collider2 | The Collider to check if it has contacts against `collider1`.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points in for contacts between with the `collider1` and
`collider2`, with the results filtered by the `ContactFilter2D`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
ContactPoint2D[] contacts);

### Parameters

rigidbody | The rigidbody to retrieve contacts for. All Colliders attached to this rigidbody will be checked.  
---|---  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points in contact with any of the Collider(s) attached
to this rigidbody.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
Collider2D[] colliders);

### Parameters

rigidbody | The rigidbody to retrieve contacts for. All Colliders attached to this rigidbody will be checked.  
---|---  
Colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` array.

### Description

Retrieves all Colliders in contact with any of the Collider(s) attached to
this rigidbody.

When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
[ContactFilter2D](ContactFilter2D.html) contactFilter, ContactPoint2D[]
contacts);

### Parameters

rigidbody | The rigidbody to retrieve contacts for. All Colliders attached to this rigidbody will be checked.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | An array of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` array.

### Description

Retrieves all contact points in contact with any of the Collider(s) attached
to this rigidbody, with the results filtered by the `ContactFilter2D`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
[ContactFilter2D](ContactFilter2D.html) contactFilter, Collider2D[]
colliders);

### Parameters

rigidbody | The rigidbody to retrieve contacts for. All Colliders attached to this rigidbody will be checked.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
Colliders | An array of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` array.

### Description

Retrieves all Colliders in contact with any of the Collider(s) attached to
this rigidbody, with the results filtered by the `ContactFilter2D`.

When retrieving contacts, you should ensure that the provided array is large
enough to contain all the contacts you are interested in. Typically the array
would be reused therefore it would be a size to return a reasonable quantity
of contacts. This function also means that no allocations occur which means no
work is produced for the garbage collector.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
List<Collider2D> colliders);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
Colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` list.

### Description

Retrieves all Colliders in contact with the `Collider`.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<Collider2D>
colliders);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
Colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` list.

### Description

Retrieves all Colliders in contact with the `Collider`, with the results
filtered by the `contactFilter2D`.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
List<ContactPoint2D> contacts);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points in contact with the `Collider`.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<ContactPoint2D>
contacts);

### Parameters

Collider | The Collider to retrieve contacts for.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points in contact with the `Collider`, with the results
filtered by the `contactFilter2D`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Collider2D](Collider2D.html) collider1,
[Collider2D](Collider2D.html) collider2,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<ContactPoint2D>
contacts);

### Parameters

collider1 | The Collider to check if it has contacts against `collider2`.  
---|---  
collider2 | The Collider to check if it has contacts against `collider1`.  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points in for contacts between with the `collider1` and
`collider2`, with the results filtered by the `contactFilter2D`.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.
This is true even if the `contactFilter` has its
[ContactFilter2D.useTriggers](ContactFilter2D-useTriggers.html) set to true.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
List<Collider2D> colliders);

### Parameters

rigidbody | The Rigidbody to retrieve contacts for. All Colliders attached to this Rigidbody will be checked.  
---|---  
Colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` list.

### Description

Retrieves all Colliders in contact with any of the Collider(s) attached to
this Rigidbody.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<Collider2D>
colliders);

### Parameters

rigidbody | The Rigidbody to retrieve contacts for. All Colliders attached to this Rigidbody will be checked.  
---|---  
contactFilter | The contact filter used to filter the results differently, such as by layer mask, Z depth, or normal angle.  
Colliders | A list of [Collider2D](Collider2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of Colliders placed in the `Colliders` list.

### Description

Retrieves all Colliders in contact with any of the Collider(s) attached to
this Rigidbody, with the results filtered by the `contactFilter2D`.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
List<ContactPoint2D> contacts);

### Parameters

rigidbody | The Rigidbody to retrieve contacts for. All Colliders attached to this Rigidbody will be checked.  
---|---  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all contact points in contact with any of the Collider(s) attached
to this Rigidbody.

Contacts involving a [Collider2D](Collider2D.html) set to be a trigger will
never be returned here because trigger Colliders do not have contact points.  
  
The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

* * *

## Declaration

public static int GetContacts([Rigidbody2D](Rigidbody2D.html) rigidbody,
[ContactFilter2D](ContactFilter2D.html) contactFilter, List<ContactPoint2D>
contacts);

### Parameters

rigidbody | The Rigidbody to retrieve contacts for. All Colliders attached to this Rigidbody will be checked.  
---|---  
contactFilter | Returns the number of contacts placed in the `contacts` list.  
contacts | A list of [ContactPoint2D](ContactPoint2D.html) used to receive the results.  
  
### Returns

**int** Returns the number of contacts placed in the `contacts` list.

### Description

Retrieves all Colliders in contact with any of the Collider(s) attached to
this Rigidbody, with the results filtered by the `contactFilter2D`.

The integer return value is the number of results written into the `results`
list. The results list will be resized if it doesn't contain enough elements
to report all the results. This prevents memory from being allocated for
results when the `results` list does not need to be resized, and improves
garbage collection performance when the query is performed frequently.  
  
The results can also be filtered by the `contactFilter`.  
  
Additional resources: [Collider2D.GetContacts](Collider2D.GetContacts.html)
and [Rigidbody2D.GetContacts](Rigidbody2D.GetContacts.html).

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

