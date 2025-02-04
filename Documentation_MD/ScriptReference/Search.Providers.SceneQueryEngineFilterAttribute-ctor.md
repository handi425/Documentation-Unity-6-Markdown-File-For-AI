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

# SceneQueryEngineFilterAttribute Constructor

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

public SceneQueryEngineFilterAttribute(string token, string[]
supportedOperators);

## Declaration

public SceneQueryEngineFilterAttribute(string token, stringComparison options,
string[] supportedOperators);

## Declaration

public SceneQueryEngineFilterAttribute(string token, string
paramTransformerFunction, string[] supportedOperators);

## Declaration

public SceneQueryEngineFilterAttribute(string token, string
paramTransformerFunction, stringComparison options, string[]
supportedOperators);

### Parameters

token | The identifier of the filter. Typically what precedes the operator in a filter (i.e. "id" in "id>=2").  
---|---  
supportedOperators | List of supported operator tokens. Null for all operators.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute. See [SceneQueryEngineParameterTransformer](Search.Providers.SceneQueryEngineParameterTransformerAttribute.html) for more information.  
  
### Description

Create a filter with the corresponding token and supported operators.

The following example adds a new filter function `dist` that returns the
distance between an object and a point. This filter needs a parameter
[transformer](Search.Providers.SceneQueryEngineParameterTransformerAttribute.html)
to transform the text into a point. Also, it doesn't support the operator
"contains" (`:`).

    
    
    [SceneQueryEngineFilter("dist", "DistanceParamHandler", new[] {"=", "!=", "<", ">", "<=", ">="})]
    static float DistanceHandler([GameObject](GameObject.html) go, [Vector3](Vector3.html) p)
    {
        return (go.transform.position - p).magnitude;
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

