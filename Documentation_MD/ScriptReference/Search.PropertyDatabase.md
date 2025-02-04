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

# PropertyDatabase

class in UnityEditor.Search

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

The [PropertyDatabase](Search.PropertyDatabase.html) is a system that can
store, in a thread-safe manner, properties of different kinds into a single
file that we call a property database.

The idea of the [PropertyDatabase](Search.PropertyDatabase.html) is that most
of the time, fetching a property value can be costly. Therefore, caching those
values for reuse at a later time can save a lot of cycles. The cache is stored
in a file, so it is not lost on a domain reload or when quitting Unity (not
all types can be serialized in the file but they can still be stored in the
[PropertyDatabase](Search.PropertyDatabase.html), see
[PropertyDatabase.IsPersistedType](Search.PropertyDatabase.IsPersistedType.html)).
You can open multiple [PropertyDatabase](Search.PropertyDatabase.html)s on
different files, but you cannot open multiple
[PropertyDatabase](Search.PropertyDatabase.html)s on a single file. Doing so
will result in an invalid [PropertyDatabase](Search.PropertyDatabase.html)
(see [valid](Search.PropertyDatabase-valid.html)). You can do concurrent
operations on a single instance of a
[PropertyDatabase](Search.PropertyDatabase.html), but for performance reasons
you should use a view (see
[PropertyDatabase.GetView](Search.PropertyDatabase.GetView.html) and
[IPropertyDatabaseView](Search.IPropertyDatabaseView.html)).  
  
There are three main operations that you can do with the
[PropertyDatabase](Search.PropertyDatabase.html): storing values, loading
values and invalidating values. When storing values, the values are stored in
an array, sorted by their keys (see
[PropertyDatabase.CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html)
and [PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html). A key
is a number representing a document and a property. You can store any values
coming from anywhere in the [PropertyDatabase](Search.PropertyDatabase.html),
but the most common use case is to store properties of an asset or a game
object. In these cases, the asset or game object would be the document, and
the property is any property on that document you want to store. You can then
load those values at a later time, either for a single property or an entire
document.

    
    
    using System.Collections.Generic;
    using NUnit.Framework;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_PropertyDatabase
    {
        // Where the property database will be written.
        const string propertyDatabaseFilePath = "Temp/test_property_db";
    
        static [PropertyDatabase](Search.PropertyDatabase.html) propertyDatabase;
    
        static void InitializePropertyDatabase()
        {
            // Setup the property database. We configure it with automatic flushing so the file store
            // will be updated automatically after an update.
            propertyDatabase = new [PropertyDatabase](Search.PropertyDatabase.html)(propertyDatabaseFilePath, true);
        }
    
        static void ClearPropertyDatabase()
        {
            propertyDatabase.Clear();
    
            // Since we are done with the property database, we should dispose it
            // to clear all resources.
            propertyDatabase.Dispose();
        }
    
        static [PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html) GetPropertyKey(int id)
        {
            return [PropertyDatabase.CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html)((ulong)id / 100, [PropertyDatabase.CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html)((id % 100).ToString()));
        }
    
        static object LoadPropertyValue(int id)
        {
            var recordKey = GetPropertyKey(id);
            if (propertyDatabase.TryLoad(recordKey, out object value))
                return value;
    
            // Fetch the value with the time consuming operation and store it for future
            // accesses.
            value = id.ToString();
            propertyDatabase.Store(recordKey, value);
            return value;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[PropertyDatabase](Search.PropertyDatabase.html)/Class")]
        public static void RunExample()
        {
            InitializePropertyDatabase();
            if (!propertyDatabase.valid)
            {
                [Debug.LogFormat](Debug.LogFormat.html)([LogType.Error](LogType.Error.html), [LogOption.NoStacktrace](LogOption.NoStacktrace.html), null, $"[PropertyDatabase](Search.PropertyDatabase.html) \"{propertyDatabase.filePath}\" failed to open properly.");
                return;
            }
    
            var allValues = new Dictionary<int, object>();
            // Load the property values to do something with it.
            for (var i = 0; i < 1000; ++i)
            {
                var value = LoadPropertyValue(i);
                allValues.Add(i, value);
            }
    
            // Validate everything is in the database
            for (var i = 0; i < 1000; ++i)
            {
                var key = GetPropertyKey(i);
                if (!propertyDatabase.TryLoad(key, out object value))
                    Assert.Fail("Record should be in the database.");
                [Assert.AreEqual](Assertions.Assert.AreEqual.html)(i.ToString(), value);
            }
    
            ClearPropertyDatabase();
        }
    }
    

If a property or an entire document change, you can invalidate the stored
values with
[PropertyDatabase.Invalidate](Search.PropertyDatabase.Invalidate.html) and
[PropertyDatabase.InvalidateMask](Search.PropertyDatabase.InvalidateMask.html).

### Properties

[autoFlush](Search.PropertyDatabase-autoFlush.html)| Boolean indicating if the
PropertyDatabase will update the backing file automatically or not.  
---|---  
[filePath](Search.PropertyDatabase-filePath.html)| The file on which this
PropertyDatabase is opened.  
[valid](Search.PropertyDatabase-valid.html)| Boolean indicating if the
PropertyDatabase is valid.  
  
### Constructors

[PropertyDatabase](Search.PropertyDatabase-ctor.html)| Constructs a new
instance of a PropertyDatabase.  
---|---  
  
### Public Methods

[Clear](Search.PropertyDatabase.Clear.html)| Clears the entire content of the
PropertyDatabase.  
---|---  
[Dispose](Search.PropertyDatabase.Dispose.html)| Dispose of the resources used
by this PropertyDatabase.  
[Flush](Search.PropertyDatabase.Flush.html)| Triggers a manual update of the
backing file.  
[GetInfo](Search.PropertyDatabase.GetInfo.html)| Returns a formatted string
showing various information of the PropertyDatabase.  
[GetValueFromRecord](Search.PropertyDatabase.GetValueFromRecord.html)|
Deserialize a record value into its proper type.  
[GetView](Search.PropertyDatabase.GetView.html)| Opens a view on the
PropertyDatabase.  
[Invalidate](Search.PropertyDatabase.Invalidate.html)| Invalidates a single
property record so it is no longer retrievable.  
[InvalidateMask](Search.PropertyDatabase.InvalidateMask.html)| Invalidate all
properties stored from multiple documents that match a document key mask.  
[Store](Search.PropertyDatabase.Store.html)| Stores a document property.  
[TryLoad](Search.PropertyDatabase.TryLoad.html)| Loads a single property,
already deseriazed into an object.  
  
### Static Methods

[CreateDocumentKey](Search.PropertyDatabase.CreateDocumentKey.html)| Creates a
document key from a document identifier.  
---|---  
[CreatePropertyHash](Search.PropertyDatabase.CreatePropertyHash.html)| Creates
a property hash from a property path.  
[CreateRecordKey](Search.PropertyDatabase.CreateRecordKey.html)| Creates a
record key from a document identifier and a property path.  
[IsPersistableType](Search.PropertyDatabase.IsPersistableType.html)| Returns a
boolean indicating if a type can be persisted into the backing file.  
  
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

