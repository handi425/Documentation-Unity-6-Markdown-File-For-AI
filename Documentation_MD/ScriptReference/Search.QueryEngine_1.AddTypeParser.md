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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).AddTypeParser

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

public void AddTypeParser(Func<string,ParseResult<TFilterConstant>> parser);

### Parameters

parser | Callback used to determine if a string can be converted into TFilterConstant. Takes a string and returns a ParseResult object. This contains the success flag, and the converted value if it succeeds.  
---|---  
  
### Description

Adds a type parser that parses a string and returns a custom type. Used by
custom operator handlers (see
[AddOperatorHandler](Search.QueryEngine_1.AddOperatorHandler.html)).

<TFilterConstant>: The type of the parsed operand that is on the right-hand
side of the operator.

    
    
    using System.Collections.Generic;
    using System.Globalization;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryEngine_AddTypeParser
    {
        static List<MyObjectType> s_Data;
    
        [[MenuItem](MenuItem.html)("Examples/[QueryEngine](Search.QueryEngine.html)/AddTypeParser")]
        public static void RunExample()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
            queryEngine.AddFilter("id", myObj => myObj.id);
            queryEngine.AddFilter("p", myObj => myObj.position, new[] { "=", "!=" });
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            // Add a new type parser for [Vector2](Vector2.html) written as "[x, y]"
            queryEngine.AddTypeParser<[Vector2](Vector2.html)>(s =>
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
            queryEngine.AddOperatorHandler("=", ([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev == fv);
            queryEngine.AddOperatorHandler("!=", ([Vector2](Vector2.html) ev, [Vector2](Vector2.html) fv) => ev != fv);
    
            s_Data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, name = "Test 1", position = new [Vector2](Vector2.html)(0, 0), active = false },
                new MyObjectType { id = 1, name = "Test 2", position = new [Vector2](Vector2.html)(0, 1), active = true },
                new MyObjectType { id = 2, name = "Test 3", position = new [Vector2](Vector2.html)(1, 0), active = false },
                new MyObjectType { id = 3, name = "Test 4", position = new [Vector2](Vector2.html)(1.2f, 0), active = false },
            };
    
            // Find all items that are located at position [0, 1]
            var query = queryEngine.ParseQuery("p=\"[0, 1]\"");
            var filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Test 2 should be in the list as its position [0, 1].");
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

