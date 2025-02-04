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

#  [IPropertyDatabaseView](Search.IPropertyDatabaseView.html).TryLoad

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

public bool TryLoad(InAttribute) recordKey, out object data);

### Parameters

recordKey | A record key.  
---|---  
data | The property value.  
  
### Returns

**bool** True if the record is found and is valid, false otherwise.

### Description

Loads a single property, already deseriazed into an object.

    
    
    // Load the value already deserialized.
    using (var view = propertyDatabase.GetView())
    {
        var colorRecordKey = view.CreateRecordKey("path/to/my/asset", "m_Color");
        if (!view.TryLoad(colorRecordKey, out object colorObject))
            Assert.Fail("Failed to load color property.");
        var color = ([Color](Color.html))colorObject;
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)(new [Color](Color.html)(1, 0, 1), color);
    }
    
    

Additional resources:
[IPropertyDatabaseView.CreateRecordKey](Search.IPropertyDatabaseView.CreateRecordKey.html).

* * *

## Declaration

public bool TryLoad(InAttribute) recordKey, out
[Search.IPropertyDatabaseRecordValue](Search.IPropertyDatabaseRecordValue.html)
data);

### Parameters

recordKey | A record key.  
---|---  
data | The property record.  
  
### Returns

**bool** True if the record is found and is valid, false otherwise.

### Description

Loads a single property, still contained within a record.

This method doesn't deserialize the value. You have to deserialize it yourself
by calling
[IPropertyDatabaseView.GetObjectFromRecordValue](Search.IPropertyDatabaseView.GetObjectFromRecordValue.html).

    
    
    // Load the record value to do a deserialization at the appropriate time.
    using (var view = propertyDatabase.GetView())
    {
        var sizeRecordKey = view.CreateRecordKey("path/to/my/asset", "m_Size");
        if (!view.TryLoad(sizeRecordKey, out [IPropertyDatabaseRecordValue](Search.IPropertyDatabaseRecordValue.html) sizeRecordValue))
            Assert.Fail("Failed to load size property.");
        var size = view.GetValueFromRecord<int>(sizeRecordValue);
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)(42, size);
    }
    
    

Additional resources:
[IPropertyDatabaseView.CreateRecordKey](Search.IPropertyDatabaseView.CreateRecordKey.html).

* * *

## Declaration

public bool TryLoad(ulong documentKey, out IEnumerable<object> data);

### Parameters

documentKey | A document key.  
---|---  
data | The document property values.  
  
### Returns

**bool** True if the record is found and is valid, false otherwise.

### Description

Loads all the properties of a document, already deseriazed into objects.

    
    
    // Load all values not associated with a document, already deserialized.
    using (var view = propertyDatabase.GetView())
    {
        var nullDocumentKey = view.CreateDocumentKey(null);
        if (!view.TryLoad(nullDocumentKey, out IEnumerable<object> noDocumentProperties))
            Assert.Fail("Failed to load properties with no documents.");
        Assert.IsNotEmpty(noDocumentProperties);
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)("myDocs_", noDocumentProperties.First());
    }
    
    

Additional resources:
[IPropertyDatabaseView.CreateDocumentKey](Search.IPropertyDatabaseView.CreateDocumentKey.html).

* * *

## Declaration

public bool TryLoad(ulong documentKey, out
IEnumerable<IPropertyDatabaseRecord> records);

### Parameters

documentKey | A document key.  
---|---  
records | The document property records.  
  
### Returns

**bool** True if the record is found and is valid, false otherwise.

### Description

Loads all the properties of a document, still contained within records.

This method doesn't deserialize the values. You have to deserialize them
yourself by calling
[IPropertyDatabaseView.GetObjectFromRecordValue](Search.IPropertyDatabaseView.GetObjectFromRecordValue.html).

    
    
    // Load all values associated with a document, not deserialized.
    using (var view = propertyDatabase.GetView())
    {
        var myAssetDocumentKey = view.CreateDocumentKey("path/to/my/asset");
        if (!view.TryLoad(myAssetDocumentKey, out IEnumerable<[IPropertyDatabaseRecord](Search.IPropertyDatabaseRecord.html)> myDocumentRecords))
            Assert.Fail("Failed to load records for my asset document.");
        var deserializedValues = new Dictionary<[PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html), object>();
        foreach (var myDocumentRecord in myDocumentRecords)
        {
            var value = view.GetValueFromRecord<object>(myDocumentRecord.value);
            deserializedValues.Add(myDocumentRecord.key, value);
        }
    
        [Assert.AreEqual](Assertions.Assert.AreEqual.html)(5, deserializedValues.Count);
    }
    
    

Additional resources:
[IPropertyDatabaseView.CreateDocumentKey](Search.IPropertyDatabaseView.CreateDocumentKey.html).

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

