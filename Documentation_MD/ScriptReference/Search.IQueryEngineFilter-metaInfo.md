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

#  [IQueryEngineFilter](Search.IQueryEngineFilter.html).metaInfo

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

public IReadOnlyDictionary<string,string> metaInfo;

### Description

Additional information specific to the filter.

You can add and remove any additional information on a filter at any given
time. This information is not used by the
[QueryEngine](Search.QueryEngine_1.html) and does not affect the filtering in
any way. Use to provide a way to store pertinent information related to a
filter that you can fetch at a later time.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_IQueryEngineFilter_AddMetaInfo
    {
        static List<MyObjectType> s_Data;
    
        static [QueryEngine](Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
    
            // Add a filter for MyObjectType.id that supports all operators
            queryEngine.AddFilter("id", myObj => myObj.id);
    
            // Add a description to the filter
            var descriptionKey = "desc";
            var descriptionValue = "This filters the objects based on their id.";
            var exampleKey = "example";
            var exampleValue = "id>10 or id=2";
            queryEngine.TryGetFilter("id", out var filter);
            filter.AddOrUpdateMetaInfo(descriptionKey, descriptionValue)
                .AddOrUpdateMetaInfo(exampleKey, exampleValue);
    
            return queryEngine;
        }
    
        [[MenuItem](MenuItem.html)("Examples/[IQueryEngineFilter](Search.IQueryEngineFilter.html)/AddMetaInfo")]
        public static void RunExample()
        {
            var queryEngine = SetupQueryEngine();
    
            var descriptionKey = "desc";
            var allFilters = queryEngine.GetAllFilters();
            var filtersWithDescription = allFilters.Where(f => f.metaInfo.ContainsKey(descriptionKey));
    
            queryEngine.TryGetFilter("id", out var filter);
            [Debug.Assert](Debug.Assert.html)(filter != null, "Filter \"id\" should not be null.");
            [Debug.Assert](Debug.Assert.html)(filtersWithDescription.Contains(filter), "Filter \"id\" should have a description.");
    
            // For the sake of the documentation, redefine a new description key.
            var descriptionMetaInfoKey = "desc";
            filter.RemoveMetaInfo(descriptionMetaInfoKey);
    
            filtersWithDescription = allFilters.Where(f => f.metaInfo.ContainsKey(descriptionMetaInfoKey));
            [Debug.Assert](Debug.Assert.html)(!filtersWithDescription.Contains(filter), "Filter \"id\" should not have a description.");
    
            filter.ClearMetaInfo();
            var filtersWithMetaInfo = queryEngine.GetAllFilters().Where(f => f.metaInfo.Count > 0);
            [Debug.Assert](Debug.Assert.html)(!filtersWithMetaInfo.Contains(filter), "Filter \"id\" should not have any meta info.");
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

