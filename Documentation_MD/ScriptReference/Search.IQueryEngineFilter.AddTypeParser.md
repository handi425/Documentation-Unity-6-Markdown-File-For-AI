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

#  [IQueryEngineFilter](Search.IQueryEngineFilter.html).AddTypeParser

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

public [Search.IQueryEngineFilter](Search.IQueryEngineFilter.html)
AddTypeParser(Func<string,ParseResult<TFilterConstant>> parser);

### Parameters

parser | Callback used to determine if a string can be converted into "TFilterConstant". Takes a string and returns a [ParseResult](Search.ParseResult_1.html) object. This contains the success flag, and the actual converted value if it succeeded.  
---|---  
  
### Returns

**IQueryEngineFilter** The current filter.

### Description

Add a type parser specific to the filter.

Add a type parser specific to the filter that parses a string and returns a
custom type. Used by custom operator handlers. This type parser will only be
used by this filter and will not affect other filters.

    
    
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
    

See [IQueryEngineFilter](Search.IQueryEngineFilter.html) for a complete
example.

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

