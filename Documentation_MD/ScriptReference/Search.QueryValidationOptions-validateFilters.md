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
[QueryValidationOptions](Search.QueryValidationOptions.html).validateFilters

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

public bool validateFilters;

### Description

Boolean indicating if filters should be validated. Default is false.

If true and [skipUnknownFilters](Search.QueryValidationOptions-
skipUnknownFilters.html) is false, unknown filters will generate errors if no
default handler is provided with
[QueryEngine.SetDefaultFilter](Search.QueryEngine_1.SetDefaultFilter.html).

    
    
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryValidationOptions_validateFilters
    {
        [[MenuItem](MenuItem.html)("Examples/[QueryValidationOptions](Search.QueryValidationOptions.html)/validateFilters")]
        public static void RunExample()
        {
            // Set up the query validation options with no filter validation
            var validationOptions = new [QueryValidationOptions](Search.QueryValidationOptions.html) { validateFilters = false };
    
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>(validationOptions);
            queryEngine.AddFilter("id", myObj => myObj.id);
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            // Parse a query with the filter "id". There shouldn't be any errors
            var query = queryEngine.ParseQuery("id>10");
            [Debug.Assert](Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
    
            // Because the [QueryEngine](Search.QueryEngine.html) doesn't validate filters, no other filters will generate an error when parsed.
            query = queryEngine.ParseQuery("name:MyName");
            [Debug.Assert](Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
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

