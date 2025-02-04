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

# PropertyDatabaseRecordKey

struct in UnityEditor.Search

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

### Description

The key of a record that is stored in the
[PropertyDatabase](Search.PropertyDatabase.html).

A key is a numerical value that represents a description of the property being
stored in the [PropertyDatabase](Search.PropertyDatabase.html). It is composed
of two parts, the document key and the property key.  
  
The document key represents what document owns the property, and the property
key represents the property itself. For example, if you wish to store the size
of a file, the file would be the document and the size would be the property.
You can use any value for your documents, as long as it is consistent when
storing multiple properties of a single document. You can also not use a
document, in which case the document key will be 0.  
  
We provide multiple helper functions to help create record keys, see
[PropertyDatabase.CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html),
[PropertyDatabase.CreateDocumentKey](Search.PropertyDatabase.CreateDocumentKey.html)
and
[PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html).

### Static Properties

[size](Search.PropertyDatabaseRecordKey-size.html)| The size of the key, in
bytes.  
---|---  
  
### Properties

[documentKey](Search.PropertyDatabaseRecordKey-documentKey.html)| The key of
the document owning the property.  
---|---  
[propertyKey](Search.PropertyDatabaseRecordKey-propertyKey.html)| The key of
the property.  
  
### Constructors

[PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey-ctor.html)|
Constructs a new record key.  
---|---  
  
### Public Methods

[CompareTo](Search.PropertyDatabaseRecordKey.CompareTo.html)| Compares the
record key to another record key.  
---|---  
[Equals](Search.PropertyDatabaseRecordKey.Equals.html)| Tests equality with
another record key.  
[GetHashCode](Search.PropertyDatabaseRecordKey.GetHashCode.html)| Gets the
hashcode of the key.  
  
### Operators

[operator !=](Search.PropertyDatabaseRecordKey-operator_ne.html)| The not
equal operator.  
---|---  
[operator <](Search.PropertyDatabaseRecordKey-operator_lt.html)| The less than
operator.  
[operator ==](Search.PropertyDatabaseRecordKey-operator_eq.html)| The equals
operator.  
[operator >](Search.PropertyDatabaseRecordKey-operator_gt.html)| The greater
than operator.  
  
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

