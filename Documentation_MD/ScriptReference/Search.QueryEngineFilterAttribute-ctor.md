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

# QueryEngineFilterAttribute Constructor

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

public QueryEngineFilterAttribute(string token, string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, stringComparison options,
string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, string
paramTransformerFunction, string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, string
paramTransformerFunction, stringComparison options, string[]
supportedOperators);

### Parameters

token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
---|---  
supportedOperators | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute.  
  
### Description

Create a filter with the corresponding token and supported operators.

* * *

## Declaration

public QueryEngineFilterAttribute(string token, bool useRegularExpression,
string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, bool useRegularExpression,
stringComparison options, string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, bool useRegularExpression,
string paramTransformerFunction, string[] supportedOperators);

## Declaration

public QueryEngineFilterAttribute(string token, bool useRegularExpression,
string paramTransformerFunction, stringComparison options, string[]
supportedOperators);

### Parameters

token | The identifier of the filter or regular expression that matches the filters. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
---|---  
useRegularExpression | Set this flag to true if the token is a regular expression.  
supportedOperators | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute.  
  
### Description

Create a filter with the corresponding token and supported operators.

This constructor allows custom filters with regular expressions to be
registered with an attribute.

    
    
    // Define a regular expression filter for the property "property".
    [MyObjectFilter("#([\\w.]+)", true)]
    static Property FilterProperty(MyObjectType myObj, string filterMatch)
    {
        if (myObj.property.name == filterMatch)
            return myObj.property;
        return Property.invalid;
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

