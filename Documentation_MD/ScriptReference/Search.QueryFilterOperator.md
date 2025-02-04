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

# QueryFilterOperator

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

A QueryFilterOperator defines a boolean operator between a value returned by a
filter and an operand inputted in the search query.

You get an object of this type whenever you add a new operator on a
[QueryEngine](Search.QueryEngine_1.html) or
[IQueryEngineFilter](Search.IQueryEngineFilter.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryFilterOperator
    {
        static List<MyObjectType> s_Data;
    
        static [QueryEngine](Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
    
            // Add a filter for MyObjectType.id that supports all operators
            queryEngine.AddFilter("id", myObj => myObj.id);
    
            // Add a new modulo operator on this filter
            var op = "%";
            queryEngine.TryGetFilter("id", out var filter);
            filter.AddOperator(op)
                .AddHandler((int ev, int fv) => ev % fv == 0)
                .AddHandler((float ev, float fv) => Math.Abs(ev % fv) < 0.00000001f);
    
            return queryEngine;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[QueryFilterOperator](Search.QueryFilterOperator.html)/Class")]
        public static void RunExample()
        {
            s_Data = GenerateExampleData();
            var queryEngine = SetupQueryEngine();
            TestFiltering(queryEngine, s_Data);
        }
    
        static void TestFiltering([QueryEngine](Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> inputData)
        {
            // Find objects that have an even id
            var filteredData = FilterData("id%2", queryEngine, inputData);
            ValidateData(filteredData, s_Data.Where(myObj => myObj.id % 2 == 0));
    
            // Find objects that have an odd id
            filteredData = FilterData("-id%2", queryEngine, inputData);
            ValidateData(filteredData, s_Data.Where(myObj => myObj.id % 2 != 0));
        }
    
        static IEnumerable<MyObjectType> FilterData(string inputQuery, [QueryEngine](Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> inputData)
        {
            // Parse the query string into a query operation
            var query = queryEngine.ParseQuery(inputQuery);
    
            // If the query is not valid, print all errors and return an empty data set
            if (!query.valid)
            {
                foreach (var queryError in query.errors)
                {
                    [Debug.LogFormat](Debug.LogFormat.html)([LogType.Error](LogType.Error.html), [LogOption.NoStacktrace](LogOption.NoStacktrace.html), null, $"[Error](PackageManager.Error.html) parsing input at {queryError.index}: {queryError.reason}");
                }
    
                return new List<MyObjectType>();
            }
    
            // Apply the query on a data set and get the filtered result.
            var filteredData = query.Apply(inputData);
            return filteredData;
        }
    
        static void ValidateData(IEnumerable<MyObjectType> filteredData, IEnumerable<MyObjectType> expectedData)
        {
            var filteredDataArray = filteredData.ToArray();
            var expectedDataArray = expectedData.ToArray();
            [Debug.Assert](Debug.Assert.html)(filteredDataArray.Length == expectedDataArray.Length, $"Filtered data should have {expectedDataArray.Length} elements.");
            if (filteredDataArray.Length != expectedDataArray.Length)
                return;
    
            for (var i = 0; i < expectedDataArray.Length; i++)
            {
                [Debug.Assert](Debug.Assert.html)(filteredDataArray[i] == expectedDataArray[i], $"{filteredDataArray[i]} should be equal to {expectedDataArray[i]}");
            }
        }
    
        static List<MyObjectType> GenerateExampleData()
        {
            var data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, name = "Test 1", position = new [Vector2](Vector2.html)(0, 0), active = false },
                new MyObjectType { id = 1, name = "Test 2", position = new [Vector2](Vector2.html)(0, 1), active = true },
                new MyObjectType { id = 2, name = "Test 3", position = new [Vector2](Vector2.html)(1, 0), active = false },
                new MyObjectType { id = 3, name = "Test 4", position = new [Vector2](Vector2.html)(1, 1), active = true },
                new MyObjectType { id = 4, name = "Test 5", position = new [Vector2](Vector2.html)(2, 0), active = false },
                new MyObjectType { id = 5, name = "Test 6", position = new [Vector2](Vector2.html)(0, 2), active = true }
            };
    
            return data;
        }
    
        /// <summary>
        /// Custom type. This is the type of objects that will be searched by the [QueryEngine](Search.QueryEngine.html).
        /// </summary>
        class MyObjectType
        {
            public int id { get; set; }
            public string name { get; set; }
            public [Vector2](Vector2.html) position { get; set; }
            public bool active { get; set; }
    
            public MyObjectType()
            {
                id = 0;
                name = "";
                position = [Vector2.zero](Vector2-zero.html);
                active = false;
            }
    
            public override string ToString()
            {
                return $"({id}, {name}, ({position.x}, {position.y}), {active})";
            }
        }
    }
    

### Properties

[token](Search.QueryFilterOperator-token.html)| The operator identifier.  
---|---  
[valid](Search.QueryFilterOperator-valid.html)| Indicates if this filter
operator is valid.  
  
### Public Methods

[AddHandler](Search.QueryFilterOperator.AddHandler.html)| Adds a custom filter
operator handler.  
---|---  
  
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

