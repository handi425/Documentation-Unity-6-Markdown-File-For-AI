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

#
[QueryValidationOptions](Search.QueryValidationOptions.html).skipUnknownFilters

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

public bool skipUnknownFilters;

### Description

Boolean indicating if unknown filters should be skipped.

If true, unknown filters are skipped. If false and
[validateFilters](Search.QueryValidationOptions-validateFilters.html) is true,
unknown filters will generate errors if no default handler is provided with
[QueryEngine.SetDefaultFilter](Search.QueryEngine_1.SetDefaultFilter.html).

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryValidationOptions_skipUnknownFilters
    {
        [[MenuItem](MenuItem.html)("Examples/[QueryValidationOptions](Search.QueryValidationOptions.html)/skipUnknownFilters")]
        public static void RunExample()
        {
            // Set up the query validation options with filter validation and unknown filter skipping.
            var validationOptions = new [QueryValidationOptions](Search.QueryValidationOptions.html) { validateFilters = true, skipUnknownFilters = true};
    
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>(validationOptions);
            queryEngine.AddFilter("id", myObj => myObj.id);
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            var dataset = new[]
            {
                new MyObjectType() { id = 0, name = "Test 1" },
                new MyObjectType() { id = 10, name = "Test 2" }
            };
    
            // Parse a query with the filter "id". There shouldn't be any errors
            var query = queryEngine.ParseQuery("id>10");
            [Debug.Assert](Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
    
            // Because the [QueryEngine](Search.QueryEngine.html) is skipping unknown filter, there should not be errors for unknown filters
            // but it should still get results for filters that are known. If validateFilters were set
            // to false, this query would yield no results since the generated filter node for the unknown filter
            // would automatically return false for any elements of the filtered data set.
            query = queryEngine.ParseQuery("id<10 name:MyName");
            [Debug.Assert](Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
            var filteredData = query.Apply(dataset).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(dataset[0]), "Test 1 should be in the filtered list since its id is < 10");
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

