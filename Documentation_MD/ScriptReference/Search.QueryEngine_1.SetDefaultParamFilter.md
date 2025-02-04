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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).SetDefaultParamFilter

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

public void SetDefaultParamFilter(Func<TData,string,string,string,string,bool>
handler);

### Parameters

handler | Callback used to handle the function filter. Takes an object of type TData, the filter identifier, the parameter, the operator, and the filter value, and returns a boolean indicating if the filter passed or not.  
---|---  
  
### Description

Sets the default filter handler for function filters that were not registered.

    
    
    using System.Collections.Generic;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryEngine_SetDefaultParamFilter
    {
        static List<MyObjectType> s_Data;
    
        [[MenuItem](MenuItem.html)("Examples/[QueryEngine](Search.QueryEngine.html)/SetDefaultParamFilter")]
        public static void RunExample()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
    
            // Add a filter for MyObjectType.id that supports all operators
            queryEngine.AddFilter("id", myObj => myObj.id);
    
            // Register a default filter handler for any filter with parameters.
            queryEngine.SetDefaultParamFilter((myObj, filterId, paramValue, operatorToken, filterValue) =>
            {
                if (myObj.property.name != filterId)
                    return false;
    
                if (myObj.property.type == PropertyType.Integer_Array)
                {
                    if (!(myObj.property.value is int[] integerArray))
                        return false;
                    if (!int.TryParse(paramValue, out var indexValue))
                        return false;
                    if (!int.TryParse(filterValue, out var filterValueInt))
                        return false;
                    if (indexValue < 0 || indexValue >= integerArray.Length)
                        return false;
                    switch (operatorToken)
                    {
                        case "=": return integerArray[indexValue] == filterValueInt;
                        case "!=": return integerArray[indexValue] != filterValueInt;
                        case "<": return integerArray[indexValue] < filterValueInt;
                        case ">": return integerArray[indexValue] > filterValueInt;
                        case "<=": return integerArray[indexValue] <= filterValueInt;
                        case ">=": return integerArray[indexValue] >= filterValueInt;
                        default: return false;
                    }
                }
    
                return false;
            });
    
            s_Data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, property = new Property("values", PropertyType.Integer_Array, new int[] {0, 2, 42}) },
                new MyObjectType { id = 1, property = new Property("weights", PropertyType.Integer_Array, new int[] {1000, 250, 400}) }
            };
    
            // Find all items that have the property "values" higher than 10 at index 2
            var query = queryEngine.ParseQuery("values(2)>10");
            var filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[0]), "The first item should be in the filtered list since its property \"values\" has a value higher than 10 at index 2.");
        }
    
        enum PropertyType
        {
            Integer,
            String,
            Integer_Array
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

