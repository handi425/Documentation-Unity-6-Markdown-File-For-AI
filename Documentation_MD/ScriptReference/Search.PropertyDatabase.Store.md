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

#  [PropertyDatabase](Search.PropertyDatabase.html).Store

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

public bool Store(string documentId, string propertyPath, object value);

### Parameters

documentId | A document identifier.  
---|---  
propertyPath | A property path or name.  
value | The value of the property.  
  
### Returns

**bool** True if the store operation succeeded, false if not.

### Description

Stores a document property.

    
    
    // Store a property of a document, like a property of an asset.
    var stored = propertyDatabase.Store("path/to/my/asset", "m_Color", new [Color](Color.html)(1, 0, 1));
    if (!stored)
        [Debug.LogWarning](Debug.LogWarning.html)("Property m_Color did not store.");
    

* * *

## Declaration

public bool Store(ulong documentKey, [Hash128](Hash128.html) propertyHash,
object value);

### Parameters

documentKey | A document key.  
---|---  
propertyHash | A property hash.  
value | The value of the property.  
  
### Returns

**bool** True if the store operation succeeded, false if not.

### Description

Stores a document property with a precomputed document key and property hash.

    
    
    // Store a property of a document, with the document id and property hash already computed.
    var documentId = [PropertyDatabase.CreateDocumentKey](Search.PropertyDatabase.CreateDocumentKey.html)("path/to/my/asset");
    var propertyHash = [PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html)("m_Size");
    stored = propertyDatabase.Store(documentId, propertyHash, 42);
    if (!stored)
        [Debug.LogWarning](Debug.LogWarning.html)("Property m_Size did not store.");
    

Additional resources:
[PropertyDatabase.CreateDocumentKey](Search.PropertyDatabase.CreateDocumentKey.html)
and
[PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html).

* * *

## Declaration

public bool Store(ref
[Search.PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html)
recordKey, object value);

### Parameters

recordKey | A record key.  
---|---  
value | The value of the property.  
  
### Returns

**bool** True if the store operation succeeded, false if not.

### Description

Stores a document property with a precomputed record key.

    
    
    // Store a property with an already computed record key.
    var recordKey = [PropertyDatabase.CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html)("path/to/my/asset", "prop1");
    stored = propertyDatabase.Store(recordKey, 123);
    if (!stored)
        [Debug.LogWarning](Debug.LogWarning.html)("Property prop1 did not store.");
    

Additional resources:
[PropertyDatabase.CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html).

* * *

## Declaration

public bool Store([Hash128](Hash128.html) propertyHash, object value);

### Parameters

propertyHash | A property hash.  
---|---  
value | The value of the property.  
  
### Returns

**bool** True if the store operation succeeded, false if not.

### Description

Stores a property with a precomputed property hash.

The document identifier is considered null and the document key will be 0.

    
    
    // Store a property without any document.
    stored = propertyDatabase.Store([PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html)("documentPrefix"), "myDocs_");
    if (!stored)
        [Debug.LogWarning](Debug.LogWarning.html)("Property documentPrefix did not store.");
    

Additional resources:
[PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html).

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

