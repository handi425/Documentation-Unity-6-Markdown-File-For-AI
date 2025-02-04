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

# IPropertyDatabaseView

interface in UnityEditor.Search

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

Interface of a [PropertyDatabase](Search.PropertyDatabase.html) view.

The idea of a [PropertyDatabase](Search.PropertyDatabase.html) view is similar
to Windows' memory-mapped file views, although much simpler. Each
[PropertyDatabase](Search.PropertyDatabase.html) view has its own filestream
that can access the [PropertyDatabase](Search.PropertyDatabase.html)
independently from other views. The views of a single
[PropertyDatabase](Search.PropertyDatabase.html) are synchronized, so
concurrent accesses are allowed. However, for concurrent accesses to work
properly each thread must have its own instance of a view.  
  
All operations available on the
[PropertyDatabase](Search.PropertyDatabase.html) class are available on the
view itself. When operating directly on the
[PropertyDatabase](Search.PropertyDatabase.html) instance, an internal view is
created to handle all the synchronization. Since we are dealing with files,
opening a view has a non-negligible cost. Therefore, it is recommended to open
a view once, and use it as long as possible before disposing it.

    
    
    using System.Collections.Generic;
    using NUnit.Framework;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_IPropertyDatabaseView
    {
        // Where the property database will be written.
        const string propertyDatabaseFilePath = "Temp/test_ipropertydatabaseview_db";
    
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
            propertyDatabase.Dispose();
        }
    
        static [PropertyDatabaseRecordKey](Search.PropertyDatabaseRecordKey.html) GetPropertyKey(int id, [IPropertyDatabaseView](Search.IPropertyDatabaseView.html) view)
        {
            return view.CreateRecordKey((ulong)id / 100, view.CreatePropertyHash((id % 100).ToString()));
        }
    
        static object LoadPropertyValue(int id, [IPropertyDatabaseView](Search.IPropertyDatabaseView.html) view)
        {
            var recordKey = GetPropertyKey(id, view);
            if (view.TryLoad(recordKey, out object value))
                return value;
    
            // Fetch the value with the time consuming operation and store it for future
            // accesses.
            value = id.ToString();
            view.Store(recordKey, value);
            return value;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[IPropertyDatabaseView](Search.IPropertyDatabaseView.html)/Interface")]
        public static void RunExample()
        {
            InitializePropertyDatabase();
            if (!propertyDatabase.valid)
            {
                [Debug.LogFormat](Debug.LogFormat.html)([LogType.Error](LogType.Error.html), [LogOption.NoStacktrace](LogOption.NoStacktrace.html), null, $"[PropertyDatabase](Search.PropertyDatabase.html) \"{propertyDatabase.filePath}\" failed to open properly.");
                return;
            }
    
            // Doing a change on the property database internally opens a view on the actual data,
            // which is non negligible. Therefore, it is advised to open a view once and use it as much as you
            // can.
            // Note: when doing concurrent accesses to the property database, each thread must have its own
            // view instance.
            var allValues = new Dictionary<int, object>();
            using (var view = propertyDatabase.GetView())
            {
                for (var i = 0; i < 1000; ++i)
                {
                    var value = LoadPropertyValue(i, view);
                    allValues.Add(i, value);
                }
            }
    
            // Validate everything is in the database
            using (var view = propertyDatabase.GetView())
            {
                for (var i = 0; i < 1000; ++i)
                {
                    var key = GetPropertyKey(i, view);
                    if (!view.TryLoad(key, out object value))
                        Assert.Fail("Record should be in the database.");
                    [Assert.AreEqual](Assertions.Assert.AreEqual.html)(i.ToString(), value);
                }
            }
    
            ClearPropertyDatabase();
        }
    }
    

Additional resources:
[PropertyDatabase.GetView](Search.PropertyDatabase.GetView.html)

### Public Methods

[Clear](Search.IPropertyDatabaseView.Clear.html)| Clears the entire content of
the PropertyDatabase.  
---|---  
[CreateDocumentKey](Search.IPropertyDatabaseView.CreateDocumentKey.html)|
Creates a document key from a document identifier.  
[CreatePropertyHash](Search.IPropertyDatabaseView.CreatePropertyHash.html)|
Creates a property hash from a property path.  
[CreateRecordKey](Search.IPropertyDatabaseView.CreateRecordKey.html)| Creates
a record key from a document identifier and a property path.  
[EnumerateAll](Search.IPropertyDatabaseView.EnumerateAll.html)| Enumerates all
records stored in the PropertyDatabase  
[GetValueFromRecord](Search.IPropertyDatabaseView.GetValueFromRecord.html)|
Deserialize a record value into its proper type.  
[Invalidate](Search.IPropertyDatabaseView.Invalidate.html)| Invalidates a
single property record so it is no longer retrievable.  
[InvalidateMask](Search.IPropertyDatabaseView.InvalidateMask.html)| Invalidate
all properties stored from multiple documents that match a document key mask.  
[IsPersistableType](Search.IPropertyDatabaseView.IsPersistableType.html)|
Returns a boolean indicating if a type can be persisted into the backing file.  
[Store](Search.IPropertyDatabaseView.Store.html)| Stores a document property.  
[Sync](Search.IPropertyDatabaseView.Sync.html)| Synchronizes the views so they
have access to the same content.  
[TryLoad](Search.IPropertyDatabaseView.TryLoad.html)| Loads a single property,
already deseriazed into an object.  
  
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

