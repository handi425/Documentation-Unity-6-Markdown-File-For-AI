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

# IQueryEngineFilter

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

Interface for the [QueryEngine](Search.QueryEngine_1.html) filters.

When you add a new filter on a [QueryEngine](Search.QueryEngine_1.html), you
receive a filter object that implements the interface
[IQueryEngineFilter](Search.IQueryEngineFilter.html). You can modify this
filter to override the global behaviors of the
[QueryEngine](Search.QueryEngine_1.html). For example, you can add [type
parsers](Search.IQueryEngineFilter.AddTypeParser.html) or
[operators](Search.IQueryEngineFilter.AddOperator.html) that are specific to
this filter.

    
    
    using System.Collections.Generic;
    using System.Globalization;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_IQueryEngineFilter
    {
        static List<MyObjectType> s_Data;
    
        static [QueryEngine](Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
    
            // Add a filter for MyObjectType.position that supports equals and not equals
            queryEngine.AddFilter("p", myObj => myObj.position, new[] { "=", "!=" });
    
            // Add a new type parser for [Vector2](Vector2.html) written as "[x, y]", but only for this filter.
            // This type parser will not affect other filters.
            queryEngine.TryGetFilter("p", out var filter);
            filter.AddTypeParser(s =>
            {
                // If the format requirement is not met, return a failure.
                if (!s.StartsWith("[") || !s.EndsWith("]"))
                    return ParseResult<[Vector2](Vector2.html)>.none;
    
                var trimmed = s.Trim('[', ']');
                var vectorTokens = trimmed.Split(',');
                var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
                if (vectorValues.Count != 2)
                    return ParseResult<[Vector2](Vector2.html)>.none;
                var vector = new [Vector2](Vector2.html)(vectorValues[0], vectorValues[1]);
    
                // When the conversion succeeds, return a success.
                return new ParseResult<[Vector2](Vector2.html)>(true, vector);
            });
    
            // Override global operators with specific operator handlers for this filter
            filter.AddOperator("=").AddHandler(([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev == fv);
            filter.AddOperator("!=").AddHandler(([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev != fv);
    
            // Set up what data from objects of type MyObjectType will be matched against search words
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            return queryEngine;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[IQueryEngineFilter](Search.IQueryEngineFilter.html)/[IQueryEngineFilter](Search.IQueryEngineFilter.html)")]
        public static void RunExample()
        {
            s_Data = GenerateExampleData();
            var queryEngine = SetupQueryEngine();
            TestFiltering(queryEngine, s_Data);
        }
    
        static void TestFiltering([QueryEngine](Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> inputData)
        {
            var vec = new [Vector2](Vector2.html)(1, 0);
            // Find objects that are at position [1, 0]
            var filteredData = FilterData("p=[1,0]", queryEngine, inputData);
            ValidateData(filteredData, s_Data.Where(myObj => myObj.position == vec));
    
            //Find objects that are not at position [1, 0]
            filteredData = FilterData("p!=[1,0]", queryEngine, inputData);
            ValidateData(filteredData, s_Data.Where(myObj => myObj.position != vec));
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
                new MyObjectType { id = 3, name = "Test 4", position = new [Vector2](Vector2.html)(1.2f, 0), active = false },
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

[metaInfo](Search.IQueryEngineFilter-metaInfo.html)| Additional information
specific to the filter.  
---|---  
[operators](Search.IQueryEngineFilter-operators.html)| Collection of
QueryFilterOperators specific for the filter.  
[overridesStringComparison](Search.IQueryEngineFilter-
overridesStringComparison.html)| Indicates if the filter overrides the global
string comparison options.  
[parameterType](Search.IQueryEngineFilter-parameterType.html)| The type of the
constant parameter passed to the filter, if used.  
[regexToken](Search.IQueryEngineFilter-regexToken.html)| The regular
expression that matches the filter. Matches what precedes the operator in a
filter (for example. "id" in "id>=2").  
[stringComparison](Search.IQueryEngineFilter-stringComparison.html)| The
string comparison options of the filter.  
[supportedOperators](Search.IQueryEngineFilter-supportedOperators.html)| List
of supported operators.  
[token](Search.IQueryEngineFilter-token.html)| The identifier of the filter.
Typically what precedes the operator in a filter (for example, "id" in
"id>=2").  
[type](Search.IQueryEngineFilter-type.html)| The type of the data that is
compared by the filter.  
[usesParameter](Search.IQueryEngineFilter-usesParameter.html)| Indicates if
the filter uses a parameter.  
[usesRegularExpressionToken](Search.IQueryEngineFilter-
usesRegularExpressionToken.html)| Indicates if the filter uses a regular
expression token or not.  
[usesResolver](Search.IQueryEngineFilter-usesResolver.html)| Indicates if the
filter uses a resolver function.  
  
### Public Methods

[AddOperator](Search.IQueryEngineFilter.AddOperator.html)| Add a custom filter
operator specific to the filter.  
---|---  
[AddOrUpdateMetaInfo](Search.IQueryEngineFilter.AddOrUpdateMetaInfo.html)| Add
or update additional information specific to the filter.  
[AddTypeParser](Search.IQueryEngineFilter.AddTypeParser.html)| Add a type
parser specific to the filter.  
[ClearMetaInfo](Search.IQueryEngineFilter.ClearMetaInfo.html)| Removes all
additional information specific to the filter.  
[RemoveMetaInfo](Search.IQueryEngineFilter.RemoveMetaInfo.html)| Remove
information on the filter.  
[RemoveOperator](Search.IQueryEngineFilter.RemoveOperator.html)| Remove a
custom operator specific to the filter.  
[SetNestedQueryTransformer](Search.IQueryEngineFilter.SetNestedQueryTransformer.html)|
Sets the filter's nested query transformer function. This function takes the
result of a nested query and extracts the necessary data to compare with the
filter.  
  
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

