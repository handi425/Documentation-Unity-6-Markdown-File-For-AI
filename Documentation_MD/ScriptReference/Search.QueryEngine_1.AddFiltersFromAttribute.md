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

#  [QueryEngine<T0>](Search.QueryEngine_1.html).AddFiltersFromAttribute

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

public void AddFiltersFromAttribute();

### Description

Adds all custom filters that are identified with the method attribute
TFilterAttribute.

Allows you to register a filter with a specific type.  
  
<TFilterAttribute>: The type of the attribute defined for your custom filters.  
  
<TTransformerAttribute>: The type of the attribute defined for your custom
parameter transformers.  
  
For more information about the custom attributes, see
[QueryEngineFilterAttribute](Search.QueryEngineFilterAttribute.html) and
[QueryEngineParameterTransformerAttribute](Search.QueryEngineParameterTransformerAttribute.html).

    
    
    using [System](Rendering.VirtualTexturing.System.html);
    using System.Collections.Generic;
    using System.Globalization;
    using System.Linq;
    using [UnityEditor](UnityEditor.html);
    using UnityEditor.Search;
    using UnityEngine;
    
    static class Example_QueryEngine_AddFilterFromAttribute
    {
        static List<MyObjectType> s_Data;
    
        [[MenuItem](MenuItem.html)("Examples/[QueryEngine](Search.QueryEngine.html)/AddFiltersFromAttribute")]
        public static void RunExample()
        {
            // Set up the query engine
            var queryEngine = new [QueryEngine](Search.QueryEngine.html)<MyObjectType>();
            queryEngine.AddFilter("id", myObj => myObj.id);
            queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
            SetupPropertyHandlers(queryEngine);
    
            // Register filters with our own attributes
            queryEngine.AddFiltersFromAttribute<MyObjectFilterAttribute, MyObjectFilterParameterTransformerAttribute>();
    
            s_Data = new List<MyObjectType>()
            {
                new MyObjectType { id = 0, name = "Test 1", values = new float[] {2, 20, 42} },
                new MyObjectType { id = 1, name = "Test 2", values = new float[] {16, 64, 128} },
                new MyObjectType { id = 2, name = "Test 3", values = new float[] {123, 48, 20}, property = new Property("size", PropertyType.Integer, 64) },
                new MyObjectType { id = 3, name = "Test 4", values = new float[] {98, 45, 1}, property = new Property("size", PropertyType.Integer, 128) },
                new MyObjectType { id = 4, name = "Test 5", values = new float[] {3, 51, 78}, property = new Property("tag", PropertyType.String, "item") },
                new MyObjectType { id = 5, name = "Test 6", values = new float[] {321, 58, 32}, property = new Property("tag", PropertyType.String, "car item") }
            };
    
            // Find all items with values at index 1 lower or equal to 32
            var query = queryEngine.ParseQuery("v(1)<=32");
            var filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[0]), "The first item should be in the list.");
    
            // Find all items with property size greater or equal to 128
            query = queryEngine.ParseQuery("#size>=128");
            filteredData = query.Apply(s_Data).ToList();
            [Debug.Assert](Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
            [Debug.Assert](Debug.Assert.html)(filteredData.Contains(s_Data[3]), $"The item \"{s_Data[3].name}\" should be in the list.");
        }
    
        static void SetupPropertyHandlers([QueryEngine](Search.QueryEngine.html)<MyObjectType> qe)
        {
            qe.AddOperatorHandler(":", (Property v, int number, StringComparison sc) => PropertyIntCompare(v, number, (f, r) => f.ToString().IndexOf(r.ToString()) != -1));
            qe.AddOperatorHandler("=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f == r));
            qe.AddOperatorHandler("!=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f != r));
            qe.AddOperatorHandler("<=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f <= r));
            qe.AddOperatorHandler("<", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f < r));
            qe.AddOperatorHandler(">", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f > r));
            qe.AddOperatorHandler(">=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f >= r));
            qe.AddOperatorHandler(":", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => f.IndexOf(r, sc) != -1));
            qe.AddOperatorHandler("=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Equals(f, r, sc)));
            qe.AddOperatorHandler("!=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => !string.Equals(f, r, sc)));
            qe.AddOperatorHandler("<=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) <= 0));
            qe.AddOperatorHandler("<", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) < 0));
            qe.AddOperatorHandler(">", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) > 0));
            qe.AddOperatorHandler(">=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) >= 0));
        }
    
        static bool PropertyStringCompare(Property p, string s, Func<string, string, bool> comparer)
        {
            if (p.type != PropertyType.String)
                return false;
            return comparer((string)p.value, s);
        }
    
        static bool PropertyIntCompare(Property p, int number, Func<int, int, bool> comparer)
        {
            if (p.type != PropertyType.Integer)
                return false;
            return comparer((int)p.value, number);
        }
    
        // Define a filter for a "value" property
        [MyObjectFilter("v", "ParseFilterValuesIndex")]
        static float FilterValues(MyObjectType myObj, int index)
        {
            return myObj.values[index];
        }
    
        // Define the parameter transformer for the filter "FilterValues"
        [MyObjectFilterParameterTransformer]
        static int ParseFilterValuesIndex(string param)
        {
            if (int.TryParse(param, NumberStyles.Number, new NumberFormatInfo(), out var i))
                return i;
            return 0;
        }
    
        // Define a regular expression filter for the property "property".
        [MyObjectFilter("#([\\w.]+)", true)]
        static Property FilterProperty(MyObjectType myObj, string filterMatch)
        {
            if (myObj.property.name == filterMatch)
                return myObj.property;
            return Property.invalid;
        }
    
    
        // Create a new attribute in order to register filters of this type only
        class MyObjectFilterAttribute : [QueryEngineFilterAttribute](Search.QueryEngineFilterAttribute.html)
        {
            public MyObjectFilterAttribute(string token, string[] supportedOperators = null)
                : base(token, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, StringComparison options, string[] supportedOperators = null)
                : base(token, options, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, string paramTransformerFunction, string[] supportedOperators = null)
                : base(token, paramTransformerFunction, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, string paramTransformerFunction, StringComparison options, string[] supportedOperators = null)
                : base(token, paramTransformerFunction, options, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, bool useRegularExpression, string[] supportedOperators = null)
                : base(token, useRegularExpression, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, bool useRegularExpression, StringComparison options, string[] supportedOperators = null)
                : base(token, useRegularExpression, options, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, bool useRegularExpression, string paramTransformerFunction, string[] supportedOperators = null)
                : base(token, useRegularExpression, paramTransformerFunction, supportedOperators) {}
    
            public MyObjectFilterAttribute(string token, bool useRegularExpression, string paramTransformerFunction, StringComparison options, string[] supportedOperators = null)
                : base(token, useRegularExpression, paramTransformerFunction, options, supportedOperators) {}
        }
    
        class MyObjectFilterParameterTransformerAttribute : [QueryEngineParameterTransformerAttribute](Search.QueryEngineParameterTransformerAttribute.html) {}
    
        enum PropertyType
        {
            None,
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
    
            public static Property invalid = new Property(string.Empty, PropertyType.None, null);
        }
    
        class MyObjectType
        {
            public int id { get; set; }
            public string name { get; set; } = string.Empty;
            public [Vector2](Vector2.html) position { get; set; } = [Vector2.zero](Vector2-zero.html);
            public bool active { get; set; }
            public float[] values { get; set; } = new float[0];
            public Property property { get; set; } = Property.invalid;
    
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

