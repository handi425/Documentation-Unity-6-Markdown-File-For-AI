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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).SetDefaultFilter

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

public void SetDefaultFilter(Func<TData,string,string,string,bool> handler);

### Parameters

handler | Callback used to handle the filter. Takes an object of type TData, the filter identifier, the operator, and the filter value, and returns a boolean indicating if the filter passed or not.  
---|---  
  
### Description

Sets the default filter handler for filters that were not registered.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryEngine_SetDefaultFilter
    {
        static List<MyObjectType> s_Data;
    
        [[MenuItem](MenuItem.html)("Examples/[QueryEngine](Search.QueryEngine.html)/SetDefaultFilter")]
        public static void RunExample()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            // Add a filter for MyObjectType.id that supports all operators
            queryEngine.AddFilter("id", myObj => myObj.id);
    
            // For all other filters, you can register a "default" filter handler that will be called when
            // an unknown filter token is encountered. It can also be useful for dynamic properties.
            queryEngine.SetDefaultFilter((myObj, filterId, operatorToken, filterValue) =>
            {
                if (myObj.property.name != filterId)
                    return false;
    
                if (myObj.property.type == PropertyType.String)
                {
                    if (!(myObj.property.value is string s))
                        return false;
                    switch (operatorToken)
                    {
                        case ":": return s.Contains(filterValue);
                        case "=": return s == filterValue;
                        default: return false;
                    }
                }
    
                if (myObj.property.type == PropertyType.Integer)
                {
                    if (!(myObj.property.value is int i))
                        return false;
                    if (!int.TryParse(filterValue, out var filterValueInt))
                        return false;
                    switch (operatorToken)
                    {
                        case "=": return i == filterValueInt;
                        case "!=": return i != filterValueInt;
                        case "<": return i < filterValueInt;
                        case ">": return i > filterValueInt;
                        case "<=": return i <= filterValueInt;
                        case ">=": return i >= filterValueInt;
                        default: return false;
                    }
                }
    
                return false;
            });
    
            s_Data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, property = new Property("size", PropertyType.Integer, 64) },
                new MyObjectType { id = 1, property = new Property("size", PropertyType.Integer, 128) },
                new MyObjectType { id = 2, property = new Property("tag", PropertyType.String, "item") },
                new MyObjectType { id = 3, property = new Property("tag", PropertyType.String, "car item") }
            };
    
            // Find all items that have the property "size" that is equal to 64
            var query = queryEngine.ParseQuery("size=64");
            var filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[0]), "The first item should be in the filtered list since its property \"size\" has a value of 64.");
    
            // Find all items that have the property "tag" that contains "item"
            query = queryEngine.ParseQuery("tag:item");
            filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 2, $"There should be 2 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[2]), "The third item should be in the list as its property \"tag\" contains \"item\".");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[3]), "The fourth item should be in the list as its property \"tag\" contains \"item\".");
        }
    
        enum PropertyType
        {
            Integer,
            String
        }
        struct Property
        {
            public string name { get; }
            public PropertyType type { get; }
            public object value { get; set; }
    
            public Property(string name, PropertyType type, object value)
            {
                this.name = name;
                this.type = type;
                this.value = value;
            }
        }
    
        class MyObjectType
        {
            public int id { get; set; }
            public string name { get; set; } = string.Empty;
            public [Vector2](Vector2.html) position { get; set; } = [Vector2.zero](Vector2-zero.html);
            public bool active { get; set; }
            public Property property { get; set; }
    
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

