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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).GetAllFilters

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

public IEnumerable<IQueryEngineFilter> GetAllFilters();

### Returns

**IEnumerable <IQueryEngineFilter>** An enumerable of
[IQueryEngineFilter](Search.IQueryEngineFilter.html).

### Description

Get all filters added on this [QueryEngine](Search.QueryEngine_1.html).

This method returns all the filters that were added on the
[QueryEngine](Search.QueryEngine_1.html).

    
    
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryEngine_GetAllFilters
    {
        static [QueryEngine](Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
    
            // Add a filter for MyObjectType.id that supports all operators
            queryEngine.AddFilter("id", myObj => myObj.id);
            // Add a filter for MyObjectType.name that supports only contains (:), equal (=) and not equal (!=)
            queryEngine.AddFilter("n", myObj => myObj.name, new[] { ":", "=", "!=" });
            // Add a filter for MyObjectType.active that supports only equal and not equal
            queryEngine.AddFilter("a", myObj => myObj.active, new[] { "=", "!=" });
            // Add a filter for the computed property magnitude that supports equal, not equal, lesser, greater, lesser or equal and greater or equal.
            queryEngine.AddFilter("m", myObj => myObj.position.magnitude, new[] { "=", "!=", "<", ">", "<=", ">=" });
    
            // Set up what data from objects of type MyObjectType will be matched against search words
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            return queryEngine;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[QueryEngine](Search.QueryEngine.html)/GetAllFilters")]
        public static void RunExample()
        {
            var queryEngine = SetupQueryEngine();
    
            var allFilters = queryEngine.GetAllFilters();
            foreach (var filter in allFilters)
            {
                [Debug.LogFormat](Debug.LogFormat.html)([LogType.Log](LogType.Log.html), [LogOption.NoStacktrace](LogOption.NoStacktrace.html), null, $"Filter: {filter.token} - Supported operators: {(filter.supportedOperators?.Any() ?? false ? "[" + string.Join(", ", filter.supportedOperators) + "]" : "All")}");
            }
    
            // Get the filter corresponding to the token "id"
            if (!queryEngine.TryGetFilter("id", out var idFilter))
                [Debug.LogError](Debug.LogError.html)("The filter \"id\" should have been found.");
    
            [Debug.Assert](Debug.Assert.html)(idFilter != null, "Filter \"id\" should not be null.");
    
            // Remove the filter with token "id"
            var token = "id";
            queryEngine.RemoveFilter("id");
    
            var found = queryEngine.TryGetFilter(token, out idFilter);
            [Debug.Assert](Debug.Assert.html)(found == false, "Filter \"id\" should not be found.");
            [Debug.Assert](Debug.Assert.html)(idFilter == null, "Filter \"id\" should be null.");
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

