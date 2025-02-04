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

#  [ParsedQuery<T0>](Search.ParsedQuery_1.html).returnPayloadIfEmpty

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

public bool returnPayloadIfEmpty;

### Description

Boolean. Indicates if the original payload should be returned when the query
is empty.

If set to true, returns the original payload when the query is empty. If set
to false, returns an empty array.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_ParsedQuery_returnPayloadIfEmpty
    {
        static List<MyObjectType> s_Data;
    
        [[MenuItem](MenuItem.html)("Examples/ParsedQuery/returnPayloadIfEmpty")]
        public static void RunExample()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
            queryEngine.AddFilter("id", myObj => myObj.id);
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            s_Data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, name = "Test 1", position = new [Vector2](Vector2.html)(0, 0), active = false },
                new MyObjectType { id = 1, name = "Test 2", position = new [Vector2](Vector2.html)(0, 1), active = true }
            };
    
            // When setting "returnPayloadIfEmpty" to true, empty queries
            // will return the same data set that was passed as input. Otherwise,
            // it will return an empty set.
            var query = queryEngine.ParseQuery("");
            var filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == s_Data.Count, "Filtered data should have the same number of items as the input to the query.");
            for (var i = 0; i < filteredData.Count; ++i)
            {
                [Debug.Assert](Debug.Assert.html)(filteredData[i] == s_Data[i], $"Filtered data at index {i} should be the same as the input.");
            }
        }
    
        class MyObjectType
        {
            public int id { get; set; }
            public string name { get; set; } = string.Empty;
            public [Vector2](Vector2.html) position { get; set; } = [Vector2.zero](Vector2-zero.html);
            public bool active { get; set; }
    
            public override string ToString()
            {
                return $"({id}, {name}, ({position.x}, {position.y}), {active})";
            }
        }
    }
    

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

